from django.db import models

# Create your models here.
class Category(models.Model):
    drug_category  = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.drug_category

class Drug(models.Model):
    drug_name = models.CharField(max_length=100, null=True)
    drug_image = models.ImageField(upload_to='drugs/%Y/%m/%d/',default='drug_default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    condition = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.drug_name