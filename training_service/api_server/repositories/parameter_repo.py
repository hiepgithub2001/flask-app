from flask_sqlalchemy import SQLAlchemy
from model.model import HyperParameter


class HyperParameterRepository:
    def __init__(self, db : SQLAlchemy):
        self.db = db

    def get_hyperparameter_by_id(self, hyperparameter_id):
        return self.db.session.query(HyperParameter).filter(HyperParameter.id == hyperparameter_id).first()

    def create_hyperparameter(self, model_id, learning_rate, num_epoch, batch_size, drop_out):
        hyperparameter = HyperParameter(model_id=model_id, learning_rate=learning_rate,
                                        num_epoch=num_epoch, batch_size=batch_size, drop_out=drop_out)
        self.db.session.add(hyperparameter)
        self.db.session.commit()
        return hyperparameter

    def update_hyperparameter(self, hyperparameter_id, learning_rate=None, num_epoch=None, batch_size=None, drop_out=None):
        hyperparameter = self.db.session.query(HyperParameter).filter(HyperParameter.id == hyperparameter_id).first()
        if hyperparameter:
            if learning_rate is not None:
                hyperparameter.learning_rate = learning_rate
            if num_epoch is not None:
                hyperparameter.num_epoch = num_epoch
            if batch_size is not None:
                hyperparameter.batch_size = batch_size
            if drop_out is not None:
                hyperparameter.drop_out = drop_out
            self.session.commit()
        return hyperparameter

    def delete_hyperparameter(self, hyperparameter_id):
        hyperparameter = self.db.session.query(HyperParameter).filter(HyperParameter.id == hyperparameter_id).first()
        if hyperparameter:
            self.db.session.delete(hyperparameter)
            self.db.session.commit()