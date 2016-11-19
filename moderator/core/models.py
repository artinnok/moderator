from django.db import models

from core import common_models as cm
from core import behaviors as bh


class Public(bh.Titleable, cm.Common):
    """
    Паблик
    """
    owner_id = models.BigIntegerField(
        verbose_name='ID паблика'
    )
    access_token = models.CharField(
        max_length=200,
        verbose_name='Токен'
    )
    like = models.PositiveSmallIntegerField(
        verbose_name='Лайки'
    )
    minute = models.PositiveSmallIntegerField(
        verbose_name='Минуты'
    )

    class Meta:
        verbose_name = 'паблик'
        verbose_name_plural = 'паблики'

    def __str__(self):
        return str(self.owner_id)
