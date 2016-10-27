import requests

from core.models import Token, Club


class Fetcher:
    owner_id = Club.objects.last().owner_id
    url = 'https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}&v=5.59'

    def fetch(self, method, parameters, token):
        return requests.get(self.url.format(
            method_name=method,
            parameters=parameters,
            access_token=token
        )).json()

    def fetch_post_list(self, owner_id):
        """вернет id постов, которые имееют количество коментов > 0"""
        method = 'wall.get'
        parameters = ('owner_id={owner_id}'
                      '&count=10'.format(owner_id=owner_id))
        token = Token.objects.last().access_token

        json = self.fetch(method, parameters, token)
        items = json['response']['items']
        return items

    def filter_post_list(self, post_list):
        return (post['id'] for post in post_list if post['comments']['count'])

    def fetch_comment_list(self, owner_id, post_id):
        """вернет id коментов у которых меньше 5 лайков"""
        method = 'wall.getComments'
        parameters = ('owner_id={owner_id}&'
                      'post_id={post_id}&'
                      'need_likes=1&'
                      'count=100'.format(owner_id=owner_id, post_id=post_id))
        token = Token.objects.last().access_token

        json = self.fetch(method, parameters, token)
        items = json['response']['items']
        return items

    def filter_comment_list(self, comment_list):
        return (comment['id'] for comment in comment_list
                if comment['likes']['count'] < 5)
