from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.pharmacy, name='pharmacy'),
    # path('drug_search', views.drug_search, name='drug_search'),
]
