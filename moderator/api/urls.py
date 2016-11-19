from django.conf.urls import url

from api.views import StartView, PublicView


urlpatterns = [
    url(
        regex=r'^start/$',
        view=StartView.as_view(),
        name='start'
    ),
    url(
        regex='r^public/$',
        view=PublicView.as_view(),
        name='public'
    )
]
