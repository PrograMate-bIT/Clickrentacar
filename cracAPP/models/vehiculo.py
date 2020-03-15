from django.db import models


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

