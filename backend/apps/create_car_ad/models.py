from datetime import datetime

from django.contrib.contenttypes.fields import GenericRelation
from django.core import validators as V
from django.db import models

from configs.settings import AUTH_USER_MODEL
from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT

from core_app.models import BaseModel

from apps.create_car_ad.choices import (
    BodyTypeChoice,
    BrandChoice,
    ColorChoice,
    DriveTypeChoice,
    FuelTypeChoice,
    ModelChoice,
)
from apps.create_car_ad.regex import CarAdRegex
from apps.create_car_ad.services import upload_car_photo


class CarAdModel(BaseModel, HitCountMixin):
    class Meta:
        db_table = 'cars_ad'

    brand = models.CharField(max_length=20, choices=BrandChoice.choices)
    model = models.CharField(max_length=20, choices=ModelChoice.choices)
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(datetime.now().year)])
    price = models.CharField(validators=[V.RegexValidator(*CarAdRegex.PRICE.value)], help_text="Acceptable input options: 10 UAH or 100 USD or 100.50 EUR", max_length=20)
    color = models.CharField(max_length=12, choices=ColorChoice.choices)
    body_type = models.CharField(max_length=13, choices=BodyTypeChoice.choices)
    fuel_type = models.CharField(max_length=15, choices=FuelTypeChoice.choices)
    drive_type = models.CharField(max_length=29, choices=DriveTypeChoice.choices)
    region = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cars')
    is_active_ad = models.BooleanField(default=False)
    check_count = models.IntegerField(default=0)

    hit_count_generic = GenericRelation(
        MODEL_HITCOUNT, object_id_field='object_pk', related_query_name='hit_count_generic_relation'
    )

class CarPhotoModel(BaseModel):
    class Meta:
        db_table = 'car_photos'

    photo = models.ImageField(upload_to=upload_car_photo, blank=True)
    car = models.ForeignKey(CarAdModel, on_delete=models.CASCADE, related_name='photos')



