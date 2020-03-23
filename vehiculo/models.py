from django.db import models

# Create your models here.
from usuario.models import PerfilPropietario


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

    id = models.IntegerField(primary_key=True)
    marca = models.CharField(default="", max_length=15)
    anio = models.IntegerField(default=1900)
    categoria = models.CharField(
        max_length=15,
        choices=CATEGORIA_OPCIONES,
        default=AUTO,
    )
    propietario = models.ForeignKey(PerfilPropietario, verbose_name="Perfil Propietario", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Vehiculo: "+ self.id +  ", Dueño: " + self.propietario

class VehiculoPapeles(models.Model):
    id = models.IntegerField(primary_key=True)
    vehiculo = models.ForeignKey(Vehiculo, verbose_name="Vehiculo", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Vehiculo asociado: "+ self.vehiculo