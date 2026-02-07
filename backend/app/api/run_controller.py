from fastapi import APIRouter
from app.services.excel_service import ExcelService
from app.services.filesystem_service import FileSystemService
from app.services.validation_service import ValidationService
from app.services.logging_service import LoggingService
from app.core.job_runner import JobRunner
from app.core.config_loader import ConfigLoader
from app.infrastructure.repositories import JobConfigRepository

router = APIRouter()

@router.post("/run/{job_id}")
def run_job(job_id: int):
    excel = ExcelService()
    fs = FileSystemService()
    val = ValidationService()
    log = LoggingService()

    runner = JobRunner(excel, fs, val, log)

    repo = JobConfigRepository()
    job_db = repo.get_config(job_id)
    config = ConfigLoader.from_db(job_db)

    runner.run(config)

    return {"status": "Job executed"}
