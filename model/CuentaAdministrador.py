from django.db import models

class Administrador(models.Model):
    id = models.IntegerField(primary_key=True)
    telefono = models.IntegerField(10)