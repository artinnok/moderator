from datetime import timedelta


BROKER_URL = 'amqp://guest@localhost//'

CELERY_TIMEZONE = 'Europe/Moscow'

CELERYD_MAX_TASKS_PER_CHILD = 1

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = 'rpc://'

CELERY_IMPORTS = ['api.fetch', 'api.filter', 'api.start']

CELERYBEAT_SCHEDULE = {
    'moderate': {
        'task': 'start',
        'schedule': timedelta(seconds=30),
    }
}
