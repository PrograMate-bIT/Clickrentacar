from django.db import models


class Administrador(models.Model):
    id = models.IntegerField(primary_key=True)
    nombreUsuario = models.CharField(default="", unique=True, max_length=30)
    contrasenia = models.CharField(default="", max_length=30)
    telefono = models.IntegerField(10)
