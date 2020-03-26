from django.shortcuts import render
from usuario.models import Ciudad


def index(request):
    # TODO ESTO ES UNA PRUEBA
    texto = "texto de prueba"
    dato = 123
    titulo = "Click Rent a Carrrr"

    try:
        variable = Ciudad(ciudad='Canelones', pais='Uruguay')
        try:
            variable.save()  # Guarda ciudad en la DB
        except:
            print("--------------------------------------------")
            print("ya existe " + str(variable)) + "en la db."
            print("--------------------------------------------")
    except Exception as e:
        print(str(e))
        variable = "variable error"
    try:
        atributo = variable.ciudad
    except:
        atributo = "atributo no anda"
    try:
        atributo2 = variable.pais
    except:
        atributo2 = "atributo2 no anda"
    try:
        atributo3 = str(variable)
    except:
        atributo3 = "atributo3 no anda"

    return render(request, 'cracAPP/index.html', {'title': titulo,
                                                  'texto': texto,
                                                  'dato': dato,
                                                  'testPais': atributo,
                                                  'testPais2': atributo2,
                                                  'testPais3': atributo3,
                                                  })
