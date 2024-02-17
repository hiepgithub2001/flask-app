from flask_sqlalchemy import SQLAlchemy
from model.model import JobStatus

class JobStatusRepository:
    def __init__(self, db : SQLAlchemy):
        self.db = db

    def create(self, parameter_id: int, status: str, current_epoch: int, progress: int, loss: int):
        job_status = JobStatus(parameter_id=parameter_id, status=status, current_epoch=current_epoch, progress=progress, loss=loss)
        self.db.session.add(job_status)
        self.db.session.commit()
        return job_status
    
    def get_by_param_id(self, parameter_id : int):
        return self.db.session.query(JobStatus).filter(JobStatus.parameter_id == parameter_id).first()

    def get_by_id(self, job_status_id: int):
        return self.db.session.query(JobStatus).filter(JobStatus.id == job_status_id).first()

    def get_latest_status_for_update(self, parameter_id):
        return self.db.session.query(JobStatus).filter(JobStatus.parameter_id == parameter_id)

    def update(self, job_status_id: int, status: str, current_epoch: int, progress: int, loss: int):
        job_status = self.get_by_id(job_status_id)
        if job_status:
            job_status.status = status
            job_status.current_epoch = current_epoch
            job_status.progress = progress
            job_status.loss = loss
            self.db.session.commit()
            return job_status
        return None

    def delete(self, job_status_id: int):
        job_status = self.get_by_id(job_status_id)
        if job_status:
            self.db.session.delete(job_status)
            self.db.session.commit()
            return True
        return False