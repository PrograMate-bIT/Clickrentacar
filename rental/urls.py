from django.urls import path
from rental.views import CreateRentalView

urlpatterns = [
    path('<int:pk>/', CreateRentalView.as_view(), name="new_rental_request"),
]
