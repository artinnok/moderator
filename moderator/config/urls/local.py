from django.conf import settings
from django.conf.urls.static import static

from config.urls.base import *
from api.views import StartView


urlpatterns = urlpatterns + [
    url(
        regex=r'^start/$',
        view=StartView.as_view(),
        name='start'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
