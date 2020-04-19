from django.db import models

from registration.models import Profile, custom_upload_to


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    carRegistration = models.CharField(max_length=12, blank=False, unique=True)
    owner = models.ForeignKey(Profile, verbose_name="Propietario", blank=False, null=False, on_delete=models.CASCADE)
    brand = models.CharField(max_length=20, blank=False)
    carModel = models.CharField(max_length=15, blank=False)
    year = models.IntegerField(default=1900, blank=True)
    seatsNumber = models.IntegerField(2, blank=True)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['carRegistration']

class VechiclePublication(models.Model):
    id = models.IntegerField(primary_key=True)
    vehicle = models.OneToOneField(Vehicle, verbose_name="Vehiculo", blank=False, null=False, on_delete=models.CASCADE)
    price = models.IntegerField(blank=False, null=False)
    publisher = models.ForeignKey(Profile, verbose_name="Propietario", blank=False, null=False, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    carPhoto = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    published = models.BooleanField(default=True)
