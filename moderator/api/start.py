from celery import shared_task, chain

from api.fetch import fetch, fetch_post_list, fetch_comment_list
from api.filter import filter_comment_list, filter_post_list


@shared_task(name='start')
def start():
    res = chain(
        fetch_post_list.s(-112088372),
        filter_post_list.s(),
    )()
    data = res.get()
    print(data)
