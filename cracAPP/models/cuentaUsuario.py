from django.db import models

from . import pais, ciudad  # , licencia


class Usuario(models.Model):

    ci = models.IntegerField(primary_key=True)
    pais = models.ForeignKey(pais.Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(ciudad.Ciudad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    fechaNacimiento = models.DateField()
    # libretaConducir = models.ForeignKey(licencia.Licencia, on_delete=models.CASCADE)
    correoElectronico = models.CharField(max_length=50)
    calle = models.CharField(max_length=50)
    esquina = models.CharField(max_length=50)
    numDireccion = models.IntegerField(4)
    tipoVivienda = models.IntegerField(1)
    bizz = models.IntegerField(4)

    def __str__(self):
        return str("nombre : "+self.nombre+" apellido: "+self.apellido+" ci: "+self.ci)