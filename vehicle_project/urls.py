from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from vehicle_app import views

router = DefaultRouter()
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'cars', views.CarViewSet)
router.register(r'bikes', views.BikeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
