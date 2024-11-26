from rest_framework import serializers

from apps.create_car_ad.models import CarAdModel


class CarAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdModel
        fields = ('id', 'brand', 'model', 'year', 'price', 'description', 'color', 'body_type', 'fuel_type', 'drive_type', 'region', 'created_at', 'updated_at')

class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAdModel
        fields = ('photo', )
        extra_kwargs = {'photo': {'required': True}}