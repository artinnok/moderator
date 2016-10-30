from celery import shared_task, group
from rest_framework.response import Response

from core.models import Public
from api.fetch import fetch_post_list, fetch_comment
from api.filter import filter_post_list, filter_comment_list
from api.delete import delete_comment


@shared_task(name='start')
def start():
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
