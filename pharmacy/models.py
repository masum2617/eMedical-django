from django.db import models

# Create your models here.
class Cardiovascular(models.Model):
    drug_category  = models.CharField(max_length=100, null=True)
    condition = models.CharField(max_length=100, null=True)
    drug_name = models.CharField(max_length=100, null=True)
    drug_image = models.ImageField(upload_to='drugs/%Y/%m/%d/',default='drug_default.jpg')

    def __str__(self):
        return self.drug_name

class Respiratory(models.Model):
    drug_category  = models.CharField(max_length=100, null=True)
    condition = models.CharField(max_length=100, null=True)
    drug_name = models.CharField(max_length=100, null=True)
    drug_image = models.ImageField(upload_to='drugs/%Y/%m/%d/',default='drug_default.jpg')

    def __str__(self):
        return self.drug_name

class Gastrointestinal(models.Model):
    drug_category  = models.CharField(max_length=100, null=True)
    condition = models.CharField(max_length=100, null=True)
    drug_name = models.CharField(max_length=100, null=True)
    drug_image = models.ImageField(upload_to='drugs/%Y/%m/%d/',default='drug_default.jpg')

    def __str__(self):
        return self.drug_name