from datetime import timedelta


broker_url = 'amqp://guest@localhost//'

timezone = 'Europe/Moscow'

# worker_max_tasks_per_child = 1

accept_content = ['json']
task_serializer = 'json'

result_serializer = 'json'
result_backend = 'rpc://'

imports = ['api.fetch', 'api.filter']

beat_schedule = {
    'moderate': {
        'task': 'start',
        'schedule': timedelta(seconds=30),
    }
}
