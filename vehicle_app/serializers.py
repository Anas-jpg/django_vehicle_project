from rest_framework import serializers
from .models import Vehicle, Car, Bike


class VehicleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    estimated_mileage = serializers.FloatField(read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'owner', 'brand', 'vehicle_type', 'color', 'year', 'estimated_mileage']

    # Custom field validation for 'color'
    def validate_color(self, value):
        if value not in ['RED', 'BLUE', 'GREEN', 'WHITE']:
            raise serializers.ValidationError("Invalid color choice.")
        return value

    # Object-level validation for 'year'
    def validate(self, data):
        if data['year'] > 2025:
            raise serializers.ValidationError("The year cannot be in the future.")
        return data


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'vehicle_type', 'color', 'year', 'num_doors']  # Removed estimated_mileage

    # Custom validation for the color and year fields
    def validate_color(self, value):
        if value not in ['RED', 'BLUE', 'GREEN', 'WHITE']:
            raise serializers.ValidationError("Invalid color choice.")
        return value

    def validate(self, data):
        if data['year'] > 2025:
            raise serializers.ValidationError("The year cannot be in the future.")
        return data


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['id', 'brand', 'vehicle_type', 'color', 'year', 'has_gear']  # Removed estimated_mileage

    # Custom validation for the color field
    def validate_color(self, value):
        if value not in ['RED', 'BLUE', 'GREEN', 'WHITE']:
            raise serializers.ValidationError("Invalid color choice.")
        return value

    def validate(self, data):
        if data['year'] > 2025:
            raise serializers.ValidationError("The year cannot be in the future.")
        return data
