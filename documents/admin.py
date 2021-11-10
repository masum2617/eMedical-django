from django.contrib import admin
from .models import MedicalHistory, MedicalRecords, Prescription, Appointment
# Register your models here.

class MedicalHistoryAdmin(admin.ModelAdmin):

    list_display = ('patient','doctor', 'is_active', 'date_created')
    list_display_links = ('patient', 'doctor')



admin.site.register(MedicalHistory,MedicalHistoryAdmin)
admin.site.register(MedicalRecords)
admin.site.register(Prescription)
admin.site.register(Appointment)

