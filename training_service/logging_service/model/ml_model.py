from model.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from model.hyper_parameter import HyperParameter

class MLModel(Base):
    __tablename__ = 'ml_model'
    id = Column(Integer, primary_key=True)

    model_script = Column(String)
    hash = Column(Integer)

    parameters = relationship('HyperParameter', backref='model')