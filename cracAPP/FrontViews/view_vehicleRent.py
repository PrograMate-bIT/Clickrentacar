from django.shortcuts import render


def vehicle_rent(request):
    return render(request, 'vehicleRent.html')
