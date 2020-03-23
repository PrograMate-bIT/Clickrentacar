from django.db import models
from vehiculo.models import Vehiculo
from usuario.models import Usuario

# Create your models here.

class SolicitudAlquiler(models.Model):
    id = models.IntegerField(primary_key=True)
    usuarioSolicitante = models.ForeignKey(Usuario, verbose_name="Usuario", on_delete=models.CASCADE, null=True, blank=True)
    vehiculo = models.ForeignKey(Vehiculo, verbose_name="Vehiculo", on_delete=models.CASCADE, null=True, blank=True)
    fechaSolicitud = models.DateTimeField(auto_now_add=True, blank=True)  # fecha del pedido
    startDate = models.DateField(blank=True)  # checkout
    startTime = models.TimeField(blank=True)
    endDate = models.DateField(blank=True)  # checkin
    endTime = models.TimeField(blank=True)

    def __str__(self):
        return "Usuario solicitante: " + self.usuarioSolicitante + ", Vehiculo solicitado: " + self.vehiculo

class RegistroAlquiler(models.Model):
    id = models.IntegerField(primary_key=True)
    fechaEmision = models.DateField()
    fechaDevolucion = models.DateField()
    solicitudAlquiler = models.ForeignKey(SolicitudAlquiler, verbose_name="SolicitudAlquiler", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Alquiler correspondiente a la solicitud N "+ self.solicitudAlquiler