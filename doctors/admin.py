from django.contrib import admin
from .models import Doctor, DoctorSpecialization, Qualification
# Register your models here.
admin.site.register(Doctor)
admin.site.register(DoctorSpecialization)
admin.site.register(Qualification)
