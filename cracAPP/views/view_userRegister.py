from django.shortcuts import render
from ..forms.createUser import CreateUser


def user_register(request):
    try:
        register_form = CreateUser()
    except Exception as error:
        register_form = 'ERROR EN EL FORM: ' + str(error)
    return render(request, 'cracAPP/userRegister.html', register_form)
