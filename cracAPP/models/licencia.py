from django.db import models


class Licencia(models.Model):
    idLicencia = models.IntegerField(primary_key=True)
    usuario = models.OneToOneField('cracAPP.Usuario', related_name='Titular', blank=False, on_delete=models.CASCADE)
    catA = models.BooleanField(default=False)
    catB = models.BooleanField(default=False)
    catC = models.BooleanField(default=False)
    catD = models.BooleanField(default=False)
    catE = models.BooleanField(default=False)
    catF = models.BooleanField(default=False)
    catG1 = models.BooleanField(default=False)
    catG2 = models.BooleanField(default=False)
    catG3 = models.BooleanField(default=False)
    catH = models.BooleanField(default=False)
    vencimiento = models.DateField(blank=False)
    restricciones = models.IntegerField(2, blank=True)
    observaciones = models.CharField(max_length=15, blank=True)

    def __str__(self):
        categorias = {'A': self.catA, 'B': self.catB, 'C': self.catC, 'D': self.catD, 'E': self.catE, 'F': self.catF,
                      'G1': self.catG1, 'G2': self.catG2, 'G3': self.catG3, 'H': self.catH}
        grupo = []
        for cat in categorias:
            if categorias[cat]:
                grupo.append(cat)

        return "Licencia: " + ', '.join(grupo)
