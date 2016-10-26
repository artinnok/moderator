from django.conf.urls import url

from api.views import (AuthorizeView, CallbackView, PostsView,
                       PermissionsView, DeleteView)

urlpatterns = [
    url(
        regex=r'^authorize/$',
        view=AuthorizeView.as_view(),
        name='authorize'
    ),
    url(
        regex=r'^callback/$',
        view=CallbackView.as_view(),
        name='callback'
    ),
    url(
        regex=r'^posts/$',
        view=PostsView.as_view(),
        name='posts'
    ),
    url(
        regex=r'^permissions/$',
        view=PermissionsView.as_view(),
        name='permissions'
    ),
    url(
        regex=r'^delete/$',
        view=DeleteView.as_view(),
        name='delete'
    ),
]
