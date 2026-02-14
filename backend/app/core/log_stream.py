import asyncio

class LogStreamManager:

    def __init__(self):
        self.streams = {}

    def get_queue(self, job_id: int):
        if job_id not in self.streams:
            self.streams[job_id] = asyncio.Queue()
        return self.streams[job_id]

    async def push(self, job_id: int, message: str):
        queue = self.get_queue(job_id)
        await queue.put(message)

    async def listen(self, job_id: int):
        queue = self.get_queue(job_id)
        while True:
            message = await queue.get()
            yield message


log_stream_manager = LogStreamManager()
