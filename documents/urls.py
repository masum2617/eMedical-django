from django.urls import path
from .import views

urlpatterns = [
    #path('history/<int:doctor_id>/', views.history, name='history'),
    path('history/', views.history, name='history'),
]
