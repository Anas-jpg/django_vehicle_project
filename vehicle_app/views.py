# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication

from datetime import datetime
from .models import Vehicle, Car, Bike
from .serializers import VehicleSerializer, CarSerializer, BikeSerializer
from .permissions import IsOwnerOrReadOnly


class BaseVehicleViewSet(viewsets.ModelViewSet):
    """
    A base viewset that includes common configurations for all vehicle types.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        Assign the owner of the vehicle to the currently authenticated user.
        """
        serializer.save(owner=self.request.user)

    def get_estimated_mileage(self, instance):
        """
        Calculate the estimated mileage based on the vehicle type and its age.
        """
        current_year = datetime.now().year
        vehicle_age = current_year - instance.year

        # Check if the instance is a Car
        try:
            car = instance.car  # Access related Car instance
            return vehicle_age * 15000
        except Car.DoesNotExist:
            pass

        # Check if the instance is a Bike
        try:
            bike = instance.bike  # Access related Bike instance
            return vehicle_age * 10000
        except Bike.DoesNotExist:
            pass

        # Default mileage calculation for base Vehicle
        return vehicle_age * 12000

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single vehicle instance and include the estimated mileage in the response.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        estimated_mileage = self.get_estimated_mileage(instance)

        response_data = serializer.data
        response_data['estimated_mileage'] = estimated_mileage
        return Response(response_data)

    def list(self, request, *args, **kwargs):
        """
        List all vehicle instances and include the estimated mileage for each in the response.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response_data = serializer.data

        # To optimize database queries, fetch all relevant instances in one go
        vehicles = {vehicle.id: vehicle for vehicle in queryset}

        for vehicle_data in response_data:
            vehicle_id = vehicle_data['id']
            vehicle_instance = vehicles.get(vehicle_id)
            if vehicle_instance:
                estimated_mileage = self.get_estimated_mileage(vehicle_instance)
                vehicle_data['estimated_mileage'] = estimated_mileage
            else:
                vehicle_data['estimated_mileage'] = None  # Handle missing instances gracefully

        return Response(response_data)


class VehicleViewSet(BaseVehicleViewSet):
    """
    ViewSet for handling Vehicle CRUD operations.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class CarViewSet(BaseVehicleViewSet):
    """
    ViewSet for handling Car CRUD operations.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class BikeViewSet(BaseVehicleViewSet):
    """
    ViewSet for handling Bike CRUD operations.
    """
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
