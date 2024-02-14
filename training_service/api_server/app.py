import base64
from flask import Flask, request, jsonify
import pika
from dto.submit_training_job_request import SubmitTrainingJob
import pika
from dotenv import load_dotenv
import os
import logging

app = Flask(__name__)

load_dotenv()
TRAINING_TOPIC = os.getenv("TRAINING_KEY")
TRAINING_JOB_KEY = os.getenv("TRAINING_JOB_KEY")
MQ_HOST = os.getenv("MQ_HOST")

logging.basicConfig(level=logging.INFO)


RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'user_code_queue'

def publish_to_rabbitmq(user_code: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=MQ_HOST))
    channel = connection.channel()

    channel.basic_publish(exchange=TRAINING_TOPIC,
                        routing_key=TRAINING_JOB_KEY,
                        body=user_code)
    connection.close()

@app.route('/submit_code', methods=['POST'])
def submit_code():
    try:
        request_data = SubmitTrainingJob.model_validate(request.json)

        user_code = base64.b64decode(request_data.user_code_encoded).decode()
        publish_to_rabbitmq(user_code)

        return jsonify({'message': 'User code submitted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)