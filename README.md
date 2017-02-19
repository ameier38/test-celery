### Docker + Celery = awesome
This repo provides a simple configuration for getting started with Docker and Celery.
To run the application, clone the repo with the following command.
```
git clone https://github.com/ameier38/test-celery.git
```
Then, make sure Docker is installed, and call the following command from within the repo.
```
docker-compose up
```
The application should then be ready, and you can execute the tasks located in tasks.py
from an IPython shell such as the following.
```python
In [1]: from tasks import add
In [2]: from celery import group
In [3]: %%time
   ...: g = group(add.s(i, i+1) for i in range(10))
   ...: value_async = sum(g().get())
Wall time: 5.05 s
In [4]: value_async
Out[4]: 100
```

For more detailed information about the configuration, check out the post
[here](http://mindhypertrophy.com/articles/6)