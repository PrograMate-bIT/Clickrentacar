from django.db import models

from . import CuentaUsuario, CuentaAdministrador, Pais, Ciudad


class Denegacion(models.Model):
    id = models.IntegerField(primary_key=True)
    numeroSolicitud = models.IntegerField()
    ciSolicitante = models.ForeignKey(CuentaUsuario, on_delete=models.CASCADE())
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE())
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    tipoDnegacion = models.TextChoices('Alquilar', 'Rentar')
    comentarioDenegacion = models.CharField(max_length=100)
    administradorDenegador = models.ForeignKey(CuentaAdministrador, on_delete=models.CASCADE())
