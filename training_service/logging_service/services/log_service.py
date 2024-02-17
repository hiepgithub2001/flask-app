from dto.log_mq_dto import LogDTO
from repositories.job_logging import JobLoggingRepository


class LoggingService:
    def __init__(self, logging_repo : JobLoggingRepository):
        self.logging_repo = logging_repo
        return

    def log(self, log_message : LogDTO):
        self.logging_repo.create(log_message.id, log_message.batch, log_message.content)