from django.db import models

from model import Pais, Licencia, Ciudad


class Cuenta(models.Model):
    ci = models.IntegerField(primary_key=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    fechaNacimiento = models.DateField()
    libretaConducir = models.ForeignKey(Licencia, on_delete=models.CASCADE)
    correoElectronico = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    esquina = models.CharField(max_length=50)
    numDireccion = models.IntegerField(4)
    tipoVivienda = models.IntegerField(1)
    bizz = models.IntegerField(4)
