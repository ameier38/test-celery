# Pull the Python 3.5 image.
FROM python:3.5-slim

# Create the default user.
RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
WORKDIR /home/user

# Specify the version of celery to install.
ENV CELERY_VERSION 4.0.2

# Install celery with the redis backend library.
RUN pip install celery[redis]=="$CELERY_VERSION"

# Specify the broker url. 'broker' will be the name of our RabbitMQ container.
ENV CELERY_BROKER_URL amqp://broker

# Specify the backend url. 'backend' will the be the name of our Redis container.
ENV CELERY_RESULT_BACKEND_URL redis://backend

# Set the user.
USER user

# Specify the command to execute when we run the container.
CMD ["celery", "worker", "--loglevel=INFO"]