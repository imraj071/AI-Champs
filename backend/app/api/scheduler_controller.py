from fastapi import APIRouter
from app.infrastructure.schedule_repository import ScheduleRepository

router = APIRouter()

@router.post("/schedule/{job_id}")
def set_schedule(job_id: int, day: str, hour: int, minute: int):
    repo = ScheduleRepository()
    repo.save_schedule(
        job_id=job_id,
        day_of_week=day,
        hour=hour,
        minute=minute,
        enabled=True
    )
    return {"status": "Schedule saved"}
