from django.shortcuts import render
from ..models.ciudad import Ciudad


def index(request):
    texto = "texto de prueba"
    dato = 123
    titulo = "Click Rent a Carrrr"

    variable = Ciudad(ciudad='Canelones', pais='Uruguay')
    try:
        variable.save()  # Guarda ciudad en la DB
    except:
        print("--------------------------------------------")
        print("ya existe " + str(variable))
        print("--------------------------------------------")
    atributo = variable.ciudad
    atributo2 = variable.pais
    atributo3 = str(variable)

    return render(request, 'cracAPP/index.html', {'title': titulo,
                                                  'texto': texto,
                                                  'dato': dato,
                                                  'testPais': atributo,
                                                  'testPais2': atributo2,
                                                  'testPais3': atributo3,
                                                  })
