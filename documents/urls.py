from django.urls import path
from .import views

urlpatterns = [
    #path('history/<int:doctor_id>/', views.history, name='history'),
    path('history/', views.history, name='history'),
    path('add_prescription/<int:patient_id>/', views.add_prescription, name='add_prescription'),
   
]
