from django.shortcuts import render


def user_document(request):
    return render(request, 'cracAPP/userDocument.html')
