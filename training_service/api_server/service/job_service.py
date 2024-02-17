from config.message_queue import RabbitMQPublisher
from dto.submit_parameter_req import HyperParametersDTO
from repositories.parameter_repo import HyperParameterRepository
from repositories.model_repo import MLModelRepository

import base64
import hashlib
import json


class JobService:
    def __init__(self, job_repo : MLModelRepository, param_repo : HyperParameterRepository, mq_publisher : RabbitMQPublisher):
        self.job_repo = job_repo
        self.param_repo = param_repo
        self.publisher = mq_publisher

    def submit_job(self, user_decoded_code : str, parameter : HyperParametersDTO):
        md5_hash = self.get_MD5_hash(user_decoded_code)

        if self.job_repo.get_model_by_hash(md5_hash) != None:
            raise Exception("Duplicated model")
        else:
            ml_model = self.job_repo.add_model(user_decoded_code, md5_hash)
            parameter_model = self.param_repo.create_hyperparameter(
                model_id=ml_model.id,
                learning_rate=parameter.lr,
                num_epoch=parameter.epochs,
                batch_size=parameter.batch_size,
                drop_out=parameter.drop_out
            )

            message = {
                'user_decoded_code' : user_decoded_code,
                'paramter_id' : parameter_model.id,
                'paramter' : parameter.tojson()
            }

            self.publisher.publish_job(json.dumps(message))
    
    def submit_param(self, user_model_id : int, parameter : HyperParametersDTO):
        model = self.job_repo.get_model_by_id(user_model_id)

        if model is None:
            return
        
        user_decoded_code = base64.b64decode(model.model_script).decode()
        parameter_model = self.param_repo.create_hyperparameter(
            learning_rate=parameter.lr,
            num_epoch=parameter.epochs,
            batch_size=parameter.batch_size,
            drop_out=parameter.drop_out
        )

        return True
    
    def get_MD5_hash(self, user_decoded_code : str):
        md5 = hashlib.md5()
        md5.update(user_decoded_code.encode())

        return md5.hexdigest()