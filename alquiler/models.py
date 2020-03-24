from django.db import models

from vehiculo.models import Vehiculo
from usuario.models import Usuario


# Create your models here.


class SolicitudAlquiler(models.Model):
    id = models.IntegerField(primary_key=True)
    usarioSolicitante = models.ForeignKey(Usuario, verbose_name="Usuario", blank=False, null=False,
                                          on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, verbose_name="Vehiculo", null=False, on_delete=models.CASCADE)
    fechaSolicitud = models.DateTimeField(auto_now_add=True, blank=True)  # fecha del pedido
    startDate = models.DateField(blank=True)  # checkout SOLICITADO
    startTime = models.TimeField(blank=True)
    endDate = models.DateField(blank=True)  # checkin SOLICITADO
    endTime = models.TimeField(blank=True)
    costoReserva = models.DecimalField(max_digits=6, decimal_places=2, blank=False)

    def __str__(self):
        return "Solicitud nº: " + str(self.id)


class RegistroAlquiler(models.Model):
    id = models.IntegerField(primary_key=True)
    solicitudAlquiler = models.ForeignKey(SolicitudAlquiler, verbose_name="Usuario", null=False,
                                          on_delete=models.CASCADE)  # RESERVA DE SOLICITUD
    startDate = models.DateTimeField(auto_now_add=False, blank=True)  # FECHAS ACORDADAS ENTRE CLIENTE Y PROPIETARIO
    endDate = models.DateTimeField(auto_now_add=False, blank=True)
    entregaDateReal = models.DateTimeField(auto_now_add=False, blank=True)  # FECHAS REALES de RETIRO Y DEVOLUCION
    devolucionDateReal = models.DateTimeField(auto_now_add=False, blank=False)
    costoPorHora = models.DecimalField(max_digits=6, decimal_places=2, blank=False)  # Dolares
    costoPorHoraRecargo = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, blank=True)
    # devueltoDate puede no ser ingresado (blank=False), para cuando un vehiculo aun no fue devuelto
    # La diferencia entre la fecha REAL de devolucion y la ACORDADA supone un recargo $$$ por hora a calcular

    observaciones = models.CharField(max_length=200, blank=True)

    # Habria que incorporar mas atributos en caso de accidente, hasta incluso una tabla

    def __str__(self):
        return "Alquiler nº: " + str(self.id)