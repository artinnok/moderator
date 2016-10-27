from celery import shared_task
import requests

from core.models import Token


class Fetcher:
    url = 'https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}&v=5.59'

    def __init__(self, owner_id):
        self.owner_id = owner_id

    def fetch_post_list(self, owner_id):
        method = 'wall.get'
        parameters = ('owner_id={owner_id}'
                      '&count=10'.format(owner_id=owner_id))
        token = Token.objects.last().access_token

        json = fetch.delay(method, parameters, token)
        json = json.get()
        return json['response']['items']

    def filter_post_list(self, post_list):
        return (post['id'] for post in post_list if post['comments']['count'])

    def fetch_comment_list(self, owner_id, post_id):
        method = 'wall.getComments'
        parameters = ('owner_id={owner_id}&'
                      'post_id={post_id}&'
                      'need_likes=1&'
                      'count=100'.format(owner_id=owner_id, post_id=post_id))
        token = Token.objects.last().access_token

        json = fetch.delay(method, parameters, token)
        json = json.get()
        return json['response']['items']

    def filter_comment_list(self, comment_list):
        return [comment['id'] for comment in comment_list
                if comment['likes']['count'] < 5]

    def delete_comment(self, owner_id, comment_id):
        method = 'wall.deleteComment'
        parameters = ('owner_id={owner_id}&'
                      'comment_id={comment_id}'.format(owner_id=owner_id,
                                                       comment_id=comment_id))
        token = Token.objects.last().access_token

        json = fetch.delay(method, parameters, token)
        json = json.get()
        return json


@shared_task(name='start')
def start():
    out = []
    fetcher = Fetcher(-112088372)
    post_list = fetcher.fetch_post_list(fetcher.owner_id)
    post_list = fetcher.filter_post_list(post_list)
    for post in post_list:
        comment_list = fetcher.fetch_comment_list(fetcher.owner_id, post)
        out += fetcher.filter_comment_list(comment_list)
    for comment_id in out:
        fetcher.delete_comment(fetcher.owner_id, comment_id)


@shared_task(rate_limit='3/s')
def fetch(method, parameters, token):
    url = 'https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}&v=5.59'
    return requests.get(url.format(
        method_name=method,
        parameters=parameters,
        access_token=token
    )).json()


