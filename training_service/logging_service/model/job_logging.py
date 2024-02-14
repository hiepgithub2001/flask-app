from sqlalchemy import Column, ForeignKey, Integer, String
from model.base import Base

class JobLogging(Base):
    __tablename__ = 'job_logging'
    id = Column(Integer, primary_key=True)
    parameter_id = Column(Integer,  ForeignKey('parameter.id'))

    batching = Column(Integer)
    content = Column(String)