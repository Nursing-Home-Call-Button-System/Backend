from django.contrib import admin
from .models import Patient, CallRequest

# Register your models here.

admin.site.register(Patient)
admin.site.register(CallRequest)