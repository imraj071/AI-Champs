from apscheduler.schedulers.background import BackgroundScheduler

class SchedulerService:

    def __init__(self, runner, config):
        self.scheduler = BackgroundScheduler()
        self.runner = runner
        self.config = config

    def start(self, day: str, hour: int, minute: int):
        self.scheduler.add_job(
            lambda: self.runner.run(self.config),
            trigger='cron',
            day_of_week=day,
            hour=hour,
            minute=minute,
            max_instances=1,
            coalesce=True
        )
        self.scheduler.start()


