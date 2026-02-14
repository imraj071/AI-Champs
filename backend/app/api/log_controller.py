from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.core.log_stream import log_stream_manager

router = APIRouter()

async def event_generator(job_id: int):
    async for message in log_stream_manager.listen(job_id):
        yield f"data: {message}\n\n"

@router.get("/logs/stream/{job_id}")
async def stream_logs(job_id: int):
    return StreamingResponse(
        event_generator(job_id),
        media_type="text/event-stream"
    )
