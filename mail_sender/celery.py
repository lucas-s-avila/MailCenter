import mail_sender.config as config

from celery import Celery

app = Celery(
    'mail_sender',
    broker = config.CELERY_BROKER_URL,
    backend = config.CELERY_RESULT_BACKEND,
    include = ['mail_sender.tasks']
)

app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()


