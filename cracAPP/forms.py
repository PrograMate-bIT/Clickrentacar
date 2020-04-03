from django import forms
from usuario.models import Usuario
from usuario.models import Ciudad


class createUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombreUsuario', 'nombre', 'apellido', 'contrasenia', 'ci', 'ciudad', 'telefono', 'fechaNacimiento',
                  'mail']
        widgets = {
            'nombreUsuario': forms.TextInput(
                attrs={'class': 'form-control mt-3', 'placeholder': 'Nombre de usuario', 'max_length': '15'}),
            'nombre': forms.TextInput(
                attrs={'class': 'form-control mt-3', 'placeholder': 'Nombre', 'max_length': '15'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Apellido'}),
            'contrasenia': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'contrasenia'}),
            'ci': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Cedula'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}),
            'fechaNacimiento': forms.DateTimeInput(attrs={'pleaceholder': 'Fecha de nacimiento'}),
            'mail': forms.EmailInput(attrs={"placeholder": "Requerido, 254 caracteres como máximo y debe ser válido"})
        }

    # nombre = forms.CharField(label="nombreUsuario", required=True)
    # contrasenia = forms.CharField(label="contrasenia", required=True)
    # ci = forms.IntegerField(label="cedula", required=True)
    # pais = forms.CharField(label="pais", required=True)
    # ciudad = forms.CharField(label="ciudad", required=True)
    # nombre = forms.CharField(max_length=15)
    # apellido = forms.CharField(max_length=15)
    # fechaNacimiento = forms.DateField()
    # libretaConducir = ??????????????????????
    # correoElectronico = forms.CharField(max_length=50)
    # calle = forms.CharField(max_length=50)
    # esquina = forms.CharField(max_length=50)
    # numDireccion = forms.IntegerField()
    # tipoVivienda = Usuario.VIVIENDA_OPCIONES  # <- creo que esta mal
    # bizz = forms.IntegerField()


class Login(forms.Form):
    nombre = forms.CharField(label="nombreUsuario", required=True)
    contrasenia = forms.CharField(label="contrasenia", required=True)
