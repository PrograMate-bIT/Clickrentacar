from django.db import models

from . import solicitudRegistro, cuentaUsuario, cuentaAdministrador


class Denegacion(models.Model):
    id = models.IntegerField(primary_key=True)
    solicitudDenegada = models.OneToOneField(solicitudRegistro.SolicitudRegistro, related_name='Solicitud',
                                             on_delete=models.CASCADE)
    usuarioSolicitante = models.ForeignKey(cuentaUsuario.Usuario, related_name='Solicitante', on_delete=models.CASCADE)
    tipoDenegacion = models.TextChoices('Alquilar', 'Poropietario')
    adminDenegador = models.ForeignKey(cuentaAdministrador.Administrador, related_name='Administrador',
                                       on_delete=models.CASCADE)
    comentarioDenegacion = models.CharField(max_length=100, blank=False)
    fechaDenegacion = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Perfil " + self.tipoDnegacion + " denegado: " + self.comentarioDenegacion
