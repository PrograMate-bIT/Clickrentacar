from django.db import models

from . import ciudad


class Administrador(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(default="", unique=True, max_length=30)
    contrasenia = models.CharField(default="", max_length=30)
    mail = models.EmailField(default="", unique=True, max_length=50)
    telefono = models.IntegerField(15)
    ciudad = models.ForeignKey(ciudad.Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre + "")

    def __repr__(self):
        return {'id': self.id, 'nombre': self.nombrePais}
