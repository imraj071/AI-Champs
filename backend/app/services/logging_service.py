import logging
import asyncio
from app.core.log_stream import log_stream_manager

class LoggingService:

    def __init__(self, job_id: int, file="logs/job.log"):
        self.job_id = job_id
        logging.basicConfig(
            filename=file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def log(self, message: str):
        formatted = f"[Job {self.job_id}] {message}"
        logging.info(formatted)

        try:
            loop = asyncio.get_event_loop()
            loop.create_task(
                log_stream_manager.push(self.job_id, formatted)
            )
        except RuntimeError:
            pass
