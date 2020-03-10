from django.db import models

from . import PerfilRenta


class Licencia(models.Model):
    idLicencia = models.IntegerField(primary_key=True)
    conductor = models.ForeignKey(PerfilRenta, on_delete=models.CASCADE())
