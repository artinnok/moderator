from django.conf import settings
from django.conf.urls.static import static

from config.urls.base import *
from core.views import error404
from api.views import StartView


urlpatterns = urlpatterns + [
    url(
        regex=r'^error404/$',
        view=error404,
        name='error404'
    ),
    url(
        regex=r'^start/$',
        view=StartView.as_view(),
        name='start'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
