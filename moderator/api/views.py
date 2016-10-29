from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from celery import chain, group, chord

from api.fetch import fetch, fetch_post_list, fetch_comment_list
from api.filter import filter_comment_list, filter_post_list
from core.models import Token


class DeleteView(APIView):
    url = 'https://api.vk.com/method/{method_name}?{parameters}&access_token={access_token}&v=5.59'

    def fetch(self, method, parameters, token):
        return requests.get(self.url.format(
            method_name=method,
            parameters=parameters,
            access_token=token
        )).json()

    def get(self, request, *args, **kwargs):
        method = 'wall.deleteComment'
        parameters = 'owner_id={}&comment_id={}'.format(-112088372, 41)
        token = Token.objects.last().access_token
        r = self.fetch(method, parameters, token)
        return Response(r)


class PermissionsView(DeleteView):
    def get(self, request, *args, **kwargs):
        method = 'account.getAppPermissions'
        parameters = ''
        token = Token.objects.last().access_token
        r = self.fetch(method, parameters, token)
        return Response(r)


class StartView(APIView):
    def get(self, request, *args, **kwargs):
        token = Token.objects.last().access_token
        owner = -112088372

        # posts
        method = 'wall.get'
        parameters = 'owner_id={}&count=10'
        res = fetch.delay(
            method,
            parameters.format(owner),
            token
        )
        post_list = res.get()['response']['items']
        post_list = filter_post_list(post_list)

        # comments
        method = 'wall.getComments'
        parameters = ('owner_id={}&'
                      'post_id={}&'
                      'need_likes=1&'
                      'count=100')
        res = group(fetch.s(method, parameters.format(owner, post), token)
                    for post in post_list)()
        comment_list = res.get()
        comment_list = filter_comment_list(comment_list)
        return Response(comment_list)

