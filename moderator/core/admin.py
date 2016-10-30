from django.contrib import admin
from django.contrib.auth import models

from core.models import User, Public


class PublicInline(admin.TabularInline):
    model = Public
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [PublicInline]
    list_display = ('user_id', 'access_token',)


admin.site.register(User, UserAdmin)

# django user and group
admin.site.unregister(models.User)
admin.site.unregister(models.Group)
