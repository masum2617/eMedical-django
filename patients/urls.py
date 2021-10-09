from django.urls import path,include
from .import views

urlpatterns = [

    path('patients_profile/', views.patients_profile, name='patients_profile'),
]
