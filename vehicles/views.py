from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView
from django import forms


from .models import Vehicle, Profile, VechiclePublication
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
            attrs={'class': 'form-control mb-2', 'placeholder': 'Matricula'})
        form.fields['brand'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Marca'})
        form.fields['carModel'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Modelo'})
        form.fields['year'].widget = forms.NumberInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Año'})
        form.fields['seatsNumber'].widget = forms.NumberInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Numero de asientos'})
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


class VehicleListView(ListView):
    model = Vehicle
    template_name = "vehicles/vehicle_list.html"
    paginate_by = 10

    def get_vehicles(self):
        # devuelve el vehiculos del usuario logueado
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        vehicle = Vehicle.objects.all().filter(owner=profile)
        return vehicle

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'give-default-value')
        order = self.request.GET.get('orderby', 'give-default-value')
        new_context = self.get_vehicles()
        return new_context

    def get_context_data(self, **kwargs):
        context = super(VehicleListView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'give-default-value')
        context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
        return context


class VehicleDetailView(DetailView):
    model = Vehicle

class VehiclePublicationListView(ListView):
    model = VechiclePublication

class VehiclePublicationDetailView(DetailView):
    model = VechiclePublication
