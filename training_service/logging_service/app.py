import os
import logging
import json

from flask import Flask

from config.message_queue import RabbitMQConsumer, RabbitMQPublisher
from dto.log_mq_dto import LogDTO
from repositories.result_repo import JobResultRepository
from repositories.status_repo import JobStatusRepository
from repositories.job_logging import JobLoggingRepository

from services.log_service import LoggingService

from config.database import DATABASE_URL
from model.model import db


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

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
    db.init_app(app)
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    connect_database()

    logging_repo = JobLoggingRepository(db)
    status_repo = JobStatusRepository(db)
    result_repo = JobResultRepository(db)

    log_service = LoggingService(
        logging_repo=logging_repo, 
        status_repo=status_repo,
        result_repo=result_repo
    )

    mq_consumer = init_mq_consumer(log_service)
    mq_pulisher = init_mq_publisher()

    app.run()