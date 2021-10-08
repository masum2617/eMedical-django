from django.contrib import admin
from .models import MedicalHistory, MedicalRecords, Prescription
# Register your models here.
admin.site.register(MedicalHistory)
admin.site.register(MedicalRecords)
admin.site.register(Prescription)
