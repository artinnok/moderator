from celery import shared_task
from celery.contrib.methods import task_method
import requests

from core.models import Token


class Fetcher:
    def __init__(self, owner_id):
        self.owner_id = owner_id

    @shared_task(name='fetch', rate_limit='3/s', filter=task_method)
    def fetch(self, method, parameters, token):
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

    def fetch_post_list(self):
        method = 'wall.get'
        parameters = ('owner_id={owner_id}'
                      '&count=10'.format(owner_id=self.owner_id))
        token = Token.objects.last().access_token

        json = self.fetch
        return json

    def fetch_comment_list(self, post_id):
        method = 'wall.getComments'
        parameters = ('owner_id={owner_id}&'
                      'post_id={post_id}&'
                      'need_likes=1&'
                      'count=100'.format(owner_id=self.owner_id,
                                         post_id=post_id))
        token = Token.objects.last().access_token

        json = self.fetch
        return json

    def delete_comment(self, comment_id):
        method = 'wall.deleteComment'
        parameters = ('owner_id={owner_id}&'
                      'comment_id={comment_id}'.format(owner_id=self.owner_id,
                                                       comment_id=comment_id))
        token = Token.objects.last().access_token

        json = self.fetch
        return json
