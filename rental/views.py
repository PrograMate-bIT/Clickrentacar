from django import forms
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from rental.forms import RentalRequestForm
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
        form.fields['timeTo'].widget = forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Hora desde'})
        form.fields['timeFrom'].widget = forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Hora hasta'})
        form.fields['Commentary'].widget = forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': 'Comentario'})
        return form

    def form_valid(self, form):
        form.instance.userRequest = self.request.user.profile
        form.instance.transportPublisher = VechiclePublication.object.get(id=self.kwargs.get('publication_pk'))
        form.instance.State = "S"
        return super().form_valid(form)

"""
    form_class = RentalRequestForm
    template_name = "create_rental_request.html"

    def get_success_url(self):
        return reverse_lazy('home') + '?register'

    def get_form(self, form_class=None):
        form = super(CreateRentalView, self).get_form()

        form.fields['dateFrom'].widget = forms.DateTimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Fecha desde'})
        form.fields['dateTo'].widget = forms.DateTimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Fecha hasta'})
        form.fields['timeTo'].widget = forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Hora desde'})
        form.fields['timeFrom'].widget = forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Hora hasta'})
        form.fields['Commentary'].widget = forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': 'Comentario'})
        return form

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)
"""