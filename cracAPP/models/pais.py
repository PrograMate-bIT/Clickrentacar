from django.db import models


class Pais(models.Model):
    URUGUAY = 'UY'
    ARGENTINA = 'AR'
    BRAZIL = 'BR'
    CHILE = 'CL'
    BOLIVIA = 'BO'
    COLOMBIA = 'CO'
    ECUADOR = 'EC'
    PARAGUAY = 'PY'
    PERU = 'PE'
    VENEZUELA = 'VE'
    PAIS_OPCIONES = [
        (URUGUAY, 'Uruguay'),
        (ARGENTINA, 'Argentina'),
        (BRAZIL, 'Brasil'),
        (CHILE, 'Chile'),
        (BOLIVIA, 'Bolivia'),
        (COLOMBIA, 'Colombia'),
        (ECUADOR, 'Ecuador'),
        (PARAGUAY, 'Paraguay'),
        (PERU, 'Perú'),
        (VENEZUELA, 'Venezuela')
    ]

    id = models.IntegerField(primary_key=True)
    nombrePais = models.CharField(
        max_length=2,
        choices=PAIS_OPCIONES,
        default=URUGUAY,
    )
