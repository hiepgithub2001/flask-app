from config.database import Session
from logging_service.model.model import HyperParameter


class HyperParameterRepository:
    def get_hyperparameter_by_id(hyperparameter_id):
        with Session() as session:
            return session.query(HyperParameter).filter(HyperParameter.id == hyperparameter_id).first()

    def create_hyperparameter(model_id, learning_rate, num_epoch, batch_size, drop_out):
        with Session() as session:
            hyperparameter = HyperParameter(model_id=model_id, learning_rate=learning_rate,
                                            num_epoch=num_epoch, batch_size=batch_size, drop_out=drop_out)
            session.add(hyperparameter)
            session.commit()
            return hyperparameter

    def update_hyperparameter(hyperparameter_id, learning_rate=None, num_epoch=None, batch_size=None, drop_out=None):
        with Session() as session:
            hyperparameter = session.query(HyperParameter).filter(HyperParameter.id == hyperparameter_id).first()
            if hyperparameter:
                if learning_rate is not None:
                    hyperparameter.learning_rate = learning_rate
                if num_epoch is not None:
                    hyperparameter.num_epoch = num_epoch
                if batch_size is not None:
                    hyperparameter.batch_size = batch_size
                if drop_out is not None:
                    hyperparameter.drop_out = drop_out
                session.commit()
            return hyperparameter

    def delete_hyperparameter(hyperparameter_id):
        with Session() as session:
            hyperparameter = session.query(HyperParameter).filter(HyperParameter.id == hyperparameter_id).first()
            if hyperparameter:
                session.delete(hyperparameter)
                session.commit()