"""{{cookiecutter.project_slug}} URL Mapping

The `urlpatterns` list maps URLs to views. More information:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Function views:
    1. Add an import:  from my_app import views
    2. Add entry to urlpatterns:  path('view_name', views.view_name, name='view_name')

Class-based views:
    1. Add an import:  from my_app.views import Home
    2. Add entry to urlpatterns:  path('view_name', ViewName.as_view(), name='view_name')

Including another (usually an app's) URLconf:
    1. Import the include() function: from django.urls import path, include
    2. Add a URL to urlpatterns:  path('appname', include('app.urls', namespace="app"))
    Path may be blank; in that case only the app URL is used

    -----------------------------------------------------------------------------------
    NOTE: when using the namespace argument with include(), the app's urls.py MUST have

        app_name="APPNAME" 

    before  urlpatterns = ...
    -----------------------------------------------------------------------------------
"""
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

# site-wide route mapping
urlpatterns = [
    path('admin', admin.site.urls),
    # To include urls from an app:
    #
    # path('', include('app.urls', namespace="appname")),  # delegate to app's URL config
    #
    # note: if path (1st arg) is not empty, it will be a prefix to app URL
    # and will follow the hostname, before the path in the app's urls.py
    #
    # i.e., if path here is "spam" and path in app/urls.py is "home",
    # url will be HOSTNAME:PORT/spam/home
    #
    # if first arg is empty, then paths in app.urls will immediately follow
    #  the host name

    # To configure a single view:
    #
    # from app.views import myview
    # path('viewpath', myview, name="myview")

]

# include Django Debug toolbar if DEBUG is set
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns

