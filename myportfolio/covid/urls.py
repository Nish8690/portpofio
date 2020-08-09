from django.urls import path

from . import views

urlpatterns = [
    path('', views.base,name='base'),
    # path('home/', views.home,name='home'),
    # path('aboutme/', views.aboutme,name='aboutme'),
    # path('projects/', views.projects,name='projects'),
    # path('contactme/', views.contactme,name='contactme'),
    # path('resume/', views.resume,name='resume'),
    # path('documents/', views.resume,name='resume'),
]
