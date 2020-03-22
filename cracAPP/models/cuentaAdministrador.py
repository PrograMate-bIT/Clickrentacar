from django.db import models

from . import ciudad


class Administrador(models.Model):
    id = models.IntegerField(primary_key=True)
    nombreUsuario = models.CharField(default="", unique=True, max_length=30)
    contrasenia = models.CharField(default="", max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField(default="", unique=True, max_length=50)
    telefono = models.IntegerField(20)
    ciudad = models.ForeignKey(ciudad.Ciudad, on_delete=models.CASCADE)
    antiguedad = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.nombreUsuario
