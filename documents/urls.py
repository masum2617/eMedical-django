from django.urls import path
from .import views

urlpatterns = [

    path('history/', views.history, name='history'),
    path('add_prescription/<int:patient_id>/', views.add_prescription, name='add_prescription'),
    path('submitPrescription/<int:patient_id>/', views.submitPrescription, name="submitPrescription"),
    path('deletePrescItem/<int:pres_id>/', views.deletePrescItem, name="deletePrescItem"),
    path('review/<int:doctor_id>/', views.review, name="review"),
]
