from sqlalchemy.orm import Session
from logging_service.model.model import JobStatus

class JobStatusRepository:
    def create(self, parameter_id: int, status: str, current_epoch: int, progress: int, loss: int):
        with Session() as session:
            job_status = JobStatus(parameter_id=parameter_id, status=status, current_epoch=current_epoch, progress=progress, loss=loss)
            self.session.add(job_status)
            self.session.commit()
            return job_status

    def get_by_id(self, job_status_id: int):
        with Session() as session:
            return session.query(JobStatus).filter(JobStatus.id == job_status_id).first()

    def update(self, job_status_id: int, status: str, current_epoch: int, progress: int, loss: int):
        with Session() as session:
            job_status = self.get_by_id(job_status_id)
            if job_status:
                job_status.status = status
                job_status.current_epoch = current_epoch
                job_status.progress = progress
                job_status.loss = loss
                session.commit()
                return job_status
            return None

    def delete(self, job_status_id: int):
        with Session() as session:
            job_status = self.get_by_id(job_status_id)
            if job_status:
                session.delete(job_status)
                session.commit()
                return True
            return False