from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.conf import settings
import requests

from core.models import Token, Club


class BaseAPI(APIView):
    url = 'https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}&v=5.59'
    method_name = ''
    parameters = ''

    def get_json_response(self, method, parameters):
        return requests.get(self.url.format(
            method_name=method,
            parameters=parameters,
            access_token=Token.objects.last().access_token
        )).json()

    def get(self, request, *args, **kwargs):
        res = self.get_json_response(self.method_name, self.parameters)
        return Response(res)


class AuthorizeView(APIView):
    url = 'https://oauth.vk.com/authorize?client_id={client_id}&display=page&redirect_uri={redirect_uri}&scope={scope}&response_type=code&v=5.59'

    def get(self, request, *args, **kwargs):
        return redirect(self.url.format(
            client_id=settings.CLIENT_ID,
            redirect_uri=settings.REDIRECT_URI,
            scope='friends,photos,wall,audio'
        ))


class CallbackView(APIView):
    url = 'https://oauth.vk.com/access_token?client_id={client_id}&client_secret={client_secret}&redirect_uri={redirect_uri}&code={code}'

    def get(self, request, *args, **kwargs):
        code = request.query_params['code']
        r = requests.get(self.url.format(
            client_id=settings.CLIENT_ID,
            client_secret=settings.CLIENT_SECRET,
            redirect_uri=settings.REDIRECT_URI,
            code=code
        ))
        json = r.json()
        Token.objects.update_or_create(
            access_token=json['access_token'],
            defaults=json
        )
        return Response('ok')


class PostsView(BaseAPI):
    owner_id = Club.objects.last().owner_id

    def get(self, request, *args, **kwargs):
        data = self.get_comment_list()
        return Response(data)

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
        json = self.get_json_response(method, parameters)
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
        json = self.get_json_response(method, parameters)
        items = json['response']['items']
        return [comment['id'] for comment in items if comment['likes']['count'] < 5]


class PermissionsView(BaseAPI):
    method_name = 'account.getAppPermissions'
    parameters = ''


class DeleteView(BaseAPI):
    method_name = 'wall.deleteComment'
    parameters = 'owner_id=-112088372&comment_id=40'



