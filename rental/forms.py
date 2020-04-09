from django import forms
from rental.models import Request


class RentalRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['dateFrom', 'dateTo', 'timeTo', 'timeFrom', 'Commentary']
        widgets = {
            'dateFrom': forms.DateTimeInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Fecha desde', 'max_length': '15'}),
            'dateTo': forms.DateTimeInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Fecha hasta', 'max_length': '15'}),
            'timeTo': forms.NumberInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Hora desde', 'max_length': '15'}),
            'timeFrom': forms.NumberInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Hora hasta', 'max_length': '15'}),
            'Commentary': forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'Comentario', 'max_length': '15'}),
        }

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)