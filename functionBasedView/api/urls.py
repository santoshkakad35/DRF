# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.companyList, name='company-list'),
    path('company/<int:pk>/', views.companyDetails, name='company-detail'),
]
