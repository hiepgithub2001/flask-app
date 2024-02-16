from model.model import JobLogging
from config.database import Session

class JobLoggingRepository:
    def create(self, parameter_id: int, batching: int, content: str):
        with Session() as session:
            job_logging = JobLogging(parameter_id=parameter_id, batching=batching, content=content)
            session.add(job_logging)
            session.commit()
            return job_logging

    def get_by_id(self, job_logging_id: int):
        with Session() as session:
            return session.query(JobLogging).filter(JobLogging.id == job_logging_id).first()

    def update(self, job_logging_id: int, batching: int, content: str):
        with Session() as session:
            job_logging = self.get_by_id(job_logging_id)
            if job_logging:
                job_logging.batching = batching
                job_logging.content = content
                session.commit()
                return job_logging
            return None

    def delete(self, job_logging_id: int):
        with Session() as session:
            job_logging = self.get_by_id(job_logging_id)
            if job_logging:
                session.delete(job_logging)
                session.commit()
                return True
            return False
