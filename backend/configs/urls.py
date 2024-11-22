from django.urls import include, path

urlpatterns = [
    path('cars_app', include('apps.create_car_application.urls')),
    path('users', include('apps.users.urls')),
]
