from django.urls import path

from apps.create_car_ad.views import (
    CarAdCreateView,
    CarAddPhotoView,
    CarAdUpdateDestroyView,
    CarListView,
    CarRetrieveView,
)

urlpatterns = [
    path('', CarListView.as_view(), name='car-list-create'),
    path('/create_ad', CarAdCreateView.as_view(), name='car-application-create'),

    path('/<int:pk>', CarRetrieveView.as_view(), name='car-retrieve'),
    path('/<int:pk>/change_ad', CarAdUpdateDestroyView.as_view(), name='car-update-destroy'),
    path('/<int:pk>/add_photo', CarAddPhotoView.as_view(), name='car-add-photo'),
]