from django.contrib import admin
from .models import Doctor, DoctorSpecialization, Qualification,Experience, AppointmentTime,PatientAppointment
# Register your models here.




admin.site.register(Doctor)
admin.site.register(DoctorSpecialization)
admin.site.register(Qualification)
admin.site.register(Experience)
admin.site.register(AppointmentTime)
admin.site.register(PatientAppointment)