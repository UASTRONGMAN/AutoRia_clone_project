from django.urls import path

from apps.create_car_application.views import CarApplicationListCreateView, CarApplicationRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarApplicationListCreateView.as_view(), name='car-application-list-create'),
    path('/<int:pk>', CarApplicationRetrieveUpdateDestroyView.as_view(), name='car-application-retrieve-update-destroy'),
]