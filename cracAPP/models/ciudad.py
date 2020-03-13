from django.db import models

from . import pais


class Ciudad(models.Model):
    id = models.IntegerField(primary_key=True)
    pais = models.ForeignKey(pais.Pais, on_delete=models.CASCADE)
