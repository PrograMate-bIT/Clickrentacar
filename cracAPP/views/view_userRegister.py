from django.shortcuts import render


def user_register(request):
    return render(request, 'cracAPP/userRegister.html')
