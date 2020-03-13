from django.db import models

from . import cuentaUsuario, cuentaAdministrador


class Denegacion(models.Model):
    id = models.IntegerField(primary_key=True)
    numeroSolicitud = models.IntegerField()
    ciSolicitante = models.ForeignKey(cuentaUsuario.Usuario, on_delete=models.CASCADE())
    pais = models.ForeignKey(cuentaUsuario.pais, on_delete=models.CASCADE())
    ciudad = models.ForeignKey(cuentaUsuario.ciudad, on_delete=models.CASCADE)
    tipoDnegacion = models.TextChoices('Alquilar', 'Rentar')
    comentarioDenegacion = models.CharField(max_length=100)
    administradorDenegador = models.ForeignKey(cuentaAdministrador.Administrador, on_delete=models.CASCADE())
