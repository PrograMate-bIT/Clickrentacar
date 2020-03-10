from django.db import models

from . import Pais


class Ciudad(models.Model):
    id = models.IntegerField(primary_key=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
