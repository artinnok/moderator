from celery import shared_task
import requests

from api.fetch import Fetcher
from core.models import Club


@shared_task(name='start')
def start():
    out = []
    owner_id = Club.objects.first().owner_id
    fetcher = Fetcher(owner_id)
    post_list = fetcher.fetch_post_list(fetcher.owner_id)
    post_list = fetcher.filter_post_list(post_list)
    for post in post_list:
        comment_list = fetcher.fetch_comment_list(fetcher.owner_id, post)
        comment_list = fetcher.filter_comment_list(comment_list)
        out += comment_list
    for comment_id in out:
        fetcher.delete_comment(owner_id, comment_id)


@shared_task(rate_limit='3/s')
def fetch(method, parameters, token):
    url = 'https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}&v=5.59'
    return requests.get(url.format(
        method_name=method,
        parameters=parameters,
        access_token=token
    )).json()

