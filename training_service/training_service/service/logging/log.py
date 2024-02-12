import pika
import logging

class RMQLogger:
    _instance = None

    def __new__(cls, connection: pika.BlockingConnection, channel: pika.channel.Channel, queue_name: str):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.connection = connection
            cls._instance.channel = channel
            cls._instance.queue_name = queue_name
            cls._instance.log_buffer = []
        return cls._instance

    @staticmethod
    def createInstance(connection: pika.BlockingConnection, channel: pika.channel.Channel, queue_name: str):
        RMQLogger._instance = RMQLogger(connection, channel, queue_name)
        return RMQLogger._instance


    @staticmethod
    def getInstance():
        if RMQLogger._instance is None:
            raise Exception("Require to call createInstance before use")
        return RMQLogger._instance

    def log(self, message: str):
        logging.info(msg="Adding log message = " + message)
        self.log_buffer.append(message)
        if len(self.log_buffer) >= 10:
            self.flush_buffer()

    def flush_buffer(self):
        if self.log_buffer:
            messages = '\n'.join(self.log_buffer)
            self.channel.basic_publish(
                exchange='training', 
                routing_key=self.queue_name, 
                body=messages
            )
            logging.info("Logs published to RabbitMQ")
            self.log_buffer.clear()