from django.db import models

from . import cuentaUsuario


class PerfilRenta(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.ForeignKey(cuentaUsuario.Usuario, on_delete=models.CASCADE)