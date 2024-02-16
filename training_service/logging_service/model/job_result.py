from sqlalchemy import Column, Float, ForeignKey, Integer
from model.base import Base

class JobResult(Base):
    __tablename__ = 'job_result'
    id = Column(Integer, primary_key=True)
    parameter_id = Column(Integer,  ForeignKey('parameter.id'))

    accuracy = Column(Float)
    runtime = Column(Integer)
    precision = Column(Float)
    logarithmic_loss = Column(Float)