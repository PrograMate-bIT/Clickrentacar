from django.db import models
from .cuentaUsuario import Usuario
from .vehiculo import Vehiculo
from datetime import date


class SolicitudAlquiler(models.Model):
    id = models.IntegerField(primary_key=True)
    usarioSolicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fechaSolicitud = models.DateTimeField()  # fecha del pedido
    startDate = models.DateField()  # checkout
    startTime = models.TimeField()
    endDate = models.DateField()  # checkin
    endTime = models.TimeField()
