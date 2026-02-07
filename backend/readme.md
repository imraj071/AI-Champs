## Folder Structure

backend/
│
├── app/
│   ├── api/               
│   ├── core/              
│   ├── domain/           
│   ├── services/          
│   ├── infrastructure/    
│
├── logs/                  
├── main.py                

## Architecture 

API Layer       → FastAPI routes
Core Layer      → Job Runner, Config Loader
Service Layer   → Excel, Validation, Filesystem, Logging, Scheduler
Domain Layer    → Rules + Pydantic Models
Infrastructure  → Database + Repositories


## Steps

1. Project Skeleton: Create folder structure to separate responsibilities

2. Config Models (Domain Layer)
domain/models.py

3. Define the rules (use dictionary of lambda functions instead of if/else)
domain/rules.py

4. Excel Service
services/excel_service.py

5. Validation Service (Business logic)
services/validation_service.py

6. File System Service 
services/filesystem_service.py

7. Logging Service
services/logging_service.py (write logs into logs/job.log)

8. Job Runner (core)
core/job_runner.py

9. Manual Test Script (to test system without API)

10. Scheduler Service (Cron scheduling)
services/scheduler_service.py

11. SQLite Database Setup
infrastructure/database.py

12. Job Config Table
infrastructure/models.py

13. Repository Pattern
infrastructure/repositories.py

14. Config Loader (Converts DB model -> Pydantic config)
core/config_loader.py

15. Scheduler Uses DB Config

16. Weekly Cron Scheduling

17. FastAPI Backend
main.py

18. Manual Run API
api/run_controller.py

19. Schedule Table

20. Scheduler API


## Final System Flow

Manual Run:
Frontend -> API -> Job Runner -> Excel Validations -> Logs

Scheduled Run:
Scheduler -> Load Config from DB -> Job Runner -> Excel Validation -> Logs



