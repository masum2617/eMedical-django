from django.db import models
from users.models import Account
from datetime import datetime

# Create your models here.
class Patient(models.Model):
    profile_image = models.ImageField(upload_to='photos/patients', blank=True)
    city  = models.CharField(max_length=100, null=True)
    gender  = models.CharField(max_length=50, null=True)
    blood_group  = models.CharField(max_length=50, null=True)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)

    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.user.first_name