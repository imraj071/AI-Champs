from app.infrastructure.database import SessionLocal
from app.infrastructure.models import JobSchedule

class ScheduleRepository:

    def get_schedule(self, job_id: int):
        db = SessionLocal()
        sched = db.query(JobSchedule).filter(JobSchedule.job_id == job_id).first()
        db.close()
        return sched

    def save_schedule(self, **kwargs):
        db = SessionLocal()
        sched = JobSchedule(**kwargs)
        db.add(sched)
        db.commit()
        db.refresh(sched)
        db.close()
        return sched
