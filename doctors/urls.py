from django.urls import path
from .import views

urlpatterns = [
    path('doctor-profile/',views.doctor_profile, name='doctor_profile'),
    path('doctor_specialization/',views.doctor_specialization, name='doctor_specialization'),
    path('doctors/',views.doctors, name='doctors'),
    path('qualification/', views.qualification, name='qualification'),
    path('experience/', views.experience, name='experience'),
    path('booking/<int:doctor_id>/', views.booking, name='booking'),
    # path('history/<int:patient_id>/', views.booking, name='booking'),
    path('medical_history/', views.medical_history, name='medical_history'),
    path('profile/<int:doctor_id>/', views.profile, name='profile'),
    path('doctor_search/', views.doctor_search, name='doctor_search'),
    path('schedule_timing/<int:doctor_id>/', views.schedule_timing, name='schedule_timing'),
    path('patient_appointment/<int:doctor_id>/', views.patient_appointment, name='patient_appointment'),
    path('video_call/<int:doctor_id>/', views.video_call, name="video_call"),
    path('appointments/', views.appointments, name="appointments"),
    path('viewReview/', views.viewReview, name="viewReview"),
    path('viewReviewOnProfile/', views.viewReviewOnProfile, name="viewReviewOnProfile"),
    path('deleteAppointment/', views.deleteAppointment, name="deleteAppointment"),
]
