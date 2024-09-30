# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication

from datetime import datetime
from .models import Vehicle, Car, Bike
from .serializers import VehicleSerializer, CarSerializer, BikeSerializer
from .permissions import IsOwnerOrReadOnly
from django.views.decorators.cache import cache_page
from django.shortcuts import render


class BaseVehicleViewSet(viewsets.ModelViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)

    def get_estimated_mileage(self, instance):

        current_year = datetime.now().year
        vehicle_age = current_year - instance.year

        try:
            car = instance.car
            return vehicle_age * 15000
        except Car.DoesNotExist:
            pass

        try:
            bike = instance.bike
            return vehicle_age * 10000
        except Bike.DoesNotExist:
            pass

        return vehicle_age * 12000

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance)

        estimated_mileage = self.get_estimated_mileage(instance)

        response_data = serializer.data
        response_data['estimated_mileage'] = estimated_mileage
        return Response(response_data)

    def list(self, request, *args, **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response_data = serializer.data

        vehicles = {vehicle.id: vehicle for vehicle in queryset}

        for vehicle_data in response_data:
            vehicle_id = vehicle_data['id']
            vehicle_instance = vehicles.get(vehicle_id)
            if vehicle_instance:
                estimated_mileage = self.get_estimated_mileage(vehicle_instance)
                vehicle_data['estimated_mileage'] = estimated_mileage
            else:
                vehicle_data['estimated_mileage'] = None

        return Response(response_data)


class VehicleViewSet(BaseVehicleViewSet):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class CarViewSet(BaseVehicleViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer


class BikeViewSet(BaseVehicleViewSet):

    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


# Create your views here.
@cache_page(60)
def home(request):
    vehicles = Vehicle.objects.all().select_related('car', 'bike').order_by('id')
    for vehicle in vehicles:

        current_year = datetime.now().year
        vehicle_age = current_year - vehicle.year
        if hasattr(vehicle, 'car'):
            vehicle.estimated_mileage = vehicle_age * 15000
        elif hasattr(vehicle, 'bike'):
            vehicle.estimated_mileage = vehicle_age * 10000
        else:
            vehicle.estimated_mileage = vehicle_age * 12000
    context = {
        'vehicles': vehicles
    }
    return render(request, 'vehicles.html', context)
