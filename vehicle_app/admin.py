from django.contrib import admin
from .models import Vehicle, Car, Bike

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'vehicle_type', 'color', 'year']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'vehicle_type', 'color', 'year', 'num_doors']

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'vehicle_type', 'color', 'year', 'has_gear']
