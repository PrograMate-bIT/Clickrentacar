from django.db import models

class Ciudad(models.Model):
    URUGUAY = 'UY'
    ARGENTINA = 'AR'
    BRAZIL = 'BR'
    CHILE = 'CL'
    BOLIVIA = 'BO'
    COLOMBIA = 'CO'
    ECUADOR = 'EC'
    PARAGUAY = 'PY'
    PERU = 'PE'
    VENEZUELA = 'VE'
    PAIS_OPCIONES = [
        (URUGUAY, 'Uruguay'),
        (ARGENTINA, 'Argentina'),
        (BRAZIL, 'Brasil'),
        (CHILE, 'Chile'),
        (BOLIVIA, 'Bolivia'),
        (COLOMBIA, 'Colombia'),
        (ECUADOR, 'Ecuador'),
        (PARAGUAY, 'Paraguay'),
        (PERU, 'Perú'),
        (VENEZUELA, 'Venezuela')
    ]

    id = models.IntegerField(primary_key=True)
    ciudad = models.CharField(max_length=30, blank=False)
    pais = models.CharField(
        max_length=2,
        choices=PAIS_OPCIONES,
        default=URUGUAY
    )

    class Meta:
        unique_together = (("ciudad", "pais"),)

    def __str__(self):
        return self.ciudad + ", " + self.pais


class Usuario(models.Model):
    CASA = "Casa"
    APARTAMENTO = "Apartamento"
    VIVIENDA_OPCIONES = [
        (CASA, "Casa"),
        (APARTAMENTO, "Apartamento")
    ]


    ci = models.IntegerField(verbose_name="ci",primary_key=True, null=False, blank=False)
    # libretaConducir = models.OneToOneField('usuario.Licencia', related_name='Licencia', blank=True, on_delete=models.CASCADE)  # Este campo lo llena la aprobacion del admin
    nombreUsuario = models.CharField(verbose_name="nombre",unique=True, max_length=30, blank=False, null=False)
    contrasenia = models.CharField(verbose_name="contrasenia",max_length=30, blank=False, null=False)
    mail = models.EmailField(verbose_name="Mail",unique=True, max_length=50, blank=False, null=False)
    ciudad = models.ForeignKey(Ciudad, verbose_name="ciudad", blank=True, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name="nombre",max_length=30)
    apellido = models.CharField(verbose_name="apellido",max_length=30)
    telefono = models.IntegerField(verbose_name="telefono")
    fechaNacimiento = models.DateField(verbose_name="fechaNacimiento",blank=False)
    calle = models.CharField(verbose_name="calle",max_length=50, blank=False, null=True)
    esquina = models.CharField(verbose_name="equina",max_length=50, null=True)
    numDireccion = models.IntegerField(verbose_name="numDireccion",max_length=5, blank=False, null=True)
    tipoVivienda = VIVIENDA_OPCIONES
    bizz = models.IntegerField(verbose_name="bizz", null=True)
    antiguedad = models.DateField(verbose_name="antiguedad",auto_now_add=True, blank=False, null=True)

    class Meta:
        unique_together = ['ci']
        ordering = ['ci']

    def __str__(self):
        return self.nombreUsuario


class Licencia(models.Model):
    idLicencia = models.IntegerField(primary_key=True)
    usuario = models.OneToOneField(Usuario, blank=False, on_delete=models.CASCADE)
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
    restricciones = models.IntegerField(2)
    observaciones = models.CharField(max_length=15)

    def __str__(self):
        categorias = {'A': self.catA, 'B': self.catB, 'C': self.catC, 'D': self.catD, 'E': self.catE, 'F': self.catF,
                      'G1': self.catG1, 'G2': self.catG2, 'G3': self.catG3, 'H': self.catH}
        grupo = []
        for cat in categorias:
            if categorias[cat]:
                grupo.append(cat)

        return "Licencia: " + ', '.join(grupo)


class Administrador(models.Model):
    id = models.IntegerField(primary_key=True)
    nombreUsuario = models.CharField(default="", unique=True, max_length=30)
    contrasenia = models.CharField(default="", max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField(default="", unique=True, max_length=50)
    telefono = models.IntegerField(20)
    ciudad = models.ForeignKey(Ciudad, verbose_name="Ciudad", on_delete=models.CASCADE, null=True, blank=True)
    antiguedad = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Admin: " + self.nombreUsuario


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
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    usuarioSolicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nroSolicitud = models.IntegerField()  # este valor no es necesario, se usa la id
    estadoSolicitud = models.CharField(
        max_length=3,
        choices=ESTADO_OPCIONES,
        default=PENDIENTE,
    )
    fechaSolicitud = models.DateField()
    horaSolicitud = models.TimeField()
    aprobador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    fechaGestion = models.DateField()
    horaGestion = models.TimeField()
    comentarioAprobador = models.CharField(max_length=100)

    def __str__(self):
        return "Solicitud nº" + str(self.id) + " de " + str(self.usuarioSolicitante)


class Denegacion(models.Model):
    id = models.IntegerField(primary_key=True)
    ciSolicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    tipoDnegacion = models.TextChoices('Alquilar', 'Arrendar')
    comentarioDenegacion = models.CharField(max_length=100)
    administradorDenegador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    fechaDenegacion = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.tipoDnegacion + " denegado: " + self.comentarioDenegacion


class PerfilAlquila(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.OneToOneField(Usuario, blank=False, null=False, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(SolicitudRegistro, blank=False, null=False, on_delete=models.CASCADE)
    libreta = models.OneToOneField(Licencia, blank=False, null=False, on_delete=models.CASCADE)

    # NOTA: OneToOneField() es equivalente a ForeignKey(unique=True)

    def __str__(self):
        return "Perfil Alquila: " + str(self.id)


class PerfilPropietario(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.OneToOneField(Usuario, blank=False, null=False, on_delete=models.CASCADE)
    solicitud = models.ForeignKey(SolicitudRegistro, blank=False, null=False, on_delete=models.CASCADE)

    # vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    def __str__(self):
        return "Perfil Propietario: " + str(self.id)
