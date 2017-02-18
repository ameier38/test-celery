import os
# Use an environment variable for the broker and backend urls
# since the host name will will be different when run inside the container.
broker_url = os.getenv('CELERY_BROKER_URL', 'amqp://')
result_backend = os.getenv('CELERY_BACKEND_URL')
# Specify to auto load the 'tasks.py' module.
imports = ("tasks",)