from app.infrastructure.database import engine, Base
from app.infrastructure.models import JobConfig

Base.metadata.create_all(bind=engine)
print("Database and tables created.")
