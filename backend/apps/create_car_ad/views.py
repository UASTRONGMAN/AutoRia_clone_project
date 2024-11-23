from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.create_car_ad.models import CarAdModel
from apps.create_car_ad.serializers import CarApplicationSerializer


class CarListView(ListAPIView):
    serializer_class = CarApplicationSerializer
    queryset = CarAdModel.objects.all()
    permission_classes = (AllowAny, )

class CarAdCreateView(CreateAPIView):
    serializer_class = CarApplicationSerializer
    permission_classes = (IsAuthenticated, )

class CarRetrieveView(RetrieveAPIView):
    queryset = CarAdModel.objects.all()
    serializer_class = CarApplicationSerializer
    permission_classes = (AllowAny,)

class CarAdUpdateDestroyView(UpdateAPIView, DestroyAPIView):
    serializer_class = CarApplicationSerializer
    queryset = CarAdModel.objects.all()
    permission_classes = (IsAuthenticated, )
