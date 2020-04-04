from django import forms

from alquiler.models import SolicitudAlquiler, RegistroAlquiler
from usuario.models import Usuario
from usuario.models import Ciudad
from vehiculo.models import Vehiculo


class createUser(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombreUsuario','nombre', 'apellido', 'contrasenia', 'ci', 'ciudad','telefono', 'fechaNacimiento', 'mail', 'calle', 'numDireccion', 'esquina']
        widgets = {
            'nombreUsuario': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Nick', 'max_length': '15'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Nombre', 'max_length': '15'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Apellido'}),
            'contrasenia': forms.PasswordInput(attrs={'class': 'form-control mt-3', 'placeholder': 'contrasenia'}),
            'ci': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Cedula'}),
            'ciudad' : forms.Select(attrs={'class':'form-control'}),
            'telefono' : forms.NumberInput(attrs={'class':'form-control'}),
            'fechaNacimiento': forms.DateTimeInput(attrs={'pleaceholder': 'Fecha de nacimiento'}),
            'mail': forms.EmailInput(attrs={"placeholder": "Requerido, 254 caracteres como máximo y debe ser válido"}),
            'calle': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Calle', 'max_length': '15'}),
            'numDireccion' : forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Numero', 'max_length': '4'}),
            'esquina': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Esquina'})
        }

class VehiculeInsert(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = ['matricula', 'propietario', 'marca', 'modelo', 'anio', 'asientos', 'puertas']
        widgeds = {
            'matricula': forms.NumberInput(attrs={'class':'form-control'}),
            'propietario': forms.Select(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Marca', 'max_length': '15'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Marca', 'max_length': '15'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control', 'max_length': '4'}),
            'asientos': forms.NumberInput(attrs={'class': 'form-control'}),
            'puertas': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class RentalRequest(forms.ModelForm):

    class Meta:
        model = SolicitudAlquiler
        fields = ['usarioSolicitante', 'vehiculo', 'startDate', 'startTime', 'costoReserva']
        widgeds = {
            'usarioSolicitante': forms.Select(attrs={'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'startDate': forms.DateTimeInput(attrs={'pleaceholder': 'Desde'}),
            'startTime': forms.DateTimeInput(attrs={'pleaceholder': 'Hasta'}),
            'costoReserva': forms.NumberInput(attrs={'class':'form-control'})
        }

class CarRental(forms.ModelForm):

    class Meta:
        model = RegistroAlquiler
        fields = ['solicitudAlquiler', 'devolucionDateReal', 'costoPorHora', 'costoPorHoraRecargo']
        widgeds = {
            'solicitudAlquiler': forms.Select(attrs={'class': 'form-control'}),
            'devolucionDateReal': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'costoPorHora': forms.NumberInput(attrs={'class': 'form-control'}),
            'costoPorHoraRecargo': forms.NumberInput(attrs={'class': 'form-control'})
        }

class Login(forms.ModelForm):
    nombre = forms.CharField(label="nombreUsuario", required=True)
    contrasenia = forms.CharField(label="contrasenia", required=True)
