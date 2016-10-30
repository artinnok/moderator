from django.conf.urls import url

from api.views import PermissionsView, AuthorizeView


urlpatterns = [
    url(
        regex=r'^authorize/$',
        view=AuthorizeView.as_view(),
        name='authorize'
    ),
    url(
        regex=r'^permissions/$',
        view=PermissionsView.as_view(),
        name='permissions'
    ),
]
