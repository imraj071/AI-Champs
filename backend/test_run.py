import time
from app.services.excel_service import ExcelService
from app.services.filesystem_service import FileSystemService
from app.services.validation_service import ValidationService
from app.services.logging_service import LoggingService
from app.services.scheduler_service import SchedulerService
from app.core.job_runner import JobRunner
from app.core.config_loader import ConfigLoader
from app.infrastructure.repositories import JobConfigRepository

excel = ExcelService()
fs = FileSystemService()
val = ValidationService()
log = LoggingService()

runner = JobRunner(excel, fs, val, log)

repo = JobConfigRepository()
job_db = repo.get_config(1)  # load job id 1
config = ConfigLoader.from_db(job_db)

scheduler = SchedulerService(runner, config)

scheduler.start(day="sun", hour=2, minute=20)
print("Weekly scheduler started (Sun 2:20 AM)")



print("Scheduler running with DB config...")

while True:
    time.sleep(10)
