"""
URL Configuration for bands
"""
from django.urls import path
from . import views   # import views from app
from . import classviews

app_name = "bands"

urlpatterns = [
    # add url patterns for the bands app here

    # Example:
    path('', views.home, name='home'),
    path('sorted', views.bands_sorted, name='sorted'),
    path('list', views.bands_list, name='list'),
    path('listmore', views.bands_list_more, name='listmore'),
    path('genre/<str:genre_name>', views.bands_by_genre, name='genre'),
    path('search/<str:search_term>', views.bands_search, name='search'),
    path('<int:pk>', views.band_details, name='band_details'),
    path('<str:band_name>', views.band_basic, name='basic'),
    path('classlist', classviews.BandListView.as_view(), name='classlist'),
    path('class/<int:pk>', classviews.BandDetailView.as_view(), name='classdetails'),
]
