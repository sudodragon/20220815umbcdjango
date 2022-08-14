"""
URL Configuration for scratch_core
"""
from django.urls import path
from . import views   # import views from app

app_name = "scratch_core"

urlpatterns = [
    path('hello1', views.Hello1.as_view(), name='hello1'),
    path('hello2', views.Hello2.as_view(), name='hello2'),
    path('hello3', views.Hello3.as_view(), name='hello3'),
    # add url patterns for the scratch_core app here

    # Examples:
    # path('', views.home, name='home'),
    # path('thing', views.thing, name='thing'),
]
