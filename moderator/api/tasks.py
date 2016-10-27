from celery import shared_task
from rest_framework.response import Response
from rest_framework.views import APIView

from api.fetch import Fetcher
from core.models import Club


@shared_task(name='start')
def start():
    out = []
    owner_id = Club.objects.first().owner_id
    fetcher = Fetcher(owner_id)
    post_list = fetcher.fetch_post_list(fetcher.owner_id)
    post_list = fetcher.filter_post_list(post_list)
    for post in post_list:
        comment_list = fetcher.fetch_comment_list(fetcher.owner_id, post)
        comment_list = fetcher.filter_comment_list(comment_list)
        out += [(post, comment_list)]
        print(out)
    return out


class HelloView(APIView):
    def get(self, request, *args, **kwargs):
        out = []
        owner_id = Club.objects.last().owner_id
        fetcher = Fetcher(owner_id)
        post_list = fetcher.fetch_post_list(fetcher.owner_id)
        post_list = fetcher.filter_post_list(post_list)
        for post in post_list:
            comment_list = fetcher.fetch_comment_list(fetcher.owner_id, post)
            comment_list = fetcher.filter_comment_list(comment_list)
            out += [(post, comment_list)]
            print(out)
        return Response('hello')
