from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ciudad.Ciudad)
admin.site.register(cuenta.Cuenta)
admin.site.register(cuentaAdministrador.Administrador)
admin.site.register(cuentaUsuario.Usuario)
admin.site.register(denegacion.Denegacion)
admin.site.register(licencia.Licencia)
admin.site.register(pais.Pais)
admin.site.register(perfilAlquila.PerfilAlquila)
admin.site.register(perfilRenta.PerfilRenta)
admin.site.register(registroAlquiler.RegistroAlquiler)
admin.site.register(solicitudAlquiler.SolicitudAlquiler)
admin.site.register(solicitudRegistro.SolicitudRegistro)
admin.site.register(vehiculo.Vehiculo)
admin.site.register(vehiculoPapeles.VehiculoPapeles)
