from django.db import models

from . import pais


class Ciudad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    pais = models.ForeignKey(pais.Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ", " + self.pais

    def __repr__(self):
        return {'id': self.id, 'ciudad': self.nombrePais, 'pais': self.pais}
