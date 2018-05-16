from celery import Celery
import time

config = dict()
config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'

celery = Celery('add_task', broker=config['CELERY_BROKER_URL'])
celery.conf.update(config)


@celery.task
def add_task(a, b):
    # some long running task here
    return a + b
