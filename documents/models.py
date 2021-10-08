from datetime import datetime
from django.db import models
from doctors.models import Doctor
from patients.models import Patient
# Create your models here.
class Prescription(models.Model):
    prescription_file = models.FileField(upload_to='prescription/%Y/% m/% d/')
    
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    uploaded_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.patient.user.first_name

class MedicalRecords(models.Model):
    medical_insurance =  models.FileField(upload_to='insurance/%Y/% m/% d/')
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name_plural = "MedicalRecords"

    def __str__(self):
        return self.patient.user.first_name


class MedicalHistory(models.Model):
    reason =  models.TextField(blank=True)
    ever_had = models.TextField(blank=True)
    height = models.CharField(max_length=20, null=True)
    weight = models.CharField(max_length=20, null=True)
    age = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=20, null=True)
    previous_operation = models.TextField(blank=True)
    current_medication = models.TextField(blank=True)
    other_illness = models.TextField(blank=True)
    other_information = models.TextField(blank=True)

    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name_plural = "MedicalHistories"

    def __str__(self):
        return self.patient.user.first_name
