from django.db import models
from registration.models import Profile


class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    carRegistration = models.CharField(max_length=12, blank=False, unique=True)
    owner = models.ForeignKey(Profile, verbose_name="Propietario", blank=False, null=False, on_delete=models.CASCADE)
    brand = models.CharField(max_length=20, blank=False)
    carModel = models.CharField(max_length=15, blank=False)
    year = models.IntegerField(default=1900, blank=True)
    seatsNumber = models.IntegerField(2, blank=True)

    class Meta:
        ordering = ['carRegistration']
