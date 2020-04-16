from django import forms
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from rental.forms import RentalRequestForm, RentalConfirmedForm
from rental.models import Request
from vehicles.models import VechiclePublication


@method_decorator(login_required, name='dispatch')
class CreateRentalView(CreateView):
    form_class = RentalRequestForm
    template_name = "rental/create_rental_request.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?requested'

    def get_form(self, form_class=None):
        form = super(CreateRentalView, self).get_form()

        form.fields['dateFrom'].widget = forms.DateTimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Fecha desde'})
        form.fields['dateTo'].widget = forms.DateTimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Fecha hasta'})
        form.fields['timeTo'].widget = forms.TimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Hora desde'})
        form.fields['timeFrom'].widget = forms.TimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Hora hasta'})
        form.fields['Commentary'].widget = forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': 'Comentario'})
        return form

    def form_valid(self, form):
        form.instance.userRequest = self.request.user.profile
        form.instance.transportPublisher = VechiclePublication.objects.get(id=self.kwargs.get('pk'))
        form.instance.State = "S"
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class MyCarRequestView(ListView):
    model = Request

    def get_queryset(self):
        obj = VechiclePublication.objects.get(id=self.kwargs.get('pk'))
        return Request.objects.filter(transportPublisher=obj)

@method_decorator(login_required, name='dispatch')
class CreateConfirmedRentalView(CreateView):
    form_class = RentalConfirmedForm
    template_name = "rental/rental_aprobe.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?requested'

    def get_form(self, form_class=None):
        form = super(CreateConfirmedRentalView, self).get_form()

        form.fields['startDate'].widget = forms.DateTimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Fecha desde'})
        form.fields['endDate'].widget = forms.DateTimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Fecha hasta'})
        form.fields['starTime'].widget = forms.TimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Hora desde'})
        form.fields['endTime'].widget = forms.TimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Hora hasta'})
        form.fields['priceHour'].widget = forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Comentario'})
        return form

    def form_valid(self, form):
        form.instance.requestRent = Request.objects.get(idSol=self.kwargs.get('pk'))
        return super().form_valid(form)

