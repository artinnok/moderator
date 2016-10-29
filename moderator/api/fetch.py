from celery import shared_task, group
import requests

from core.models import Token


@shared_task(name='fetch', rate_limit='3/s')
def fetch(method, parameters, token):
    url = ('https://api.vk.com/method/'
           '{method_name}?'
           '{parameters}&'
           'access_token={access_token}'
           '&v=5.59')
    return requests.get(url.format(
        method_name=method,
        parameters=parameters,
        access_token=token
    )).json()


@shared_task(name='fetch_post_list')
def fetch_post_list(owner_id):
    method = 'wall.get'
    parameters = ('owner_id={owner_id}'
                  '&count=10'.format(owner_id=owner_id))
    token = Token.objects.last().access_token

    json = fetch.delay(method, parameters, token)
    return json['response']['items']


@shared_task(name='fetch_comment_list')
def fetch_comment_list(post_list, owner_id):
    method = 'wall.getComments'
    token = Token.objects.last().access_token
    parameters = ('owner_id={owner_id}&'
                  'post_id={post_id}&'
                  'need_likes=1&'
                  'count=100'.format(owner_id=owner_id, post_id=post))

