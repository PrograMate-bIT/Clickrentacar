from django.shortcuts import render
#from ..forms.createUser import CreateUser <- createUser.py tiene errores


def user_register(request):
    #create_form = CreateUser()
    #return render(request, 'cracAPP/userRegister.html', create_form)
    return render(request, 'cracAPP/userRegister.html')
