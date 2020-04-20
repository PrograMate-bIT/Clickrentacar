from django.urls import path
from vehicles.views import VehicleRegisterView, VehicleListView, VehiclePublicationListView, \
    VehiclePublicationDetailView, CreatePublicationView, MyVechiclePublication, PublicationUpdate

urlpatterns = [
    path('register/', VehicleRegisterView.as_view(), name="vehicleRegister"),
    path('my_vehicles/', VehicleListView.as_view(), name="my_vehicles"),
    path('publications/', VehiclePublicationListView.as_view(), name="publications"),
    path('<int:pk>/', VehiclePublicationDetailView.as_view(), name="vehicle_publication"),
    path('publicate/', CreatePublicationView.as_view(), name="new_publication"),
    path('publicate/<int:veihcle_pk>/', CreatePublicationView.as_view(), name="new_publication"),
    path('my_publications/', MyVechiclePublication.as_view(), name="my_publications"),
    path('<int:pk>/edit_publications/', PublicationUpdate.as_view(), name="edit_publications")
]
