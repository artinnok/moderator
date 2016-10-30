from datetime import timedelta


broker_url = 'amqp://guest@localhost//'

timezone = 'Europe/Moscow'

accept_content = ['json']
task_serializer = 'json'

result_serializer = 'json'
result_backend = 'rpc://'

imports = ['api.fetch', 'api.delete']

beat_schedule = {
    'moderate': {
        'task': 'start',
        'schedule': timedelta(seconds=30),
    },
}
