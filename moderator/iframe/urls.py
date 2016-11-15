from django.conf.urls import url

from iframe.views import DesktopView


urlpatterns = [
    url(
        regex=r'^desktop/$',
        view=DesktopView.as_view(),
        name='desktop'
    ),
]
