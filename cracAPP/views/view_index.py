from django.shortcuts import render
from django.http import Http404
from ..models.cuentaUsuario import Usuario
from ..models.ciudad import Ciudad
from ..models.pais import Pais


def index(request):
    texto = "texto de prueba"
    dato = 123
    titulo = "Click Rent a Carrrr"

    pais = Pais(nombre='Uruguay')
    variable = Ciudad(nombre='Canelones', pais=pais)
    print(variable)

    return render(request, 'cracAPP/index.html', {'title': titulo,
                                                  'texto': texto,
                                                  'dato': dato,
                                                  'variable': str(variable),
                                                  })
