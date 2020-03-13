from django.db import models


class SolicitudAlquiler(models.Model):
    id = models.IntegerField(primary_key=True)
