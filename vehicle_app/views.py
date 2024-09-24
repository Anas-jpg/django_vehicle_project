from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .models import Vehicle, Car, Bike
from .serializers import VehicleSerializer, CarSerializer, BikeSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # Calculate estimated mileage based on vehicle type
        current_year = datetime.now().year
        vehicle_age = current_year - instance.year

        if isinstance(instance, Car):
            estimated_mileage = vehicle_age * 15000
        elif isinstance(instance, Bike):
            estimated_mileage = vehicle_age * 10000
        else:
            estimated_mileage = vehicle_age * 12000  # Example default value

        response_data = serializer.data
        response_data['estimated_mileage'] = estimated_mileage
        return Response(response_data)

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Calculate mileage for each vehicle in the queryset
        response_data = serializer.data
        current_year = datetime.now().year
        for vehicle_data in response_data:
            vehicle_instance = self.get_queryset().get(id=vehicle_data['id'])
            vehicle_age = current_year - vehicle_data['year']  # Get year from vehicle data

            if isinstance(vehicle_instance, Car):
                estimated_mileage = vehicle_age * 15000
            elif isinstance(vehicle_instance, Bike):
                estimated_mileage = vehicle_age * 10000
            else:
                estimated_mileage = vehicle_age * 12000  # Example default value

            vehicle_data['estimated_mileage'] = estimated_mileage

        return Response(response_data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


class BikeViewSet(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    permission_classes = [IsAuthenticated]
