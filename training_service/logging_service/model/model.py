from sqlalchemy import Column, Float, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from model.base import Base

class MLModel(Base):
    __tablename__ = 'ml_model'
    id = Column(Integer, primary_key=True)

    model_script = Column(String)
    hash = Column(String)

    parameters = relationship('HyperParameter', backref='model')

class HyperParameter(Base):
    __tablename__ = 'parameter'
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer,  ForeignKey('ml_model.id'))

    learning_rate = Column(Float)
    num_epoch = Column(Integer)
    batch_size = Column(Integer)
    drop_out = Column(Float)

    result = relationship("JobResult", backref="parameter", uselist=False)
    status = relationship("JobStatus", backref="parameter", uselist=False)
    logs = relationship("JobLogging", backref="parameter")


class JobLogging(Base):
    __tablename__ = 'job_logging'
    id = Column(Integer, primary_key=True)
    parameter_id = Column(Integer,  ForeignKey('parameter.id'))

    batching = Column(Integer)
    content = Column(String)

class JobResult(Base):
    __tablename__ = 'job_result'
    id = Column(Integer, primary_key=True)
    parameter_id = Column(Integer,  ForeignKey('parameter.id'))

    accuracy = Column(Float)
    runtime = Column(Integer)
    precision = Column(Float)
    logarithmic_loss = Column(Float)

class JobStatus(Base):
    __tablename__ = 'job_status'
    id = Column(Integer, primary_key=True)
    parameter_id = Column(Integer,  ForeignKey('parameter.id'))

    status = Column(Enum('loading', 'training', 'evaluating', 'done', name="status_enum"))
    current_epoch = Column(Integer)
    progress = Column(Integer)
    loss = Column(Integer)


