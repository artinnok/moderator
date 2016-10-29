from django.conf.urls import url

from api.authorize import AuthorizeView, CallbackView
from api.views import PermissionsView, StartView


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
        regex=r'^permissions/$',
        view=PermissionsView.as_view(),
        name='permissions'
    ),
    url(
        regex=r'^start/$',
        view=StartView.as_view(),
        name='start'
    ),
]
