from pathlib import Path
import shutil

class FileSystemService:

    def read(self, path: str):
        return Path(path)

    def write(self, source: str, destination: str):
        shutil.copy(source, destination)
        return destination
