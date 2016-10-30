from rest_framework.views import APIView
from rest_framework.response import Response
from celery import group

from api.fetch import fetch_post_list, fetch_comment, base_fetch
from api.filter import filter_comment_list, filter_post_list
from api.delete import delete_comment
from core.models import User, Public


class PermissionsView(APIView):
    def get(self, request, *args, **kwargs):
        method = 'account.getAppPermissions'
        parameters = ''
        out = []
        for user in User.objects.all():
            res = base_fetch(method, parameters, user.access_token)
            out.append({
                'user_id': user.user_id,
                'permissions': res['response']})
        return Response(out)


class StartView(APIView):
    def get(self, request, *args, **kwargs):
        out = []
        for public in Public.objects.all():
            owner_id = public.owner_id
            access_token = public.user.access_token

            # retrieve posts
            post_list = fetch_post_list.delay(owner_id, access_token).get()
            post_list = filter_post_list(post_list)

            # retrieve comments
            comment_list = group(fetch_comment.s(owner_id, post, access_token)
                                 for post in post_list)().get()
            comment_list = filter_comment_list(comment_list)

            # delete comments
            res = group(delete_comment.s(owner_id, comment, access_token)
                        for comment in comment_list)().get()
            out.append(res)

        return Response(out)

