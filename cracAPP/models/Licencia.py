from django.db import models

from . import cuentaUsuario


class Licencia(models.Model):
    idLicencia = models.IntegerField(primary_key=True)
    conductor = models.ForeignKey(cuentaUsuario.Usuario, on_delete=models.CASCADE)
