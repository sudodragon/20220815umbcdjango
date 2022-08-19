from django.urls import include, path
from rest_framework import routers
from . import views, viewsets

app_name = 'api'

router = routers.DefaultRouter()
router.register('artists', viewsets.ArtistViewSet)
router.register('artworks', viewsets.ArtworkViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('artists-cbv', views.ArtistsList.as_view(), name='artists-cbv'),
    path('artists-cbv/<str:pk>', views.ArtistsDetail.as_view(), name='artists-detail-cbv'),
    path('artworks-cbv', views.ArtworksList.as_view(), name='workists-cbv'),
    path('artworks-cbv/<str:pk>', views.ArtworksDetail.as_view(), name='artworks-detail-cbv'),
    path('hello', views.hello_world, name='hello'),
    path('artists-fbv/<str:guid>', views.artists, name='artists-fbv'),
    #    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

