from datetime import timedelta


broker_url = 'amqp://guest@localhost//'

timezone = 'Europe/Moscow'

accept_content = ['json']
task_serializer = 'json'

result_serializer = 'json'
result_backend = 'rpc://'

imports = ['api.fetch', 'api.delete']

task_routes = {
    'fetch': 'fetch',
    'fetch_post_list': 'fetch',
    'fetch_comment_list': 'fetch',
    'delete_comment': 'delete',
    'start': 'start',
}

beat_schedule = {
    'moderate': {
        'task': 'start',
        'schedule': timedelta(minutes=5),
    },
}
