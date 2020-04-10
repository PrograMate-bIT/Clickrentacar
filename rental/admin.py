from django.contrib import admin
from .models import Request, Confirmed

# Register your models here.
admin.site.register(Request)
admin.site.register(Confirmed)
