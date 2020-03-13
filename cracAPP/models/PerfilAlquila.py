from django.db import models

from . import cuentaUsuario, licencia


class PerfilAlquila(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.ForeignKey(cuentaUsuario.Usuario, on_delete=models.CASCADE)
    libreta = models.ForeignKey(licencia.Licencia, on_delete=models.CASCADE)