from django.db.models import Count, F, Q

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.create_car_ad.models import CarAdModel
from apps.create_car_ad.serializers import CarAdSerializer
from apps.users.views import UserModel


class CarListView(ListAPIView):
    serializer_class = CarAdSerializer
    queryset = CarAdModel.objects.all()
    permission_classes = (AllowAny, )

class CarAdCreateView(GenericAPIView):
    serializer_class = CarAdSerializer
    permission_classes = (IsAuthenticated, )

    # def count(self, cars:dict):
    #     print(CarAdModel.objects.annotate(
    #         car_count=Count('car', filter=Q(user_id=F('id')))
    #     ))
    #     print(13)

    def post(self, *args, **kwargs):

        users_with_car_counts = UserModel.objects.annotate(car_count=Count('cars', distinct=True))
        for user in users_with_car_counts:
            print(f"User ID: {user.id}, Email: {user.email}, Cars Created: {user.car_count}")

        data = self.request.data
        serializer = CarAdSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CarRetrieveView(RetrieveAPIView):
    queryset = CarAdModel.objects.all()
    serializer_class = CarAdSerializer
    permission_classes = (AllowAny,)

class CarAdUpdateDestroyView(UpdateAPIView, DestroyAPIView):
    serializer_class = CarAdSerializer
    queryset = CarAdModel.objects.all()
    permission_classes = (IsAuthenticated, )
