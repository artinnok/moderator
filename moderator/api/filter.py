from celery import shared_task


@shared_task(name='filter_post_list')
def filter_post_list(post_list):
    return [post['id'] for post in post_list if post['comments']['count']]


@shared_task(name='filter_comment_list')
def filter_comment_list(comment_list):
    return [comment['id'] for comment in comment_list
            if comment['likes']['count'] < 5]
