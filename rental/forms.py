from django import forms
from rental.models import Request, Confirmed


class RentalRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['dateFrom', 'dateTo', 'timeTo', 'timeFrom', 'Commentary']
        widgets = {
            'dateFrom': forms.DateTimeInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Fecha desde', 'max_length': '15'}),
            'dateTo': forms.DateTimeInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Fecha hasta', 'max_length': '15'}),
            'timeTo': forms.TimeInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Hora desde', 'max_length': '15'}),
            'timeFrom': forms.TimeInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Hora hasta', 'max_length': '15'}),
            'Commentary': forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'Comentario', 'max_length': '15'}),
        }

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)

class RentalConfirmedForm(forms.ModelForm):
    class Meta:
        model = Confirmed
        fields = ['startDate', 'endDate', 'starTime', 'endTime', 'priceHour']
        widgets = {
        'startDate' : forms.DateTimeInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Fecha desde', 'max_length': '15'}),
        'endDate' : forms.DateTimeInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Fecha hasta', 'max_length': '15'}),
        'starTime' : forms.TimeInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Hora desde', 'max_length': '15'}),
        'endTime' : forms.TimeInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Hora hasta', 'max_length': '15'}),
        'priceHour' : forms.NumberInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Precio', 'max_length': '15'}),
        }
