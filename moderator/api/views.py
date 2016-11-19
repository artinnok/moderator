from rest_framework.views import APIView
from rest_framework.response import Response
from celery import group

from api.fetch import fetch_post_list, fetch_comment_list
from api.filter import filter_comment_list, filter_post_list, flatten
from api.delete import delete_comment
from core.models import Public


class PublicView(APIView):
    """
    Добавляет паблики с access_token + owner_id
    """
    def post(self, request, *args, **kwargs):
        Public.objects.update_or_create(
            owner_id=request.data['owner_id'],
            defaults=request.data
        )
        return Response({"success": True})


# TODO переписываем
class StartView(APIView):
    """
    Старт зачистки коментов
    """
    def get(self, request, *args, **kwargs):
        out = []
        for public in Public.objects.all():
            owner_id = public.owner_id
            access_token = public.access_token

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

