from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("ESTE ES EL INDEX.")

def categorys(request, categoria_id):
    return HttpResponse("CATEGORIA: %s" % categoria_id)

def search(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")

def about(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")

def contact(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")

def userLogin(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")

def userPanel(request, usuario_id):
    return HttpResponse("ESTO ES UNA PRUEBA.")

def userRegister(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")

def userDocument(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")

def vehicleDocument(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")

def vehicleRent(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")

def vehiclePublish(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")

