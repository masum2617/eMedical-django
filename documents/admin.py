from django.contrib import admin
from .models import MedicalHistory, MedicalRecords, Prescription, Review
# Register your models here.

class MedicalHistoryAdmin(admin.ModelAdmin):

    list_display = ('patient','doctor', 'is_active', 'date_created')
    list_display_links = ('patient', 'doctor')

class PrescriptionAdmin(admin.ModelAdmin):

    list_display = ('name','quantity', 'days', 'doctor', 'patient')
    list_display_links = ('name', 'patient', 'doctor')

admin.site.register(MedicalHistory,MedicalHistoryAdmin)
admin.site.register(MedicalRecords)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Review),
# admin.site.register(PatientAppointment)


