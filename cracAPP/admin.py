from django.contrib import admin
from .models.ciudad import Ciudad
from .models.cuentaAdministrador import Administrador
from .models.cuentaUsuario import Usuario
from .models.denegacion import Denegacion
from .models.licencia import Licencia
from .models.pais import Pais
from .models.perfilAlquila import PerfilAlquila
from .models.perfilRenta import PerfilRenta
from .models.registroAlquiler import RegistroAlquiler
from .models.solicitudAlquiler import SolicitudAlquiler
from .models.solicitudRegistro import SolicitudRegistro
from .models.vehiculo import Vehiculo
from .models.vehiculoPapeles import VehiculoPapeles

from .models.ciudad import Ciudad
from .models.cuentaAdministrador import Administrador
from .models.cuentaUsuario import Usuario
from .models.denegacion import Denegacion
from .models.licencia import Licencia
from .models.perfilAlquila import PerfilAlquila
from .models.perfilPropietario import PerfilPropietario
from .models.registroAlquiler import RegistroAlquiler
from .models.solicitudAlquiler import SolicitudAlquiler
from .models.solicitudRegistro import SolicitudRegistro
from .models.vehiculo import Vehiculo
from .models.vehiculoPapeles import VehiculoPapeles

# Register your models here.
admin.site.register(Ciudad)
admin.site.register(Administrador)
admin.site.register(Usuario)
admin.site.register(Denegacion)
admin.site.register(Licencia)
admin.site.register(PerfilAlquila)
admin.site.register(PerfilPropietario)
admin.site.register(RegistroAlquiler)
admin.site.register(SolicitudAlquiler)
admin.site.register(SolicitudRegistro)
admin.site.register(Vehiculo)
admin.site.register(VehiculoPapeles)
