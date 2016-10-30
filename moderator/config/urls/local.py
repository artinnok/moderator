from django.conf import settings
from django.conf.urls.static import static

from config.urls.base import *


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
