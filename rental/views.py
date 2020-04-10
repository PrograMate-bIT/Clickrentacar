from django import forms
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from rental.forms import RentalRequestForm


@method_decorator(login_required, name='dispatch')
class CreateRentalView(CreateView):
    form_class = RentalRequestForm
    template_name = ""

    def get_success_url(self):
        return reverse_lazy('home')

    def get_form(self, form_class=None):
        form = super(CreateRentalView, self).get_form()

        form.fields['dateFrom'].widget = forms.DateTimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Fecha desde'})
        form.fields['dateTo'].widget = forms.DateTimeInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Fecha hasta'})
        form.fields['timeTo'].widget = forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Hora desde'})
        form.fields['timeFrom'].widget = forms.NumberInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Hora hasta'})
        form.fields['Commentary'].widget = forms.Textarea(attrs={'class': 'form-control mb-2', 'placeholder': 'Comentario'})
        return form
