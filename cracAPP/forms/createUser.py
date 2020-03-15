from django import  forms

class CreateUser(forms.Form):
    nombre = forms.CharField(label="nombreUsuario", required=True)
    contrasenia = forms.CharField(label="contrasenia", required=True)
    ci = forms.IntegerField(primary_key=True)
    pais = forms.
    ciudad = forms.
    nombre = forms.CharField(max_length=15)
    apellido = forms.CharField(max_length=15)
    fechaNacimiento = forms.DateField()
    # libretaConducir = models.ForeignKey(licencia.Licencia, on_delete=models.CASCADE)
    correoElectronico = forms.CharField(max_length=50)
    calle = forms.CharField(max_length=50)
    esquina = forms.CharField(max_length=50)
    numDireccion = forms.IntegerField(4)
    tipoVivienda = VIVIENDA_OPCIONES
    bizz = forms.IntegerField(4)