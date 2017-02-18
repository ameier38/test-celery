import os
import time
from celery import Celery

app = Celery('tasks')  
@app.task 
def add(x, y):     
    time.sleep(5)
    return x + y

@app.task
def tadd(numbers):
    return sum(numbers)