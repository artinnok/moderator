from celery import shared_task, chain
from celery.contrib.methods import task
import requests

from core.models import Token


class Fetcher:
    def __init__(self, owner_id):
        self.owner_id = owner_id

    def fetch_post_list(self):
        method = 'wall.get'
        parameters = ('owner_id={owner_id}'
                      '&count=10'.format(owner_id=self.owner_id))
        token = Token.objects.last().access_token

        json = fetch
        return json

    def fetch_comment_list(self, post_id):
        method = 'wall.getComments'
        parameters = ('owner_id={owner_id}&'
                      'post_id={post_id}&'
                      'need_likes=1&'
                      'count=100'.format(owner_id=self.owner_id,
                                         post_id=post_id))
        token = Token.objects.last().access_token

        json = fetch
        return json

    def delete_comment(self, comment_id):
        method = 'wall.deleteComment'
        parameters = ('owner_id={owner_id}&'
                      'comment_id={comment_id}'.format(owner_id=self.owner_id,
                                                       comment_id=comment_id))
        token = Token.objects.last().access_token

        json = fetch
        return json


@shared_task(name='start')
def start():
    out = []
    fetcher = Fetcher(-112088372)
    fetcher.fetch_post_list(-112088372)


@shared_task(name='fetch', rate_limit='3/s')
def fetch(method, parameters, token):
    url = ('https://api.vk.com/method/'
           '{method_name}?'
           '{parameters}&'
           'access_token={access_token}'
           '&v=5.59')
    return requests.get(url.format(
        method_name=method,
        parameters=parameters,
        access_token=token
    )).json()


@shared_task(name='filter_post_list')
def filter_post_list(post_list):
    return (post['id'] for post in post_list if post['comments']['count'])


@shared_task(name='filter_comment_list')
def filter_comment_list(comment_list):
    return (comment['id'] for comment in comment_list
            if comment['likes']['count'] < 5)
