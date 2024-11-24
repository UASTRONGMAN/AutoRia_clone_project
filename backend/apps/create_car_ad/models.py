from datetime import datetime

# from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

# from core_app.dataclasses.user_dataclass import User
from core_app.models import BaseModel

from apps.create_car_ad.choices import (
    BodyTypeChoice,
    BrandChoice,
    ColorChoice,
    DriveTypeChoice,
    FuelTypeChoice,
    ModelChoice,
)

# from apps.users.models import UserModel

# UserModel: User = get_user_model()


class CarAdModel(BaseModel):
    class Meta:
        db_table = 'cars_ad'

    brand = models.CharField(max_length=20, choices=BrandChoice.choices)
    model = models.CharField(max_length=20, choices=ModelChoice.choices)
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1_000_000_000)])
    color = models.CharField(max_length=12, choices=ColorChoice.choices)
    body_type = models.CharField(max_length=13, choices=BodyTypeChoice.choices)
    fuel_type = models.CharField(max_length=15, choices=FuelTypeChoice.choices)
    drive_type = models.CharField(max_length=29, choices=DriveTypeChoice.choices)
    region = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')
    # photo = models.ImageField(blank=True, null=True)

