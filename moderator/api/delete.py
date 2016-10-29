from celery import shared_task

from api.fetch import base_fetch


@shared_task(name='delete_comment', rate_limit='3/s')
def delete_comment(owner_id, comment_id, access_token):
    method = 'wall.deleteComment'
    parameters = ('owner_id={owner_id}&'
                  'comment_id={comment_id}'.format(owner_id=owner_id,
                                                   comment_id=comment_id))
    return base_fetch(method, parameters, access_token)
