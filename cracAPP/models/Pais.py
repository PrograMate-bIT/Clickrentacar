from django.db import models


class Pais(models.Model):
    id = models.IntegerField(primary_key=True)
    nombrePais = models.CharField(30)
