from rest_framework.views import APIView
from rest_framework.response import Response
from celery import group

from api.fetch import fetch_post_list, fetch_comment, base_fetch
from api.filter import filter_comment_list, filter_post_list
from api.delete import delete_comment
from core.models import User


class PermissionsView(APIView):
    def get(self, request, *args, **kwargs):
        method = 'account.getAppPermissions'
        parameters = ''
        token = User.objects.last().access_token
        res = base_fetch(method, parameters, token)
        return Response(res)


class StartView(APIView):
    def get(self, request, *args, **kwargs):
        access_token = '455c5c6c0a7234dbd5f7d2f187ba892a3b83453222abb289e674ed430d6303a01a8f3883267caab69d0e7'
        owner_id = -112088372

        # retrieve posts
        post_list = fetch_post_list.delay(owner_id, access_token).get()
        post_list = filter_post_list(post_list)

        # retrieve comments
        comment_list = group(fetch_comment.s(owner_id, post, access_token)
                             for post in post_list)().get()
        comment_list = filter_comment_list(comment_list)

        # delete comments
        out = group(delete_comment.s(owner_id, comment, access_token)
                    for comment in comment_list)().get()

        return Response(out)

