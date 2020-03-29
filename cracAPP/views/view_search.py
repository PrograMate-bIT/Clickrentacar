from django.shortcuts import render


def search(request):
    return render(request, 'cracAPP/search.html')
