from django.db import models


class SolicitudAlquiler(models.Model):
    idSolicitudAlquiler = models.IntegerField(primary_key=True)
