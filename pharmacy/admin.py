from django.contrib import admin
from .models import Gastrointestinal, Cardiovascular, Respiratory
# Register your models here.

admin.site.register(Gastrointestinal)
admin.site.register(Cardiovascular)
admin.site.register(Respiratory)