# Generated by Django 5.1.3 on 2024-11-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]