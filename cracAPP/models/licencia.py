from django.db import models
from datetime import date

from . import cuentaUsuario


class Licencia(models.Model):
    idLicencia = models.IntegerField(primary_key=True)
    catA = models.BooleanField(default=False)
    catB = models.BooleanField(default=False)
    catC = models.BooleanField(default=False)
    catD = models.BooleanField(default=False)
    catE = models.BooleanField(default=False)
    catF = models.BooleanField(default=False)
    catG1 = models.BooleanField(default=False)
    catG2 = models.BooleanField(default=False)
    catG3 = models.BooleanField(default=False)
    catH = models.BooleanField(default=False)
    vencimiento = models.DateField(default=date.today())
    cantPasajeros = models.IntegerField(2)
    restricciones = models.IntegerField(2)
    observaciones = models.CharField(max_length=15)
