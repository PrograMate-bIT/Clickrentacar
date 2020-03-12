from django.db import models

#from . import perfilAlquila


class Licencia(models.Model):
    idLicencia = models.IntegerField(primary_key=True)
    #conductor = models.ForeignKey(perfilAlquila.PerfilAlquila, on_delete=models.CASCADE())
