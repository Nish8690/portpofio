from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.base,name='base'),
    path('home/', views.home,name='home'),
    path('aboutme/', views.aboutme,name='home'),
    path('projects/', views.projects,name='home'),
    path('contactme/', views.contactme,name='home'),
    path('resume/', views.resume,name='home'),
]
