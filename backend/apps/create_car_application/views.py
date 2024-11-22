from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.create_car_application.models import CarApplicationModel
from apps.create_car_application.serializers import CarApplicationSerializer


class CarApplicationListCreateView(ListCreateAPIView):
    serializer_class = CarApplicationSerializer
    queryset = CarApplicationModel.objects.all()

class CarApplicationRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarApplicationSerializer
    queryset = CarApplicationModel.objects.all()
