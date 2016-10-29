from celery import shared_task
import requests


def base_fetch(method, parameters, access_token):
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


@shared_task(name='delete_comment', rate_limit='3/s')
def delete_comment(owner_id, comment_id, access_token):
    method = 'wall.deleteComment'
    parameters = ('owner_id={owner_id}&'
                  'comment_id={comment_id}'.format(owner_id=owner_id,
                                                   comment_id=comment_id))
    return base_fetch(method, parameters, access_token)