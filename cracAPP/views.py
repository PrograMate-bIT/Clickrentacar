from django.shortcuts import render
from django.http import HttpResponse
from .forms.loginVista import Login

# Create your views here.


def index(request):
    return HttpResponse("ESTE ES EL INDEX.")

def prueba(request):
    return HttpResponse("ESTO ES UNA PRUEBA.")

def login(request):
    login_form = Login()
    render(request, "login.html", login_form)

def createUser(request):
    create_form = CreateUser()
    render(request, "create_user.html", create_form)
