from django.db import models

from . import ciudad


class Administrador(models.Model):
    id = models.IntegerField(primary_key=True)
    nombreUsuario = models.CharField(unique=True, max_length=30, blank=False)
    contrasenia = models.CharField(max_length=30, blank=False)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    mail = models.EmailField(unique=True, max_length=50, blank=False)
    telefono = models.IntegerField(20)
    ciudad = models.ForeignKey(ciudad.Ciudad, on_delete=models.CASCADE)
    antiguedad = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.nombreUsuario
