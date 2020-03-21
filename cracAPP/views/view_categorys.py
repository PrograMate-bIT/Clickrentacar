from django.shortcuts import render
from django.http import HttpResponse


def categorys(request, categoria_id=None):
    return render(request, 'cracAPP/categorys.html')

def category_id(request, categoria_id=None):
    return HttpResponse("CATEGORIA: %s" % categoria_id)
