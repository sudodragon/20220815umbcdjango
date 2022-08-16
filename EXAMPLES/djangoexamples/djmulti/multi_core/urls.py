"""
URL Configuration for multi_core
"""
from django.urls import path
from . import views   # import views from app

app_name = "multi_core"

urlpatterns = [
    # add url patterns for the multi_core app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
    path('', views.home, name='home'),
]
