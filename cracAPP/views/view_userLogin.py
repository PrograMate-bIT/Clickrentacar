from django.shortcuts import render
from ..forms.loginVista import Login


def user_login(request):
    try:
        login_form = Login()
        return render(request, 'cracAPP/userLogin.html', login_form)
    except Exception as error:
        login_form = 'ERROR EN EL FORM: ' + str(error)
    return render(request, 'cracAPP/userLogin.html', login_form)
