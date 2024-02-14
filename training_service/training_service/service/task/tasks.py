
from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost//')

@app.task
def process_message(message):
    # Perform your task here
    print("Received message:", message)