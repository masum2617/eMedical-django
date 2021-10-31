from django.urls import path
from .import views

urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('doctor_dashboard/',views.doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/',views.patient_dashboard, name='patient_dashboard'),
    path('status/<int:patient_id>',views.status, name='status'),
    path('current_patient/<int:patient_id>/', views.current_patient, name="current_patient"),
]
