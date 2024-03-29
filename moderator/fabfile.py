from fabric.api import env, run, sudo, prefix

env.user = 'artem'
env.hosts = ['moderator']
env.cwd = '~/moderator_project/moderator/'
env.supervisor_programs = 'flower gunicorn celery:'


def git_pull():
    run("git pull")


def backend():
    sudo("find . -name '*.pyc' -delete")
    with prefix("source ../env/bin/activate"):
        run("pip install -r requirements/production.txt")
        run("python manage.py migrate --settings config.settings.production --noinput")
    sudo("supervisorctl restart {}".format(env.supervisor_programs))


def frontend():
    run("npm install")
    run("webpack")
    with prefix("source ../env/bin/activate"):
        run("python manage.py collectstatic --settings config.settings.production --noinput")


def update_frontend():
    print('=' * 20, 'FRONTEND UPDATE STARTED', '=' * 20)
    git_pull()
    frontend()
    print('=' * 20, 'FRONTEND UPDATE ENDED', '=' * 20)


def update_backend():
    print('=' * 20, 'BACKEND UPDATE STARTED', '=' * 20)
    git_pull()
    backend()
    print('=' * 20, 'BACKEND UPDATE ENDED', '=' * 20)


def update():
    print('*' * 40, 'UPDATE STARTED', '*' * 40)
    update_frontend()
    update_backend()
    print('*' * 40, 'UPDATE ENDED', '*' * 40)