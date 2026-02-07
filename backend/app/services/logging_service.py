import logging

class LoggingService:

    def __init__(self, file="logs/job.log"):
        logging.basicConfig(
            filename=file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def log(self, message: str):
        logging.info(message)
