from django.contrib import admin
from django.contrib.auth.models import User, Group

from core.models import Token, Club


class TokenAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'access_token', 'expires_in',)


class ClubAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner_id',)

admin.site.register(Token, TokenAdmin)
admin.site.register(Club, ClubAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
