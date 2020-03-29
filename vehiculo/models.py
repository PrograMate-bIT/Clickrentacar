from django.db import models

from usuario.models import PerfilPropietario


# Create your models here.

class Vehiculo(models.Model):
    AUTO = 'auto'
    CAMIONETA = 'camioneta'
    CAMION = 'camion'
    MOTO = 'moto'

    CATEGORIA_OPCIONES = [
        (AUTO, 'Auto'),
        (CAMIONETA, 'Camioneta'),
        (CAMION, 'Camion'),
        (MOTO, 'Moto'),
    ]

    id = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=12, blank=False, unique=True)
    propietario = models.ForeignKey(PerfilPropietario, verbose_name="Propietario", blank=False, null=False,
                                    on_delete=models.CASCADE)
    marca = models.CharField(max_length=20, blank=False)
    modelo = models.CharField(max_length=15, blank=False)
    anio = models.IntegerField(default=1900, blank=True)
    asientos = models.IntegerField(2, blank=True)
    puertas = models.IntegerField(2, blank=True)
    categoria = models.CharField(
        max_length=15,
        choices=CATEGORIA_OPCIONES,
        default=AUTO,
    )

    def __str__(self):
        return self.categoria + ": " + self.matricula + ", " + self.marca + ", " + self.modelo


class VehiculoPapeles(models.Model):
    id = models.AutoField(primary_key=True)
    vehiculo = models.ForeignKey(Vehiculo, verbose_name="Vehiculo", blank=False, null=False, on_delete=models.CASCADE)
    documentacion = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return "Documentacion: " + self.documentacion
