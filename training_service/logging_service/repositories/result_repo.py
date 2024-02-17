from flask_sqlalchemy import SQLAlchemy
from model.model import JobResult


class JobResultRepository:
    def __init__(self, db : SQLAlchemy):
        self.db = db

    def create(self, parameter_id: int, accuracy: float, runtime: int, precision: float, logarithmic_loss: float):
            job_result = JobResult(parameter_id=parameter_id, accuracy=accuracy, runtime=runtime, precision=precision, logarithmic_loss=logarithmic_loss)
            self.db.session.add(job_result)
            self.db.session.commit()
            return job_result

    def get_by_id(self, job_result_id: int):
            return self.db.session.query(JobResult).filter(JobResult.id == job_result_id).first()

    def update(self, job_result_id: int, accuracy: float, runtime: int, precision: float, logarithmic_loss: float):
            job_result = self.get_by_id(job_result_id)
            if job_result:
                job_result.accuracy = accuracy
                job_result.runtime = runtime
                job_result.precision = precision
                job_result.logarithmic_loss = logarithmic_loss
                self.db.session.commit()
                return job_result
            return None

    def delete(self, job_result_id: int):
            job_result = self.get_by_id(job_result_id)
            if job_result:
                self.db.session.delete(job_result)
                self.db.session.commit()
                return True
            return False
