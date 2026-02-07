from fastapi import FastAPI
from app.api.run_controller import router as run_router
from app.api.scheduler_controller import router as scheduler_router

app = FastAPI(title="Excel Validation Backend")

app.include_router(run_router)
app.include_router(scheduler_router)

@app.get("/")
def health_check():
    return {"status": "Backend Running"}
