# Generated by Django 5.1.1 on 2024-09-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_app', '0003_rename_mileage_vehicle_estimated_mileage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='VehiclePermission',
        ),
    ]
