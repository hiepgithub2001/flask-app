from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from model.base import Base

from model.job_logging import JobLogging
from model.job_result import JobResult
from model.job_status import JobStatus

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