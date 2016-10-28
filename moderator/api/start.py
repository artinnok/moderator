from celery import shared_task, chain


@shared_task(name='start')
def start():
    pass