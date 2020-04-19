from django.urls import path
from rental.views import CreateRentalView, MyLessorRentals, MyLesseeRentals

from rental.views import CreateRentalView, MyCarRequestView, CreateConfirmedRentalView

urlpatterns = [
    path('<int:pk>/', CreateRentalView.as_view(), name="new_rental_request"),
    path('<int:pk>/rental_request/', MyCarRequestView.as_view(), name="rental_request"),
    path('<int:pk>/rental_aprobe/', CreateConfirmedRentalView.as_view(), name="rental_aprobe"),
    path('my_rental_confirmed/', MyLessorRentals.as_view(), name="rental_confirmed"),
    path('my_request_confirmed/', MyLesseeRentals.as_view(), name="request_confirmed"),
]
