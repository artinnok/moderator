from django.db import models

from core import common_models as cm
from core import behaviors as bh


class User(cm.Common):
    """
    Пользователь Вконтакте, имеет много Пабликов
    """
    user_id = models.BigIntegerField(
        verbose_name='ID пользователя'
    )
    access_token = models.CharField(
        max_length=200,
        verbose_name='Токен'
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['-created']

    def __str__(self):
        return str(self.user_id)


class Public(bh.Titleable, cm.Common):
    """
    Паблик
    """
    user = models.ForeignKey(
        'core.User',
        verbose_name='Пользователь',
        related_name='public_list'
    )
    owner_id = models.BigIntegerField(
        verbose_name='ID паблика'
    )

    class Meta:
        verbose_name = 'паблик'
        verbose_name_plural = 'паблики'

    def __str__(self):
        return str(self.owner_id)
