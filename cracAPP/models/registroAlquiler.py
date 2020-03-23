from django.db import models

from .solicitudAlquiler import SolicitudAlquiler


class RegistroAlquiler(models.Model):
    id = models.IntegerField(primary_key=True)
    tramiteSolicitud = models.ForeignKey(SolicitudAlquiler, on_delete=models.CASCADE)
    startDate = models.DateTimeField(auto_now_add=False, blank=True)  # FECHAS ACORDADAS ENTRE CLIENTE Y PROPIETARIO
    endDate = models.DateTimeField(auto_now_add=False, blank=True)
    entregaDateReal = models.DateTimeField(auto_now_add=False, blank=True)  # FECHAS REALES de RETIRO Y DEVOLUCION
    devolucionDateReal = models.DateTimeField(auto_now_add=False, blank=False)
    costoPorHora = models.DecimalField(max_digits=6, decimal_places=2, blank=False)  # Dolares
    costoPorHoraRecargo = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, blank=True)
    # devueltoDate puede no ser ingresado (blank=False), para cuando un vehiculo aun no fue devuelto
    # La diferencia entre la fecha REAL de devolucion y la ACORDADA supone un recargo $$$ por hora a calcular

    observaciones = models.CharField(max_length=200, blank=True)
    # Habria que incorporar mas atributos en caso de accidente, e incluso una tabla

    def __str__(self):
        return "Alquiler nº: " + str(self.id)
