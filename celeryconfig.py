import os

# Specify to auto load the 'tasks.py' module.
imports = ("tasks",)
result_backend = os.getenv('CELERY_RESULT_BACKEND_URL', 'redis://')