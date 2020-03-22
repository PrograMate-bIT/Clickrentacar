from django.db import models

from . import cuentaUsuario, cuentaAdministrador


class Denegacion(models.Model):
    id = models.IntegerField(primary_key=True)
    ciSolicitante = models.ForeignKey(cuentaUsuario.Usuario, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(cuentaUsuario.ciudad.Ciudad, on_delete=models.CASCADE)
    tipoDnegacion = models.TextChoices('Alquilar', 'Arrendar')
    comentarioDenegacion = models.CharField(max_length=100)
    administradorDenegador = models.ForeignKey(cuentaAdministrador.Administrador, on_delete=models.CASCADE)
    fechaDenegacion = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.tipoDnegacion + " denegado: " + self.comentarioDenegacion
