from django.urls import path,include
from .import views

urlpatterns = [

    path('patients_profile/', views.patients_profile, name='patients_profile'),
    # path('profile_patient/<int:doctor_id>/', views.profile_patient, name='profile_patient')
]
