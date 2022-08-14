"""
URL Configuration for superheroes
"""
from django.urls import path
from django.views.generic import TemplateView
from . import views
from .models import Superhero

urlpatterns = [
    # welcome page using template view
    path(
        '',
        views.HomeView.as_view(),
        name = 'home'
    ),

    path('other', views.OtherView.as_view(), name='other'),
    # NO view -- don't do this:
    path(
        'noview',
        TemplateView.as_view(template_name='superheroes/generic_only.html'),
        name="noview",
    ),

    # minimal views with models
    path(
        'herolist',
        views.HeroListView.as_view(),
        name="herolist",
    ),
    path(
        'herodetails/<int:pk>',
        views.HeroDetailView.as_view(),
        name="herodetails",
    ),

    # enhanced views with extra information
    path(
        'herolistplus/',
        views.HeroListViewPlus.as_view(),
        name="herolistplus",
    ),
    path(
        'herodetailsplus/<int:pk>/',
        views.HeroDetailViewPlus.as_view(),
        name="herodetailsplus",
    ),

    # create and update views
    path(
        'herocreate/',
        views.HeroCreateView.as_view(),
        name="herocreate",
    ),
    path(
        'heroupdate/<int:pk>/',
        views.HeroUpdateView.as_view(),
        name="heroupdate",
    ),
    path(
        'herodelete/<int:pk>/',
        views.HeroDeleteView.as_view(),
        name="herodelete",
    ),
    path(
        'citycreate',
        views.CityCreateView.as_view(),
        name="citycreate",
    ),
    path(
        'success', views.SuccessView.as_view(), name="success",
    )
]

