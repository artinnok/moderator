import requests

from core.models import Token, Club


class Fetcher:
    url = 'https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}&v=5.59'

    def __index__(self, owner_id):
        self.owner_id = owner_id

    def fetch(self, method, parameters, token):
        return requests.get(self.url.format(
            method_name=method,
            parameters=parameters,
            access_token=token
        )).json()['response']['items']

    def fetch_post_list(self, owner_id):
        method = 'wall.get'
        parameters = ('owner_id={owner_id}'
                      '&count=10'.format(owner_id=owner_id))
        token = Token.objects.last().access_token

        items = self.fetch(method, parameters, token)
        return items

    def filter_post_list(self, post_list):
        return (post['id'] for post in post_list if post['comments']['count'])

    def fetch_comment_list(self, owner_id, post_id):
        method = 'wall.getComments'
        parameters = ('owner_id={owner_id}&'
                      'post_id={post_id}&'
                      'need_likes=1&'
                      'count=100'.format(owner_id=owner_id, post_id=post_id))
        token = Token.objects.last().access_token

        items = self.fetch(method, parameters, token)
        return items

    def filter_comment_list(self, comment_list):
        return (comment['id'] for comment in comment_list
                if comment['likes']['count'] < 5)

