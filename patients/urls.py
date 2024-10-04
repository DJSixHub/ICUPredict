from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_patient, name='add_patient'),
    path('view/', views.view_patient, name='view_patient'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

