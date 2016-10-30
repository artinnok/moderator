from django.contrib import admin
from django.contrib.auth import models

from core.models import User, Public


class PublicInline(admin.TabularInline):
    model = Public
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [PublicInline]
    list_display = ('user_id', 'access_token', 'get_public_list')

    def get_public_list(self, obj):
        return [public.title for public in obj.public_list.all()]
    get_public_list.short_description = 'Паблики'


admin.site.register(User, UserAdmin)

# django user and group
admin.site.unregister(models.User)
admin.site.unregister(models.Group)
