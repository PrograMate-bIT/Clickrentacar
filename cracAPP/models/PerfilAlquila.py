from django.db import models

from . import CuentaUsuario


class PerfilAlquila(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.ForeignKey(CuentaUsuario, on_delete=models.CASCADE)
