import os

CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://redis:6379/0') 
CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://redis:6379/0') 

DJANGO_URL = os.environ.get('DJANGO_URL', 'http://localhost:8000/mailcenter/')