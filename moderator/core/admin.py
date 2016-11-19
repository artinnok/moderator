from django.contrib import admin
from django.contrib.auth import models

from core.models import Public


admin.site.register(Public)

# django user and group
admin.site.unregister(models.User)
admin.site.unregister(models.Group)
