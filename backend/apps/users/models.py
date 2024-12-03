from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V
from django.db import models

from core_app.models import BaseModel

from apps.create_car_ad.models import CarAdModel
from apps.users.managers import UserManager
from apps.users.regex import ProfileRegex


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_premium_user = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15, validators=[V.RegexValidator(*ProfileRegex.PHONE_NUMBER.value)])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')

