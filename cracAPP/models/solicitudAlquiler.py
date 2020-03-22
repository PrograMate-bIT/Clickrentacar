from django.db import models
from .cuentaUsuario import Usuario
from .vehiculo import Vehiculo


class SolicitudAlquiler(models.Model):
    id = models.IntegerField(primary_key=True)
    usarioSolicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fechaSolicitud = models.DateTimeField(auto_now_add=True, blank=True)  # fecha del pedido
    startDate = models.DateField(blank=True)  # checkout
    startTime = models.TimeField(blank=True)
    endDate = models.DateField(blank=True)  # checkin
    endTime = models.TimeField(blank=True)
