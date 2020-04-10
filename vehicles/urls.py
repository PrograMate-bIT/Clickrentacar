from django.urls import path
from vehicles.views import VehicleRegisterView, VehicleListView, VehiclePublicationListView, \
    VehiclePublicationDetailView, CreatePublicationView

urlpatterns = [
    path('register/', VehicleRegisterView.as_view(), name="vehicleRegister"),
    path('my_vehicles/', VehicleListView.as_view(), name="my_vehicles"),
    path('publications/', VehiclePublicationListView.as_view(), name="publications"),
    path('<int:pk>/', VehiclePublicationDetailView.as_view(), name="vehicle_publication"),
    path('publicate/', CreatePublicationView.as_view(), name="new_publication")
]
