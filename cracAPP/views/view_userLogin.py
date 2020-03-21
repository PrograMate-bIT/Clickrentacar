from django.shortcuts import render
from ..forms.loginVista import Login


def user_login(request):
    login_form = Login()
    return render(request, 'cracAPP/userLogin.html', login_form)
