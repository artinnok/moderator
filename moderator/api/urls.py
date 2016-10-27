from django.conf.urls import url

from api.authorize import AuthorizeView, CallbackView
from api.tasks import HelloView


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
        regex=r'^hello/$',
        view=HelloView.as_view(),
        name='hello'
    ),
]
