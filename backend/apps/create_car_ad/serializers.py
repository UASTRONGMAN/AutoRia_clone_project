from rest_framework import serializers

from apps.create_car_ad.models import CarAdModel


class CarApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdModel
        fields = ('id', 'brand', 'model', 'year', 'price', 'description', 'created_at', 'updated_at')