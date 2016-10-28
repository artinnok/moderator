from celery import shared_task
from celery.contrib.methods import task_method


class Filterer:
    @shared_task(name='filter_post_list', filter=task_method)
    def filter_post_list(self, post_list):
        return (post['id'] for post in post_list if post['comments']['count'])

    @shared_task(name='filter_comment_list', filter=task_method)
    def filter_comment_list(self, comment_list):
        return (comment['id'] for comment in comment_list
                if comment['likes']['count'] < 5)
