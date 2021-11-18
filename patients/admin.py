from django.contrib import admin
from .models import Patient,PrescriptionStatus 
# Register your models here.
admin.site.register(Patient)
admin.site.register(PrescriptionStatus)