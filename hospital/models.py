from django.db import models
from users.models import Account
from doctors.models import Doctor
from patients.models import Patient
# Create your models here.
class Hospital(models.Model):
    hospital_name  = models.CharField(max_length=50, null=True)
    hospital_address  = models.CharField(max_length=100, null=True)
    hospital_country  = models.CharField(max_length=50, null=True)
    hospital_city  = models.CharField(max_length=50, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.hospital_name

class Appointment(models.Model):
    appointment_date  = models.DateField(null=True)
    appointment_status  = models.BooleanField(default='inactive')
    booking_date  = models.DateField(null=True)
    followup_date  = models.DateField(null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.patient.user.first_name