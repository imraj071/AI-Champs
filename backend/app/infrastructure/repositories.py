from app.infrastructure.database import SessionLocal
from app.infrastructure.models import JobConfig

class JobConfigRepository:

    def get_config(self, job_id: int):
        db = SessionLocal()
        job = db.query(JobConfig).filter(JobConfig.id == job_id).first()
        db.close()
        return job

    def create_config(self, **kwargs):
        db = SessionLocal()
        job = JobConfig(**kwargs)
        db.add(job)
        db.commit()
        db.refresh(job)
        db.close()
        return job
