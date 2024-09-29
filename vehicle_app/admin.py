from django.contrib import admin
from .models import Vehicle, Car, Bike


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'vehicle_type', 'color', 'year', 'estimated_mileage']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'vehicle_type', 'color', 'year', 'num_doors', 'estimated_mileage']


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'vehicle_type', 'color', 'year', 'has_gear', 'estimated_mileage']
