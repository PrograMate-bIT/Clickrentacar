from django.shortcuts import render


def vehicle_publish(request):
    return render(request, 'vehiclePublish.html')
