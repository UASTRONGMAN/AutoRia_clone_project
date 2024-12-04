from datetime import timedelta

from django.contrib.contenttypes.models import ContentType
from django.db.models import Avg, Case, F, FloatField, Value, When
from django.utils.timezone import now

from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

import requests
from better_profanity import profanity
from hitcount.models import Hit, HitCount

from core_app.services.email_service import EmailService

from apps.create_car_ad.models import CarAdModel
from apps.create_car_ad.serializers import CarAdSerializer, CarPhotoSerializer


class CarListView(ListAPIView):
    """
    Вивід всіх оголошень з авто.
    """

    serializer_class = CarAdSerializer
    permission_classes = (AllowAny, )
    queryset = CarAdModel.objects.all()


class CarAdCreateView(GenericAPIView):
    """
    Створення оголошення авто за моделлю CarAdModel.
    """

    serializer_class = CarAdSerializer
    permission_classes = (IsAuthenticated, )


    def post(self, *args, **kwargs):
        user = self.request.user
        if user.is_premium_user or user.cars.count() < 1:
            data = self.request.data
            serializer = CarAdSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif not user.is_premium_user and user.cars.count() == 1:
            return Response({"detail": "Your ability to create car ads has already been exhausted. If you want to create more than one ad, you have to buy premium status of user."})

class CarRetrieveView(GenericAPIView):

    """
    Вивід оголошення за переданою id цього оголошення в посиланні.
    """

    permission_classes = (AllowAny,)
    queryset = CarAdModel.objects.all()

    def get(self, *args, **kwargs):
        user = self.request.user


        if user.is_authenticated and getattr(user, "is_premium_user", False):
            car = self.get_object()
            url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
            res = requests.get(url).json()
            USD = res.pop(-1)
            EUR = res.pop(0)
            UAH_TO_USD = 1 / float(USD['sale'])
            EUR_TO_USD = float(EUR['buy']) / float(USD['sale'])

            converted_price_to_usd = Case(
                When(price__endswith=" UAH", then=F('price') * Value(UAH_TO_USD)),
                When(price__endswith=" EUR", then=F('price') * Value(EUR_TO_USD)),
                When(price__endswith=" USD", then=F('price')),
                output_field=FloatField()
            )

            content_type = ContentType.objects.get_for_model(CarAdModel)
            car_price_by_region = CarAdModel.objects.filter(region=car.region, brand=car.brand).annotate(price_usd=converted_price_to_usd).aggregate(Avg('price_usd')).get('price_usd__avg')
            car_price_by_brand = CarAdModel.objects.filter(brand=car.brand).annotate(price_usd=converted_price_to_usd).aggregate(Avg('price_usd')).get('price_usd__avg')

            hitcounts = HitCount.objects.filter(content_type=content_type)
            last_day = now() - timedelta(days=1)
            last_week = now() - timedelta(weeks=1)
            last_month = now() - timedelta(days=30)

            daily_hits = Hit.objects.filter(
                created__gte=last_day,
                hitcount__in=hitcounts
            ).count()

            weekly_hits = Hit.objects.filter(
                created__gte=last_week,
                hitcount__in=hitcounts
            ).count()

            monthly_hits = Hit.objects.filter(
                created__gte=last_month,
                hitcount__in=hitcounts
            ).count()

            total_hits = Hit.objects.filter(hitcount__in=hitcounts).count()


            count, gap, currency = car.price.partition(' ')
            count = float(count)

            converted_prices = {}
            match currency:
                case 'UAH':
                    converted_prices['USD'] = round(count / float(USD['sale']), 2)
                    converted_prices['EUR'] = round(count / float(EUR['sale']), 2)
                case 'USD':
                    converted_prices['UAH'] = round(count * float(USD['buy']), 2)
                    converted_prices['EUR'] = round((count * float(USD['buy'])) / float(EUR['sale']), 2)
                case 'EUR':
                    converted_prices['UAH'] = round(count * float(EUR['buy']), 2)
                    converted_prices['USD'] = round((count * float(EUR['buy'])) / float(USD['sale']), 2)


            serializer = CarAdSerializer(car)
            return Response({
                "data": serializer.data,
                "average price by region": car_price_by_region,
                "average price by brand": car_price_by_brand,
                "hits by last day":  daily_hits,
                "hits by last week": weekly_hits,
                "hits by last month": monthly_hits,
                "total hits": total_hits,
                "converted prices": converted_prices
            }, status=status.HTTP_200_OK)

        car = self.get_object()
        serializer = CarAdSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CarAdUpdateDestroyView(UpdateAPIView, DestroyAPIView):

    """
    Реалізація методів зміни, часткової та повної, а також видалення оголошення за переданим id в посиланні.
    """

    queryset = CarAdModel.objects.all()
    permission_classes = (IsAuthenticated, )

class CarAddPhotosView(GenericAPIView):

    """
    Додавання фотографій до оголошення.
    """

    permission_classes = (IsAuthenticated, )
    serializer_class = CarPhotoSerializer
    queryset = CarAdModel.objects.all()

    def put(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for index in files:
            serializer = CarPhotoSerializer(data={'photo': files[index]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        car_serializer = CarAdSerializer(car)
        return Response(car_serializer.data, status=status.HTTP_200_OK)


class CarCheckCensorshipView(GenericAPIView):

    """
    Проведення перевірки оголошення на цензуру.
    """

    queryset = CarAdModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        car = self.get_object()
        corrections_needed = False

        fields_to_check = ['description', 'region']

        for field in fields_to_check:
            field_value = getattr(car, field, "")
            if field_value and profanity.contains_profanity(field_value):
                corrections_needed = True
                return Response({
                    "details": "You need to fix your ad."
                }, status=status.HTTP_200_OK)

        if not corrections_needed:
            car.is_active_ad = True
            car.check_count = 0
            car.save()
            return Response({
                "details": "Your ad pass the censorship validation. Ad is active and it adds on platform."
            }, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        data = self.request.data
        car = self.get_object()
        user = self.request.user

        profanity.load_censor_words()
        fields_to_check = ['description', 'region']

        for field in fields_to_check:
            if field in data and data[field]:
                if profanity.contains_profanity(data[field]):
                    car.check_count += 1
                    car.save()
                    if car.check_count < 3:
                        return Response({
                            "details": f"The field '{field}' contains inappropriate language. Your ad will be deactivated after 3 failed attempts."
                        })
                    else:
                        EmailService.obscene_language_varification(user, car.id, user.profile.name, user.profile.surname)
                        return Response({
                            "details": f"The field '{field}' contains inappropriate language. Your ad is deactivated after 3 failed attempts."
                        })

        car.is_active_ad = True
        car.check_count = 0
        car.save()
        serializer = CarAdSerializer(car, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "details": "Your ad has been successfully updated and activated.",
            "data": serializer.data
        },status=status.HTTP_200_OK)
