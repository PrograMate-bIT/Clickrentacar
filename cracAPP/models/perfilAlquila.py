from django.db import models

from . import cuentaUsuario, licencia, solicitudRegistro


class PerfilAlquila(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.OneToOneField(cuentaUsuario.Usuario, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(solicitudRegistro.SolicitudRegistro, on_delete=models.CASCADE)
    libreta = models.OneToOneField(licencia.Licencia, on_delete=models.CASCADE)

    # OneToOneField() es equivalente a ForeignKey(unique=True)

    def __str__(self):
        return "Perfil Alquila: " + str(self.id)
