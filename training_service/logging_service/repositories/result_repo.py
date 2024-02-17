from sqlalchemy.orm import Session
from logging_service.model.model import JobResult

from config.database import Session

class JobResultRepository:
    def create(self, parameter_id: int, accuracy: float, runtime: int, precision: float, logarithmic_loss: float):
        with Session() as session:
            job_result = JobResult(parameter_id=parameter_id, accuracy=accuracy, runtime=runtime, precision=precision, logarithmic_loss=logarithmic_loss)
            session.add(job_result)
            session.commit()
            return job_result

    def get_by_id(self, job_result_id: int):
        with Session() as session:
            return session.query(JobResult).filter(JobResult.id == job_result_id).first()

    def update(self, job_result_id: int, accuracy: float, runtime: int, precision: float, logarithmic_loss: float):
        with Session() as session:
            job_result = self.get_by_id(job_result_id)
            if job_result:
                job_result.accuracy = accuracy
                job_result.runtime = runtime
                job_result.precision = precision
                job_result.logarithmic_loss = logarithmic_loss
                session.commit()
                return job_result
            return None

    def delete(self, job_result_id: int):
        with Session() as session:
            job_result = self.get_by_id(job_result_id)
            if job_result:
                session.delete(job_result)
                session.commit()
                return True
            return False
