"""
URL Configuration for yeasty
"""
from django.urls import path
# from . import views   # import views from app
from yeasty.views import home, baguette

app_name = "yeasty"

urlpatterns = [
    # add url patterns for the yeasty app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
    path('', home, name="home"),
    path('baguette', baguette, name="baguette"),
]
