from celery import shared_task
from celery.contrib.methods import task_method


# owner_id -112088372
class Starter:
    def __init__(self, fetcher, filterer):
        self.fetcher = fetcher
        self.filterer = filterer

    @shared_task(name='start', filter=task_method)
    def start(self):
        out = []