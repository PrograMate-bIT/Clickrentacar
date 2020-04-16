from django.db import models
from registration.models import Profile
from vehicles.models import VechiclePublication


class Request(models.Model):
    idSol = models.IntegerField(primary_key=True)  # Solicitud
    userRequest = models.ForeignKey(Profile, verbose_name="ci", blank=False, null=False, on_delete=models.CASCADE)
    transportPublisher = models.ForeignKey(VechiclePublication, verbose_name="id", blank=False, null=False,
                                           on_delete=models.CASCADE)
    dateRequest = models.DateField(null=True, blank=True)  # fechadesolicitud
    timeRequest = models.TimeField(null=True, blank=True)  # horadesolicitud
    dateFrom = models.DateField(null=True, blank=True)  # fechaDesde
    dateTo = models.DateField(null=True, blank=True)  # fehasta
    timeTo = models.TimeField(null=True, blank=True)  # hora desde
    timeFrom = models.TimeField(null=True, blank=True)  # hora hasta
    Commentary = models.CharField(max_length=75, null=True, blank=True)  # comentarios en la solicitud
    State = models.CharField(max_length=1, default='S', null=True,
                             blank=True)  # estado de la solicitud C=confiormado S=solicitado C=Cancelado


class Confirmed(models.Model):
    id = models.IntegerField(primary_key=True)
    requestRent = models.OneToOneField(Request, on_delete=models.CASCADE)
    startDate = models.DateField(auto_now_add=False, blank=True, null=True, )  # FECHAS ACORDADAS ENTRE CLIENTE Y PROPIETARIO
    endDate = models.DateField(auto_now_add=False, blank=True, null=True)
    starTime = models.TimeField(auto_now_add=False, default='9.0.0.0', blank=True, null=True)
    endTime = models.TimeField(auto_now_add=False, default='9.0.0.0', blank=True, null=True)
    returnUserDate = models.DateField(auto_now_add=False, blank=True, null=True)  # FECHAS REALES de Devolución
    Commentary = models.CharField(max_length=75, null=True, blank=True) # comentarios del alquiler(lo rellena el usuario que alquila)
    priceHour = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)  # Dolares
    priceHourSurcharge = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, blank=True, null=True)  # precio por hora de recargo
    Qualification = models.IntegerField(default=1, blank=True, null=True)
    Observations = models.CharField(max_length=200, blank=True)  # Observaciones por parte del dueño del vehículo
    # devueltoDate puede no ser ingresado (blank=False), para cuando un vehiculo aun no fue devuelto
    # La diferencia entre la fecha REAL de devolucion y la ACORDADA supone un recargo $$$ por hora a calcular

    # Habria que incorporar mas atributos en caso de accidente, hasta incluso una tabla
