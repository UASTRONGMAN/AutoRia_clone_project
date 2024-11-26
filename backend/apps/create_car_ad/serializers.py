from rest_framework import serializers

from apps.create_car_ad.models import CarAdModel, CarPhotoModel


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotoModel
        fields = ('photo', )
        extra_kwargs = {'photo': {'required': True}}

class CarAdSerializer(serializers.ModelSerializer):
    photos = CarPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CarAdModel
        fields = ('id', 'brand', 'model', 'year', 'price', 'description', 'color', 'body_type', 'fuel_type', 'drive_type', 'region', 'created_at', 'updated_at', 'photos')

