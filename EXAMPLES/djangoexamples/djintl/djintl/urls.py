"""djintl URL Mapping

The `urlpatterns` list maps URLs to views. More information:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/

Function views:
    1. Add an import:  from my_app import views
    2. Add entry to urlpatterns:  path(r'', views.home, name='home')

Class-based views:
    1. Add an import:  from my_app.views import Home
    2. Add entry to urlpatterns:  path(r'', Home.as_view(), name='home')

Including another (usually an app's) URLconf:
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls', namespace="blog"))
"""
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django import VERSION

# site-wide route mapping
urlpatterns = [
    path('admin/', admin.site.urls),
    # example
    path('core/', include('core.urls', namespace="core")),
]

# include Django Debug toolbar if DEBUG is set
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
