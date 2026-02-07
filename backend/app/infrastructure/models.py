from sqlalchemy import Column, Integer, String, Float
from app.infrastructure.database import Base
from sqlalchemy import Boolean

class JobSchedule(Base):
    __tablename__ = "job_schedule"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer)
    day_of_week = Column(String)
    hour = Column(Integer)
    minute = Column(Integer)
    enabled = Column(Boolean, default=True)


class JobConfig(Base):
    __tablename__ = "job_config"

    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String)
    sheet_name = Column(String)
    column_name = Column(String)
    threshold = Column(Float)
    operation = Column(String)
    output_column = Column(String)
