import os
import time
from celery import Celery

broker = os.getenv('CELERY_BROKER_URL', 'amqp://')
result_backend = os.getenv('CELERY_RESULT_BACKEND_URL', 'redis://')

app = Celery('tasks', broker=broker)
# set this separately because of issue with Windows
app.conf.update(result_backend=result_backend)

@app.task 
def add(x, y):     
    time.sleep(5)
    return x + y

@app.task
def tadd(numbers):
    return sum(numbers)