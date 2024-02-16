from sqlalchemy import Column, ForeignKey, Integer, Enum
from model.base import Base

class JobStatus(Base):
    __tablename__ = 'job_status'
    id = Column(Integer, primary_key=True)
    parameter_id = Column(Integer,  ForeignKey('parameter.id'))

    status = Column(Enum('loading', 'training', 'evaluating', 'done', name="status_enum"))
    current_epoch = Column(Integer)
    progress = Column(Integer)
    loss = Column(Integer)

