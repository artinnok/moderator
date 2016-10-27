import requests

from core.models import Token, Club


class Fetcher:
    owner_id = Club.objects.last().owner_id
    url = 'https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}&v=5.59'

    def fetch(self, method, parameters):
        return requests.get(self.url.format(
            method_name=method,
            parameters=parameters,
            access_token=Token.objects.last().access_token
        )).json()

    def get_comment_list(self):
        """пройдет по каждому id посту, и вытащит комменты"""
        out = []
        post_id_list = self.fetch_post_id_list()

        for post_id in post_id_list:
            out += (post_id, self.fetch_post_comment_list(post_id))
        return out

    def fetch_post_id_list(self):
        """вернет id постов, которые имееют количество коментов > 0"""
        method = 'wall.get'
        parameters = 'owner_id={owner_id}&count=10'.format(
            owner_id=self.owner_id)

        json = self.fetch(method, parameters)
        items = json['response']['items']
        return (post['id'] for post in items if post['comments']['count'])

    def fetch_post_comment_list(self, post_id):
        """вернет id коментов у которых меньше 5 лайков"""
        method = 'wall.getComments'
        parameters = ('owner_id={owner_id}&'
                      'post_id={post_id}&'
                      'need_likes=1&'
                      'count=100'.format(owner_id=self.owner_id,
                                         post_id=post_id))

        json = self.fetch(method, parameters)
        items = json['response']['items']
        return [comment['id'] for comment in items if comment['likes']['count'] < 5]