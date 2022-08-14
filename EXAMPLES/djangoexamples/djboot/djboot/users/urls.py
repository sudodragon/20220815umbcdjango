from django.conf.urls import url

from . import views

urlpatterns = [
    path(
        regex='',
        view=views.UserListView.as_view(),
        name='list'
    ),
    path(
        regex='~redirect/',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    path(
        regex='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    path(
        regex='~update/',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
]
