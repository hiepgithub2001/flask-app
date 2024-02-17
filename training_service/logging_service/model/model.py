from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class MLModel(db.Model):
    __tablename__ = 'ml_model'
    id = Column(Integer, primary_key=True)

    model_script = Column(String)
    hash = Column(String)

    parameters = relationship('HyperParameter', backref='model')

class HyperParameter(db.Model):
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


class JobLogging(db.Model):
    __tablename__ = 'job_logging'
    id = Column(Integer, primary_key=True)
    parameter_id = Column(Integer,  ForeignKey('parameter.id'))

    batching = Column(Integer)
    content = Column(String)

class JobResult(db.Model):
    __tablename__ = 'job_result'
    id = Column(Integer, primary_key=True)
    parameter_id = Column(Integer,  ForeignKey('parameter.id'))

    accuracy = Column(Float)
    runtime = Column(Integer)
    precision = Column(Float)
    logarithmic_loss = Column(Float)

class JobStatus(db.Model):
    __tablename__ = 'job_status'
    id = Column(Integer, primary_key=True)
    parameter_id = Column(Integer,  ForeignKey('parameter.id'))

    status = Column(Enum('loading', 'training', 'evaluating', 'done', name="status_enum"))
    current_epoch = Column(Integer)
    progress = Column(Integer)
    loss = Column(Float)


