from rest_framework import serializers

from apps.create_car_application.models import CarApplicationModel


class CarApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarApplicationModel
        fields = ('id', 'brand', 'model', 'year', 'price', 'description', 'created_at', 'updated_at')