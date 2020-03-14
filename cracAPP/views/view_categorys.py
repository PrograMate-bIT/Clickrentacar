from django.shortcuts import render
from django.http import HttpResponse


def categorys(request, categoria_id=''):
    if categoria_id == '':
        return render(request, 'cracAPP/categorys.html')
    return HttpResponse("CATEGORIA: %s" % categoria_id)
