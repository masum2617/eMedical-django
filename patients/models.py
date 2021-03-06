from django.db import models
# from doctors.models import Doctor
from users.models import Account
from datetime import datetime

# Create your models here.
class Patient(models.Model):
    profile_image = models.ImageField(upload_to='patients/%Y/%m/%d/', default='default.png')
    city  = models.CharField(max_length=100, null=True)
    state  = models.CharField(max_length=100, null=True)
    country  = models.CharField(max_length=100, null=True)
    gender  = models.CharField(max_length=50, null=True)
    blood_group  = models.CharField(max_length=50, null=True)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    date_of_birth = models.DateField(null=True)
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.user.first_name

class PrescriptionStatus(models.Model):
    is_uploaded= models.BooleanField(default=False)
    doctor = models.ForeignKey("doctors.Doctor", on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)

    def __int__(self):
        return self.id

    
