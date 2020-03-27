from django import forms


class CreateUser(forms.Form):
    nombre = forms.CharField(label="nombreUsuario", required=True)
    contrasenia = forms.CharField(label="contrasenia", required=True)
    ci = forms.IntegerField(label="cedula", required=True)
    pais = forms.CharField(label="pais", required=True)
    ciudad = forms.CharField(label="ciudad", required=True)
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    fechaNacimiento = forms.DateField()
    # libretaConducir = ??????????????????????
    correoElectronico = forms.CharField(max_length=50)
    calle = forms.CharField(max_length=50)
    esquina = forms.CharField(max_length=50)
    numDireccion = forms.IntegerField()
    # tipoVivienda = Usuario.VIVIENDA_OPCIONES  # <- creo que esta mal
    bizz = forms.IntegerField()
