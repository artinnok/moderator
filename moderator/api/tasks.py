from celery import shared_task

from api.fetch import Fetcher
from core.models import Club


@shared_task(name='start')
def start():
    out = []
    fetcher = Fetcher(Club.objects.first().owner_id)
    post_list = fetcher.fetch_post_list(fetcher.owner_id)
    post_list = fetcher.filter_post_list(post_list)
    for post in post_list:
        comment_list = fetcher.fetch_comment_list(fetcher.owner_id, post)
        comment_list = fetcher.filter_comment_list(comment_list)
        out += [(post, comment_list)]
    return out
