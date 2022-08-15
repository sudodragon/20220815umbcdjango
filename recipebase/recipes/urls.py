"""
URL Configuration for recipes
"""
from django.urls import path
from . import views   # import views from app

app_name = "recipes"

urlpatterns = [
    path('', views.home, name="home"),
    path('steak', views.steak, name="steak"),
    # add url patterns for the recipes app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
