from django.shortcuts import render


def vehicle_document(request):
    return render(request, 'cracAPP/vehicleDocument.html')
