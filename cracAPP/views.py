from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("ESTE ES EL INDEX.")


def prueba(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")
