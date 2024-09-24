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

    def __str__(self):
        return f"{self.brand} - {self.vehicle_type}"

    def get_type(self):
        return f"This is a generic vehicle."

    # Overriding save method for encapsulation
    def save(self, *args, **kwargs):
        if not self.brand or not self.vehicle_type:
            raise ValidationError("Brand and type cannot be empty.")
        super().save(*args, **kwargs)


# Derived Car class with function overriding
class Car(Vehicle):
    num_doors = models.IntegerField()

    def get_type(self):
        return f"This is a car with {self.num_doors} doors."


# Derived Bike class with function overriding
class Bike(Vehicle):
    has_gear = models.BooleanField(default=False)

    def get_type(self):
        return f"This is a bike with cool gears: {self.has_gear}."


# Custom permission logic inside the model
class VehiclePermission(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    class Meta:
        unique_together = ('vehicle', 'user')
