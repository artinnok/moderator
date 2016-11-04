from celery import shared_task
from django.conf import settings
import requests


@shared_task(name='start')
def start():
    return requests.get(settings.START_URL + '/api/start/').json()
