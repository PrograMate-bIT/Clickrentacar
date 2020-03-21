from django.db import models

from . import ciudad  # , licencia


class Usuario(models.Model):
    CASA = "Casa"
    APARTAMENTO = "Apartamento"
    VIVIENDA_OPCIONES = [
        (CASA, "Casa"),
        (APARTAMENTO, "Apartamento")
    ]
    ci = models.IntegerField(primary_key=True)
    nombreUsuario = models.CharField(default="", unique=True, max_length=30)
    contrasenia = models.CharField(default="", max_length=30)
    ciudad = models.ForeignKey(ciudad.Ciudad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    fechaNacimiento = models.DateField()
    # libretaConducir = models.ForeignKey(licencia.Licencia, on_delete=models.CASCADE)
    correoElectronico = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    esquina = models.CharField(max_length=50)
    numDireccion = models.IntegerField(4)
    tipoVivienda = VIVIENDA_OPCIONES
    bizz = models.IntegerField(4)

    def __str__(self):
        return str("nombre : " + self.nombre + " apellido: " + self.apellido + " ci: " + self.ci)
