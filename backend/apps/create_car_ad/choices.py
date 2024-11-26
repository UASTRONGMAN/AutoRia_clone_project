from django.db import models


class BrandChoice(models.TextChoices):
    BMW = 'BMW'
    Audi = 'Audi'
    Mercedes = 'Mercedes'
    Volvo = 'Volvo'
    Nissan = 'Nissan'
    Toyota = 'Toyota'
    Honda = 'Honda'
    Bugatti = 'Bugatti'
    Lamborghini = 'Lamborghini'
    Mazda = 'Mazda'

class ModelChoice(models.TextChoices):
    M8 = 'M8'
    M30 = 'M3'
    RSQ7 = 'RSQ7'
    Q8 = 'Q8'
    Brabus = 'Brabus'
    CLS350 = 'CLS350'
    XC90 = 'XC90'
    Qashqai = 'Qashqai'
    Camry = 'Camry'
    Civic = 'Civic'
    Veyron = 'Veyron'
    Urus = 'Urus'
    CX60 = 'CX-60'
    
class ColorChoice(models.TextChoices):
    White = 'White'
    Grey = 'Grey'
    Black = 'Black'
    Blue = 'Blue'
    Red = 'Red'
    Green = 'Green'
    Yellow = 'Yellow'
    Brown = 'Brown'
    Silver = 'Silver'
    Gold = 'Gold'
    Beige = 'Beige'
    Pink = 'Pink'
    Purple = 'Purple'
    Orange = 'Orange'

class BodyTypeChoice(models.TextChoices):
    Sedan = 'Sedan'
    Hatchback = 'Hatchback'
    Station_wagon = 'Station wagon'
    Coupe = 'Coupe'
    Convertible = 'Convertible'
    Crossover = 'Crossover'
    SUV = 'SUV'
    Pickup = 'Pickup'
    Minivan = 'Minivan'
    Liftback = 'Liftback'
    Van = 'Van'
    Roadster = 'Roadster'

class FuelTypeChoice(models.TextChoices):
    Petrol = 'Petrol'
    Diesel = 'Diesel'
    LPG = 'LPG'
    CNG = 'CNG'
    Hybrid = 'Hybrid',
    Electric = 'Electricity'
    Biodiesel = 'Biodiesel'
    Hydrogen_fuel = 'Hydrogen fuel'

class DriveTypeChoice(models.TextChoices):
    Front_wheel_drive = 'Front wheel drive'
    Rear_wheel_drive = 'Rear wheel drive'
    All_wheel_drive = 'All wheel drive'
    Four_wheel_drive = 'Four wheel drive'
    Electric_drive = 'Electric drive'


