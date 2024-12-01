from django.urls import path

from apps.create_car_ad.views import (
    CarAdCreateView,
    CarAddPhotosView,
    CarAdUpdateDestroyView,
    CarCheckCensorshipView,
    CarListView,
    CarRetrieveView,
)

urlpatterns = [
    path('', CarListView.as_view(), name='car-list'),
    path('/create_ad', CarAdCreateView.as_view(), name='car-application-create'),

    path('/<int:pk>', CarRetrieveView.as_view(), name='car-retrieve'),
    path('/<int:pk>/change_ad', CarAdUpdateDestroyView.as_view(), name='car-update-destroy'),
    path('/<int:pk>/add_photos', CarAddPhotosView.as_view(), name='car-add-photos'),
    path('/<int:pk>/check_censorship', CarCheckCensorshipView.as_view(), name='car-check-censorship'),
]