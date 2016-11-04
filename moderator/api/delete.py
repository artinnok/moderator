from celery import shared_task

from api.fetch import base_fetch


@shared_task(name='delete_comment', rate_limit='2.5/s')
def delete_comment(owner_id, comment_id, access_token):
    method = 'wall.deleteComment'
    parameters = ('owner_id={owner_id}&'
                  'comment_id={comment_id}'.format(owner_id=owner_id,
                                                   comment_id=comment_id))
    res = base_fetch(method, parameters, access_token)
    out = {'comment_id': comment_id}
    out.update(res)
    return out
