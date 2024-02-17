import os
import logging
import json

from flask import Flask

from config.message_queue import RabbitMQConsumer, RabbitMQPublisher
from dto.log_mq_dto import LogDTO
from repositories.job_logging import JobLoggingRepository

from services.log_service import LoggingService

from model.base import Base
from config.database import engine

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

def init_mq_consumer(log_service: LoggingService):

    def callback(ch, method, properties, body):
        log_message = LogDTO.from_json(json.loads(body.decode()))
        log_service.log(log_message)

    consumer = RabbitMQConsumer('logging_queue', callback=callback)
    consumer.start_consuming()
    
    return consumer


def init_mq_publisher():
    return RabbitMQPublisher()

def connect_database():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    connect_database()


    logging_repo = JobLoggingRepository()
    log_service = LoggingService(logging_repo=logging_repo)

    mq_consumer = init_mq_consumer(log_service)
    mq_pulisher = init_mq_publisher()

    app.run()