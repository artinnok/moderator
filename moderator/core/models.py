from django.db import models

from core import common_models as cm
from core import behaviors as bh


class Token(cm.Common):
    """
    Токен, полученный от Вконтакте
    """
    user_id = models.BigIntegerField(
        verbose_name='ID пользователя'
    )
    access_token = models.CharField(
        max_length=200,
        verbose_name='Токен'
    )
    expires_in = models.BigIntegerField(
        verbose_name='Истекает в течение'
    )

    class Meta:
        verbose_name = 'токен'
        verbose_name_plural = 'токены'
        ordering = ['-created']

    def __str__(self):
        return str(self.user_id)


class Club(bh.Titleable, cm.Common):
    """
    Сущность паблика
    """
    owner_id = models.BigIntegerField(
        verbose_name='ID паблика'
    )

    class Meta:
        verbose_name = 'паблик'
        verbose_name_plural = 'паблики'

    def __str__(self):
        return str(self.owner_id)
