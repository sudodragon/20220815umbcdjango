"""
URL Configuration for superheroes
"""
from django.urls import path
from . import views   # import views from app

app_name = "superheroes"

urlpatterns = [
    path('', views.home, name='home'),
    path('secret', views.secret_word, name='secret'),
    path('random', views.random_word, name='random'),
    path('request_dump', views.request_dump, name='request_dump'),
]
