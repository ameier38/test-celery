import os

# Specify to auto load the 'tasks.py' module.
imports = ("tasks",)
broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://')
result_backend = os.getenv('CELERY_RESULT_BACKEND_URL', 'redis://')
