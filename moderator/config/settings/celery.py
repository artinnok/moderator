from datetime import timedelta


broker_url = 'amqp://guest@localhost//'

timezone = 'Europe/Moscow'

accept_content = ['json']
task_serializer = 'json'

result_serializer = 'json'
result_backend = 'rpc://'

imports = ['api.fetch', 'api.delete']

task_routes = {
    'fetch': 'foo',
    'fetch_post_list': 'foo',
    'fetch_comment': 'foo',
    'delete_comment': 'foo',
    'start': 'bar'
}

beat_schedule = {
    'moderate': {
        'task': 'start',
        'schedule': timedelta(minutes=5),
    },
}
