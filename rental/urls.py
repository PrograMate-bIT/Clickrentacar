from django.urls import path

from rental.views import CreateRentalView, MyCarRequestView

urlpatterns = [
    path('<int:pk>/', CreateRentalView.as_view(), name="new_rental_request"),
    path('rental_request/',MyCarRequestView.as_view(), name="rental_request"),
]
