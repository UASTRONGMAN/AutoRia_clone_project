# Generated by Django 5.1.3 on 2024-11-26 22:38

import django.db.models.deletion
from django.db import migrations, models

import apps.create_car_ad.services


class Migration(migrations.Migration):

    dependencies = [
        ('create_car_ad', '0003_caradmodel_photo_alter_caradmodel_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caradmodel',
            name='photo',
        ),
        migrations.CreateModel(
            name='CarPhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to=apps.create_car_ad.services.upload_car_photo)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='create_car_ad.caradmodel')),
            ],
            options={
                'db_table': 'car_photos',
            },
        ),
    ]
