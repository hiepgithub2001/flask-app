
import pika
from dotenv import load_dotenv
import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.ml_model import MLModel

from model.base import Base


load_dotenv()
TRAINING_TOPIC = os.getenv("TRAINING_KEY")
TRAINING_LOG_KEY = os.getenv("TRAINING_LOGGING_KEY")
MQ_HOST = os.getenv("MQ_HOST")

POSTGRESS_HOST = os.getenv("POSTGRESS_HOST")
POSTGRESS_PORT = os.getenv("POSTGRESS_PORT")
POSTGRESS_USER = os.getenv("POSTGRESS_USER")
POSTGRESS_PASSWORD = os.getenv("POSTGRESS_PASSWORD")
POSTGERSS_DB = os.getenv("POSTGRESS_DB")


logging.basicConfig(level=logging.INFO)


def init_mq_consuming():
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=MQ_HOST))
    channel = connection.channel()

    channel.exchange_declare(exchange=TRAINING_TOPIC, exchange_type='topic')

    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(
        exchange=TRAINING_TOPIC, 
        queue=queue_name, 
        routing_key=TRAINING_LOG_KEY
    )

    def callback(ch, method, properties, body):
        print("Received message:")
        print(f"  Delivery tag: {method.delivery_tag}")
        print(f"  Exchange: {method.exchange}")
        print(f"  Routing key: {method.routing_key}")
        print(f"  Content type: {properties.content_type}")
        print(f"  Content encoding: {properties.content_encoding}")
        print(f"  Headers: {properties.headers}")
        print(f"  Message body: {body.decode()}")


    channel.basic_consume(
        queue=queue_name, 
        on_message_callback=callback, 
        auto_ack=True
    )
    channel.start_consuming()

def connect_database():
    db_url = f'postgresql+psycopg2://{POSTGRESS_USER}:{POSTGRESS_PASSWORD}@{POSTGRESS_HOST}:{POSTGRESS_PORT}/{POSTGERSS_DB}'
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)


connect_database()
init_mq_consuming()

