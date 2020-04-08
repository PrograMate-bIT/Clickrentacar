from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django import forms
from vehicles.forms import VehicleRegisterForm

@method_decorator(login_required, name='dispatch')
class VehicleRegisterView(CreateView):
    form_class = VehicleRegisterForm
    template_name = "vehicles/vehicleRegister.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?register'

    def get_form(self, form_class=None):
        form = super(VehicleRegisterView, self).get_form()

        form.fields['carRegistration'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Matricula'})
        form.fields['brand'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Marca'})
        form.fields['carModel'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Modelo'})
        form.fields['year'].widget = forms.NumberInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Año'})
        form.fields['seatsNumber'].widget = forms.NumberInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Numero de asientos'})
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)
