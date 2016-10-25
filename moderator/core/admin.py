from django.contrib import admin
from django.contrib.auth.models import User, Group

from core.models import Token


class TokenAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'access_token', 'expires_in')

admin.site.register(Token, TokenAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
