from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import createUser, RentalRequest, CarRental


class UserRegister(CreateView):
    form_class = createUser
    template_name = 'cracAPP/userRegister.html'
    reverse_lazy = '/registro'

    def get_success_url(self):
        return reverse_lazy(UserRegister)

    def get_form(self, form_class=None):
        form = super(UserRegister, self).get_form()

        return form

class RentalRequestInsert(CreateView):
    form_class = RentalRequest
    template_name = "cracAPP/rentRequest.html"
    reverse_lazy = '/index'

    def get_success_url(self):
        return reverse_lazy(RentalRequestInsert)

    def get_form(self, form_class=None):
        form = super(RentalRequestInsert, self).get_form()
        return form

class CarRental(CreateView):
    form_class = CarRental
    template_name = "cracAPP/vehicleRent.html"
    reverse_lazy = '/index'

    def get_success_url(self):
        return reverse_lazy(CarRental)

    def get_form(self, form_class=None):
        form = super(CarRental, self).get_form()
        return form