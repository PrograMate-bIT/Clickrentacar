from django.db import models

from . import vehiculo


class VehiculoPapeles(models.Model):
    id = models.IntegerField(primary_key=True)
    vehiculo = models.ForeignKey(vehiculo.Vehiculo, on_delete=models.CASCADE)
