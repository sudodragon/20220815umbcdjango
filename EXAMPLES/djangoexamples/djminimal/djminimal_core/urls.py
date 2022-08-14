from django.urls import path
from djminimal_core import views

urlpatterns = [
    path('', views.home, name="home"),
]
