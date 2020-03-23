from django.db import models

from . import cuentaUsuario, solicitudRegistro


class PerfilPropietario(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.OneToOneField(cuentaUsuario.Usuario, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(solicitudRegistro.SolicitudRegistro, blank=False, on_delete=models.CASCADE)

    # OneToOneField() es equivalente a ForeignKey(unique=True)

    def __str__(self):
        return "Perfil Propietario: " + str(self.id)
