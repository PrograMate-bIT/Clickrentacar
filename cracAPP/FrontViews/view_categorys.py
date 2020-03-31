from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def categorys(request, **kwargs):
    entrada = kwargs.get('categoria_id', "default_value")
    if entrada == 'default_value':
        return render(request, 'cracAPP/categorys.html')
    return HttpResponse("CATEGORIA: %s" % kwargs.get('categoria_id', "default_value"))
    # return HttpResponse("CATEGORIA: %s" % categoria_id)
