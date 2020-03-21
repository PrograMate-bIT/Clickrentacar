from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def categorys(request):
    if request.method == 'GET':
        pass
        # do_something()
    elif request.method == 'POST':
        pass
        # do_something_else()

    return render(request, 'cracAPP/categorys.html')


def category_id(request, categoria_id):
    titulo = HttpRequest(category_id)
    # return HttpResponse("CATEGORIA: %s" % categoria_id)
    return render(request, 'cracAPP/categorys.html', {'title': titulo})
