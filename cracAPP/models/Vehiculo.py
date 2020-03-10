from django.db import models


class Vehiculo(models.Model):
    idVehiculo = models.IntegerField(primary_key=True)
