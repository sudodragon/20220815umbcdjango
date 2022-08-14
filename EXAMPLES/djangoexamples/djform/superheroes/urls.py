"""
URL Configuration for superheroes
"""
from django.urls import path
from . import views

app_name = 'superheroes'

urlpatterns = [
    path('', views.home, name='home'),
    path('demoform', views.demoform, name='demoform'),
    path('heroform', views.heroform, name='heroform'),
    path('heroadd', views.heroadd, name='heroadd'),
    path('herolist', views.herolist, name='herolist'),
]

