import os
import time
from celery import Celery

app = Celery('tasks')

# set backend again separately because of issue with Windows
result_backend = os.getenv('CELERY_RESULT_BACKEND_URL', 'redis://')
app.conf.update(result_backend=result_backend)

@app.task 
def add(x, y):     
    time.sleep(5)
    return x + y

@app.task
def tadd(numbers):
    return sum(numbers)