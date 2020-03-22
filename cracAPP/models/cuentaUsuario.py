from django.db import models
from . import ciudad, licencia


class Usuario(models.Model):
    CASA = "Casa"
    APARTAMENTO = "Apartamento"
    VIVIENDA_OPCIONES = [
        (CASA, "Casa"),
        (APARTAMENTO, "Apartamento")
    ]
    ci = models.IntegerField(primary_key=True)
    nombreUsuario = models.CharField(default="", unique=True, max_length=30)
    contrasenia = models.CharField(default="", max_length=30)
    mail = models.EmailField(default="", unique=True, max_length=50)
    ciudad = models.ForeignKey(ciudad.Ciudad, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField(20)
    fechaNacimiento = models.DateField(blank=False)
    libretaConducir = models.OneToOneField('cracAPP.Usuario', blank=True, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50)
    esquina = models.CharField(max_length=50)
    numDireccion = models.IntegerField(4)
    tipoVivienda = VIVIENDA_OPCIONES
    bizz = models.IntegerField(4)
    antiguedad = models.DateField(auto_now_add=True, blank=True)

    class Meta:
        unique_together = (("nombre", "apellido"),)

    def __str__(self):
        return self.nombreUsuario
