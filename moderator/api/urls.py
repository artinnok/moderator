from django.conf.urls import url

from api.views import AuthorizeView, CallbackView

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
]
