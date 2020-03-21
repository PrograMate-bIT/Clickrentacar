from django.shortcuts import render
from django.http import Http404
from ..models.cuentaUsuario import Usuario


def index(request):
    texto = "texto de prueba"
    dato = 123
    titulo = "Click Rent a Carrrr"
    return render(request, 'cracAPP/index.html', {'title': titulo,
                                                  'texto': texto,
                                                  'dato': dato,
                                                  })
