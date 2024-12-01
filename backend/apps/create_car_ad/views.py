from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from better_profanity import profanity

from core_app.services.email_service import EmailService

from apps.create_car_ad.models import CarAdModel
from apps.create_car_ad.serializers import CarAdSerializer, CarPhotoSerializer


class CarListView(ListAPIView):
    serializer_class = CarAdSerializer
    queryset = CarAdModel.objects.all()
    permission_classes = (AllowAny, )

class CarAdCreateView(GenericAPIView):
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

class CarRetrieveView(RetrieveAPIView):
    queryset = CarAdModel.objects.all()
    serializer_class = CarAdSerializer
    permission_classes = (AllowAny,)

class CarAdUpdateDestroyView(UpdateAPIView, DestroyAPIView):
    queryset = CarAdModel.objects.all()
    permission_classes = (IsAuthenticated, )

class CarAddPhotosView(GenericAPIView):
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
