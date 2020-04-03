from django.shortcuts import render
from usuario.models import Ciudad


def index(request):
    # TODO ESTO ES UNA PRUEBA
    titulo = "Click Rent a Carrrr"
    dato = 1024 + 1024
    texto = "texto de prueba"
    atributo1 = ''
    atributo2 = ''
    atributo3 = ''

    try:
        nueva_ciudad = Ciudad(ciudad='Paysandú', pais='Uruguay')
        texto = "Intentando guardar ciudades en la DB"
        atributo1 = "String de la clase: " + str(nueva_ciudad)
        atributo2 = "Pais: " + nueva_ciudad.pais
        atributo3 = "Ciudad: " + nueva_ciudad.ciudad
        try:
            nueva_ciudad.save()  # Guarda ciudad en la DB
            texto = "Se guardaró [" + str(nueva_ciudad) + "] en la tabla Ciudades"
        except:
            texto = "No se guradó [" + str(nueva_ciudad) + "], ya existe en la db."
    except Exception as error:
        texto = "ERROR EN INDEX.PY" + str(error)

    return render(request, 'cracAPP/index.html', {'title': titulo,
                                                  'texto': texto,
                                                  'dato': dato,
                                                  'testPais': atributo1,
                                                  'testPais2': atributo2,
                                                  'testPais3': atributo3,
                                                  })
