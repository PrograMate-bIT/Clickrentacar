from django.db import models

from . import CuentaUsuario, CuentaAdministrador, Pais, Ciudad


class SolicitudRegistro(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE())
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    ciSolicitante = models.ForeignKey(CuentaUsuario, on_delete=models.CASCADE())
    nroSolicitud = models.IntegerField()
    estadoSolicitud = models.TextChoices('Pendiente', 'Aprobada', 'Denegada')
    fechaSolicitud = models.DateField()
    horaSolicitud = models.TimeField()
    aprobador = models.ForeignKey(CuentaAdministrador, on_delete=models.CASCADE())
    fechaGestion = models.DateField()
    horaGestion = models.TimeField()
    comentarioAprobador = models.CharField(max_length=100)
