from django.db import models


class Vehiculo(models.Model):
    id = models.IntegerField(primary_key=True)
    marca = models.CharField(default="", max_length=15)
    anio = models.IntegerField(default=1900, max_length=4)