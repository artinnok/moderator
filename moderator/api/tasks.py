from celery import shared_task

from core.models import Token


@shared_task(name='delet_comment_list')
def delete_comment_list(self, comment_id, owner_id):
    method = 'wall.deleteComment'
    parameters = ('owner_id={owner_id}&'
                  'comment_id={comment_id}'.format(owner_id=owner_id,
                                                   comment_id=comment_id))
    token = Token.objects.last().access_token

    json = self.fetch.delay(method, parameters, token).wait()
    return json['response']
