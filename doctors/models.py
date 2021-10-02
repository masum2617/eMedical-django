from django.db import models
from datetime import datetime

from django.db.models.enums import Choices
from users.models import Account
from multiselectfield import MultiSelectField
# Create your models here.
class Doctor(models.Model):
    city  = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='photos/doctors', blank=True)
    gender = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)

    # getting the user
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.user.first_name


class DoctorSpecialization(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    specialized_category  = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.specialized_category


class Qualification(models.Model):
    institution_name  = models.CharField(max_length=50, null=True)
    qualification_degree = models.CharField(max_length=50, null=True)
    years_of_completion = models.DateField(null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.institution_name


