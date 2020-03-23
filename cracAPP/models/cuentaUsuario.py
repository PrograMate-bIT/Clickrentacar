from django.db import models
from . import ciudad


class Usuario(models.Model):
    CASA = "Casa"
    APARTAMENTO = "Apartamento"
    VIVIENDA_OPCIONES = [
        (CASA, "Casa"),
        (APARTAMENTO, "Apartamento")
    ]
    ci = models.IntegerField(primary_key=True)
    libretaConducir = models.OneToOneField('cracAPP.Licencia', related_name='Licencia', blank=True,
                                           on_delete=models.CASCADE)  # Este campo lo llena la aprobacion del admin
    nombreUsuario = models.CharField(unique=True, max_length=30, blank=False)
    contrasenia = models.CharField(max_length=30, blank=False)
    mail = models.EmailField(unique=True, max_length=50, blank=False)
    ciudad = models.ForeignKey(ciudad.Ciudad, blank=False, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, blank=False)
    apellido = models.CharField(max_length=30, blank=False)
    telefono = models.IntegerField(20, blank=False)
    fechaNacimiento = models.DateField(blank=False)
    calle = models.CharField(max_length=50, blank=False)
    esquina = models.CharField(max_length=50)
    numDireccion = models.IntegerField(4, blank=False)
    tipoVivienda = VIVIENDA_OPCIONES
    bizz = models.IntegerField(4)
    antiguedad = models.DateField(auto_now_add=True, blank=True)

    class Meta:
        unique_together = (("nombre", "apellido"),)

    def __str__(self):
        return self.nombreUsuario
