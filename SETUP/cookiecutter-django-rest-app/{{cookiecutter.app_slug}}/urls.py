"""
URL Configuration for {{cookiecutter.app_slug}}
"""
from django.urls import path
from . import views   # import views from app

app_name = "{{cookiecutter.app_slug}}"

urlpatterns = [
    # add url patterns for the {{cookiecutter.app_slug}} app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
