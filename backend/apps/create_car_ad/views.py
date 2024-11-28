from rest_framework import status
from rest_framework.generics import DestroyAPIView, GenericAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

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
        