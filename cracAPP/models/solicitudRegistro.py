from django.db import models

from . import cuentaUsuario, cuentaAdministrador


class SolicitudRegistro(models.Model):
    PENDIENTE = 'PEN'
    APROBADA = 'APR'
    DENEGADA = 'DEN'
    ESTADO_OPCIONES = [
        (PENDIENTE, 'Pendiente'),
        (APROBADA, 'Aprobada'),
        (DENEGADA, 'Denegada'),
    ]

    id = models.IntegerField(primary_key=True)
    usuarioSolicitante = models.ForeignKey(cuentaUsuario.Usuario, on_delete=models.CASCADE)
    funcionSolicitada = models.TextChoices('Alquilar', 'Poropietario')
    estadoSolicitud = models.CharField(
        max_length=3,
        choices=ESTADO_OPCIONES,
        default=PENDIENTE,
    )
    fechaSolicitud = models.DateField(auto_now_add=True, blank=True)
    horaSolicitud = models.TimeField(auto_now_add=True, blank=True)
    aprobador = models.ForeignKey(cuentaAdministrador.Administrador, on_delete=models.CASCADE)
    fechaGestion = models.DateField(auto_now_add=False, blank=True)
    horaGestion = models.TimeField(auto_now_add=False, blank=True)
    comentarioAprobador = models.CharField(max_length=100, null=False)

    def __str__(self):
        return "Solicitud" + self.funcionSolicitada + ": " + self.estadoSolicitud
