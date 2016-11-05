from celery import shared_task
import requests


def base_fetch(method, parameters, access_token=''):
    url = ('https://api.vk.com/method/'
           '{method_name}?'
           '{parameters}&'
           'access_token={access_token}'
           '&v=5.59')
    return requests.get(url.format(
        method_name=method,
        parameters=parameters,
        access_token=access_token
    )).json()


@shared_task(name='fetch', rate_limit='2.5/s')
def fetch(method, parameters, access_token):
    return base_fetch(method, parameters, access_token)


@shared_task(name='fetch_post_list', rate_limit='2.5/s')
def fetch_post_list(owner_id):
    method = 'wall.get'
    parameters = ('owner_id={owner_id}'
                  '&count=100'.format(owner_id=owner_id))

    return base_fetch(method, parameters)['response']['items']


@shared_task(name='fetch_comment_list', rate_limit='2.5/s')
def fetch_comment_list(owner_id, post_id):
    method = 'wall.getComments'
    parameters = ('owner_id={owner_id}&'
                  'post_id={post_id}&'
                  'need_likes=1&'
                  'count=100'.format(owner_id=owner_id, post_id=post_id))

    return base_fetch(method, parameters)['response']['items']

