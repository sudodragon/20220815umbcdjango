#!/usr/bin/env python
from django.urls import path
from . import views

app_name = "words"

urlpatterns = [
    path('', views.home, name='home'),
    path('noboot', views.homenoboot, name='homenoboot'),
    path('layout', views.layout, name='layout'),
    path('layoutloops', views.layoutloops, name='layoutloops'),
    path('cycle', views.cycle, name='cycle'),
    path('grid', views.grid, name='grid'),
    path('alerts', views.alerts, name='alerts'),
    path('breadcrumbs', views.breadcrumbs, name='breadcrumbs'),
]
