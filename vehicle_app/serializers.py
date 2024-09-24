from rest_framework import serializers
from .models import Vehicle, Car, Bike


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'brand', 'vehicle_type', 'color', 'year']

    # Custom field validation
    def validate_color(self, value):
        if value not in ['RED', 'BLUE', 'GREEN', 'WHITE']:
            raise serializers.ValidationError("Invalid color choice.")
        return value

    # Object-level validation overriding validate method
    def validate(self, data):
        if data['year'] > 2025:
            raise serializers.ValidationError("The year cannot be in the future.")
        return data


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'vehicle_type', 'color', 'year', 'num_doors']


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['id', 'brand', 'vehicle_type', 'color', 'year', 'has_gear']
