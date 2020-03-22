from django.db import models

from . import cuentaUsuario, licencia


class PerfilAlquila(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.OneToOneField(cuentaUsuario.Usuario, on_delete=models.CASCADE)
    libreta = models.OneToOneField(licencia.Licencia, on_delete=models.CASCADE)
