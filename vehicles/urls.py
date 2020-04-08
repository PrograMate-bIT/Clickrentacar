from django.urls import path
from vehicles.views import VehicleRegisterView

urlpatterns = [
    path('register/', VehicleRegisterView.as_view(), name="vehicleRegister"),
]