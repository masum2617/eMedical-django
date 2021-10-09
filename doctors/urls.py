from django.urls import path
from .import views

urlpatterns = [
    path('doctor-profile/',views.doctor_profile, name='doctor_profile'),
    path('doctor_specialization/',views.doctor_specialization, name='doctor_specialization'),
    path('doctors/',views.doctors, name='doctors'),
    path('qualification/', views.qualification, name='qualification'),
    path('experience/', views.experience, name='experience'),
]
