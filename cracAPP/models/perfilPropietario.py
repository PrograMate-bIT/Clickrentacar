from django.db import models

from . import cuentaUsuario, vehiculo


class PerfilPropietario(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.OneToOneField(cuentaUsuario.Usuario, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(vehiculo.Vehiculo, on_delete=models.CASCADE)
