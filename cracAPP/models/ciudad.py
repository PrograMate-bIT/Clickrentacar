from django.db import models

from . import pais


class Ciudad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    pais = models.ForeignKey(pais.Pais, on_delete=models.CASCADE)  # Este atributo es de tipo model! (Todos los FK)

    def __str__(self):
        return str(self.nombre) + ", " + str(self.pais)  # Acá le pasa el __str__() del model Pais

    def __repr__(self):
        return {'id': self.id, 'ciudad': self.nombrePais, 'pais': self.pais}
