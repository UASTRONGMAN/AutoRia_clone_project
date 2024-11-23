from django.urls import include, path

urlpatterns = [
    path('cars_ad', include('apps.create_car_ad.urls')),
    path('users', include('apps.users.urls')),
    path('auth', include('apps.auth.urls')),
]
