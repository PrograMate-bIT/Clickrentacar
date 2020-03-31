from django.shortcuts import render
from django.urls import reverse_lazy
from django import forms
from django.views.generic import CreateView
from usuario.models import Ciudad
from .forms import createUser


class UserRegister(CreateView):
    form_class = createUser
    template_name = 'cracAPP/userRegister.html'
    reverse_lazy = '/registro'

    def get_success_url(self):

        return reverse_lazy(UserRegister)

    def get_form(self, form_class=None):
        form = super(UserRegister, self).get_form()

        return form


def user_register(request):
    try:
        register_form = UserRegister.get_form()
        text = 'anda'
        return render(request, 'cracAPP/userRegister.html', {'register_form': register_form, 'mensaje': text})
    except Exception as error:
        register_form = 'ERROR EN EL FORM: ' + str(error)
        text = 'no anda'
    return render(request, 'cracAPP/userRegister.html', {'register_form': register_form, 'mensaje': text})

# def user_login(request):
# try:
#    login_form = Login()
#    return render(request, 'cracAPP/userLogin.html', login_form)
# except Exception as error:
#    login_form = 'ERROR EN EL FORM: ' + str(error)
# return render(request, 'cracAPP/userLogin.html', login_form)
