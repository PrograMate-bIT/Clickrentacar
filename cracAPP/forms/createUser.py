from django import forms

from usuario.models import Usuario


class CreateUser(forms.Form):
    nombre = forms.CharField(label="nombreUsuario", required=True)
    contrasenia = forms.CharField(label="contrasenia", required=True)
    ci = forms.IntegerField(label="cedula", required=True)
    # pais = forms.   <- pendiente
    # ciudad = forms.  <- pendiente
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    fechaNacimiento = forms.DateField()
    # libretaConducir = models.ForeignKey(licencia.Licencia, on_delete=models.CASCADE) <- esto no anda, en el model tampoco anda....
    correoElectronico = forms.CharField(max_length=50)
    calle = forms.CharField(max_length=50)
    esquina = forms.CharField(max_length=50)
    numDireccion = forms.IntegerField(4)
    tipoVivienda = Usuario.VIVIENDA_OPCIONES  # <- lo corregí, pero no se si esto está bien
    bizz = forms.IntegerField(4)
