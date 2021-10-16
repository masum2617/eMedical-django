from django.db import models
from datetime import datetime
from django.db.models.deletion import CASCADE

from django.db.models.enums import Choices
from django.shortcuts import redirect


from users.models import Account
from multiselectfield import MultiSelectField
# Create your models here.
class Doctor(models.Model):
    city  = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='doctors/%Y/%m/%d/',default='default.png')
    gender = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)

    # getting the user
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.user.first_name


class DoctorSpecialization(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    specialized_category  = models.CharField(max_length=50, null=True)
    
    
    def __str__(self):
        return self.specialized_category


class Qualification(models.Model):
    institution_name  = models.CharField(max_length=50, null=True)
    qualification_degree = models.CharField(max_length=50, null=True)
    years_of_completion = models.DateField(null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.institution_name

class Experience(models.Model):
    hospital_name = models.CharField(max_length=50, null=True)
    worked_from = models.DateField(null=True)
    worked_to = models.DateField(null=True)
    designation = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.hospital_name

# class Appointment(models.Model):
#     appointment = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, null=True)
#     # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
#     # patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
#     appointment_time = models.CharField(max_length=30, null=True)
#     appointment_date = models.CharField(max_length=30, null=True)

#     def __str__(self):
#         return self.id


