from django.contrib import admin
from alquiler.models import SolicitudAlquiler
from alquiler.models import RegistroAlquiler

admin.site.register(SolicitudAlquiler)
admin.site.register(RegistroAlquiler)