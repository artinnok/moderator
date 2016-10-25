from django.conf.urls import url

from api.views import AuthorizeView

urlpatterns = [
    url(
        regex=r'^authorize/$',
        view=AuthorizeView.as_view(),
        name='authorize'
    ),
]
