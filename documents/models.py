from datetime import datetime
from django.db import models
from doctors.models import Doctor
from patients.models import Patient
# Create your models here.

class MedicalRecords(models.Model):
    medical_insurance =  models.FileField(upload_to='insurance/%Y/% m/% d/')
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name_plural = "MedicalRecords"

    def __str__(self):
        return self.patient.user.first_name


class MedicalHistory(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    reason =  models.CharField(max_length=200, blank=True)
    ever_had = models.CharField(max_length=200,blank=True)
    
    weight = models.CharField(max_length=20, null=True)
    age = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=20, null=True)
    blood_group  = models.CharField(max_length=50, null=True)
    previous_operation = models.CharField(max_length=200,blank=True)
    current_medication = models.CharField(max_length=200,blank=True)
    other_illness = models.CharField(max_length=200,blank=True)
    other_information = models.CharField(max_length=200,blank=True)
    is_processing = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "MedicalHistories"

    # def __str__(self):
    #     return self.id

    # def __str__(self):
    #     if self.doctor:
    #         return f"For Dr. {self.doctor}"
    #     else:
    #         return f"History from {self.patient.user.first_name}"




class Prescription(models.Model):
    name =  models.CharField(max_length=50, null=True)
    quantity  = models.CharField(max_length=50, null=True)
    days = models.CharField(max_length=50, null=True)
    morning = models.CharField(max_length=10, null=True)
    afternoon = models.CharField(max_length=10, null=True)
    evening = models.CharField(max_length=10, null=True)
    night = models.CharField(max_length=10, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    uploaded_date = models.DateTimeField(default=datetime.now, blank=True)
    

    # def __str__(self):
    #     return self.name

class Review(models.Model):
    title = models.CharField(max_length=100, null=True)
    review = models.TextField(max_length=200, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING, null=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
