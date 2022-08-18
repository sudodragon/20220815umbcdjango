"""
URL Configuration for bands
"""
from django.urls import path
from . import views

app_name = "bands"

urlpatterns = [
    # home route
    path('', views.home, name='home'),

    # create route
    path('create', views.create, name='create'),

    # success route
    path('success', views.success, name='success'),

    # band urls
    path('bands', views.BandList.as_view(), name="bandlist"),
    path('band/<int:pk>', views.BandDetails.as_view(), name="banddetails"),
    path('bands/add', views.BandCreate.as_view(), name="bandcreate"),
    
    # album urls
    path('albums', views.AlbumList.as_view(), name="albumlist"),
    path('album/<int:pk>', views.AlbumDetails.as_view(), name="albumdetails"),
    path('albums/add', views.AlbumCreate.as_view(), name="albumcreate"),

    # artist urls
    path('artists', views.ArtistList.as_view(), name="artistlist"),
    path('artist/<int:pk>', views.ArtistDetails.as_view(), name="artistdetails"),
    path('artist/add', views.ArtistCreate.as_view(), name="artistcreate"),

    # bandmember urls
    path('bandmembers', views.BandMemberList.as_view(), name="bandmemberlist"),
    path('bandmember/<int:pk>', views.BandMemberDetails.as_view(), name="bandmemberdetails"),
    path('bandmember/add', views.BandMemberCreate.as_view(), name="bandmembercreate"),

    # genre urls
    path('genres', views.GenreList.as_view(), name="genrelist"),
    path('genre/<int:pk>', views.GenreDetails.as_view(), name="genredetails"),
    path('genres/add', views.GenreCreate.as_view(), name="genrecreate"),
]
