from dto.log_mq_dto import LogDTO
from repositories.result_repo import JobResultRepository
from repositories.status_repo import JobStatusRepository
from repositories.job_logging import JobLoggingRepository


class LoggingService:
    def __init__(self, 
            logging_repo : JobLoggingRepository,
            status_repo : JobStatusRepository,
            result_repo : JobResultRepository
        ):
        self.logging_repo = logging_repo
        self.status_repo = status_repo
        self.result_repo = result_repo
        return

    def log(self, log_message : LogDTO):
        self.analyze_log(log_message=log_message)
        self.logging_repo.create(log_message.id, log_message.batch, log_message.content)

    def analyze_log(self, log_message : LogDTO):
        last_train_log : str = None
        test_set_info : str = None
        for line in log_message.content.strip().split('\n'):
            if line.startswith("Train"):
                last_train_log = line
            elif line.startswith("Test set"):
                test_set_info = line

        if last_train_log is not None:
            parts = last_train_log.split()

            cur_epoch = int(parts[2])
            cur_progress = int(parts[4][1:-3])
            cur_loss = float(parts[-1])

            latest_status = self.status_repo.get_by_param_id(log_message.id)
            if latest_status is not None:
                if latest_status.current_epoch < cur_epoch or latest_status.progress < cur_progress :
                    latest_status.current_epoch = cur_epoch
                    latest_status.loss = cur_loss
                    latest_status.progress = cur_progress

                    self.db.session.commit()
            else:
                self.status_repo.create(
                    parameter_id=log_message.id,
                    status='training',
                    current_epoch=cur_epoch,
                    progress=cur_progress,
                    loss=cur_loss
                )

        if test_set_info is not None:
            parts = test_set_info.split(' ')

            average_loss = float(parts[4][:-1])
            accuracy = float(parts[7][1:-3])

            print("Average Loss:", average_loss)
            print("Accuracy:", accuracy)

