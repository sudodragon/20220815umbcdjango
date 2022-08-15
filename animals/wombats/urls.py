from django.urls import path
from wombats.views import home, lunch

urlpatterns = [
    path('', home, name="home"),
    path('lunch', lunch, name="lunch"),
    path("daytime/meals", lunch, name="broccoli"),
]
