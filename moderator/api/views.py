from rest_framework.views import APIView
from rest_framework.response import Response
from celery import group
from django.conf import settings
from django.shortcuts import redirect

from api.fetch import fetch_post_list, fetch_comment_list, base_fetch
from api.filter import filter_comment_list, filter_post_list, flatten
from api.delete import delete_comment
from core.models import User, Public


class PermissionsView(APIView):
    """
    Проверка прав доступа
    """
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


class AuthorizeView(APIView):
    """
    Авторизует пользователя в приложении
    """
    url = ('https://oauth.vk.com/authorize?'
           'client_id={client_id}&'
           'display=page&'
           'redirect_uri={redirect_uri}&'
           'scope={scope}&'
           'response_type=token&'
           'v=5.59')

    def get(self, request, *args, **kwargs):
        return redirect(self.url.format(
            client_id=settings.CLIENT_ID,
            redirect_uri=settings.REDIRECT_URI,
            scope='wall,offline'
        ))


class StartView(APIView):
    """
    Старт зачистки коментов
    """
    def get(self, request, *args, **kwargs):
        out = []
        for public in Public.objects.all():
            owner_id = public.owner_id
            access_token = public.user.access_token

            # retrieve posts
            post_list = fetch_post_list.delay(owner_id).get()
            post_list = filter_post_list(post_list)

            # retrieve comments
            comment_list = group(fetch_comment_list.s(owner_id, post)
                                 for post in post_list)().get()
            comment_list = flatten(comment_list)
            comment_list = filter_comment_list(comment_list)

            # delete comments
            res = group(delete_comment.s(owner_id, comment, access_token)
                        for comment in comment_list)().get()
            out.append(res)

        return Response(out)

