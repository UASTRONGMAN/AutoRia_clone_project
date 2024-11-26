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
            return Response('Your ability to create car ads has already been exhausted. If you want to create more than one ad, you have to buy premium status of user.')

class CarRetrieveView(RetrieveAPIView):
    queryset = CarAdModel.objects.all()
    serializer_class = CarAdSerializer
    permission_classes = (AllowAny,)

class CarAdUpdateDestroyView(UpdateAPIView, DestroyAPIView):
    serializer_class = CarAdSerializer
    queryset = CarAdModel.objects.all()
    permission_classes = (IsAuthenticated, )

class CarAddPhotoView(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CarPhotoSerializer
    queryset = CarAdModel.objects.all()
    http_method_names = ['put']

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)


