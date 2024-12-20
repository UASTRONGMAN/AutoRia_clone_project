# Generated by Django 5.1.3 on 2024-11-23 18:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarAdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('BMW', 'Bmw'), ('Audi', 'Audi'), ('Mercedes', 'Mercedes'), ('Volvo', 'Volvo'), ('Nissan', 'Nissan'), ('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Bugatti', 'Bugatti'), ('Lamborghini', 'Lamborghini'), ('Mazda', 'Mazda')], max_length=20)),
                ('model', models.CharField(choices=[('M8', 'M8'), ('M3', 'M30'), ('RSQ5', 'Rsq5'), ('Q8', 'Q8'), ('Brabus', 'Brabus'), ('CLS350', 'Cls350'), ('XC90', 'Xc90'), ('Qashqai', 'Qashqai'), ('Camry', 'Camry'), ('Civic', 'Civic'), ('Veyron', 'Veyron'), ('Urus', 'Urus'), ('CX-60', 'Cx60')], max_length=20)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2024)])),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000000000)])),
                ('color', models.CharField(choices=[('White', 'White'), ('Grey', 'Grey'), ('Black', 'Black'), ('Blue', 'Blue'), ('Red', 'Red'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Brown', 'Brown'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Beige', 'Beige'), ('Pink', 'Pink'), ('Purple', 'Purple'), ('Orange', 'Orange')], max_length=12)),
                ('body_type', models.CharField(choices=[('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Station wagon', 'Station Wagon'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Crossover', 'Crossover'), ('SUV', 'Suv'), ('Pickup', 'Pickup'), ('Minivan', 'Minivan'), ('Liftback', 'Liftback'), ('Van', 'Van'), ('Roadster', 'Roadster')], max_length=13)),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('LPG', 'Lpg'), ('CNG', 'Cng'), ('Hybrid', 'Hybrid'), ('Electricity', 'Electric'), ('Biodiesel', 'Biodiesel'), ('Hydrogen fuel', 'Hydrogen Fuel')], max_length=15)),
                ('drive_type', models.CharField(choices=[('Front wheel drive', 'Front Wheel Drive'), ('Rear wheel drive', 'Rear Wheel Drive'), ('All wheel drive', 'All Wheel Drive'), ('Four wheel drive', 'Four Wheel Drive'), ('Electric drive', 'Electric Drive')], max_length=29)),
                ('region', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'cars_ad',
            },
        ),
    ]
