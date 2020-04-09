from django.urls import path
from vehicles.views import VehicleRegisterView, VehicleListView

urlpatterns = [
    path('register/', VehicleRegisterView.as_view(), name="vehicleRegister"),
    path('my_vehicles', VehicleListView.as_view(),name="my_vehicles"),
]