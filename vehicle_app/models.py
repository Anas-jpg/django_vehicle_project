from django.db import models
from rest_framework.exceptions import ValidationError


class Vehicle(models.Model):
    COLOR_CHOICES = [
        ('RED', 'Red'),
        ('BLUE', 'Blue'),
        ('GREEN', 'Green'),
        ('WHITE', 'White'),
    ]

    brand = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)
    color = models.CharField(choices=COLOR_CHOICES, max_length=50)
    year = models.PositiveIntegerField()
    estimated_mileage = models.FloatField(default=0.0)  # Current mileage field

    def __str__(self):
        return f"{self.brand} - {self.vehicle_type}"

    def save(self, *args, **kwargs):
        if not self.brand or not self.vehicle_type:
            raise ValidationError("Brand and type cannot be empty.")
        super().save(*args, **kwargs)


class Car(Vehicle):
    num_doors = models.IntegerField()


class Bike(Vehicle):
    has_gear = models.BooleanField(default=False)
