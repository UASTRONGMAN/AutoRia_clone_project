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
    RSQ5 = 'RSQ5'
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