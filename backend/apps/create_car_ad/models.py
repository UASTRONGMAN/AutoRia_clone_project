from datetime import datetime

from django.core import validators as V
from django.db import models

from core_app.models import BaseModel

from apps.create_car_ad.choices import BrandChoice, ModelChoice


class CarAdModel(BaseModel):
    class Meta:
        db_table = 'cars_ad'

    brand = models.CharField(max_length=20, choices=BrandChoice.choices)
    model = models.CharField(max_length=20, choices=ModelChoice.choices)
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1_000_000_000)])
    # photo = models.ImageField(blank=True, null=True)
    # region = models.CharField(max_length=50)
    description = models.TextField(blank=True)

