import os
import time
from watchdog.events import FileSystemEventHandler
from .file import File

class FileHandler(FileSystemEventHandler):
    def __init__(self, settings):
        self.settings = settings
        self._last_event = {}

    def on_created(self, event):
        if event.is_directory:
            return

        now = time.time()
        last_time = self._last_event.get(event.src_path, 0)
        if now - last_time < 1:
            return  
        self._last_event[event.src_path] = now

        # Warte, bis die Datei wirklich existiert und nicht mehr gesperrt ist
        for _ in range(10):  # max. 10 Versuche (ca. 2 Sekunden)
            if os.path.exists(event.src_path):
                try:
                    with open(event.src_path, "rb"):
                        break
                except Exception:
                    time.sleep(0.2)
            else:
                time.sleep(0.2)
        else:
            print(f"⚠ Datei konnte nicht geöffnet werden: {event.src_path}")
            return

        file = File(event.src_path, self.settings)
        print(f"📂 File created: {file.basename} ({event.src_path})")
        if file.destination:
            print(f"📂 Moving file: {file.basename} to {file.destination}")
            self.moveFile(file, event.src_path)

    def moveFile(self, file: File, src_path: str):
        import shutil
        filename = os.path.basename(src_path)
        destination_dir = file.destination
        destination_path = os.path.join(destination_dir, filename)
        print(destination_path)
        if os.path.exists(destination_path):
            print(f"⚠ Datei existiert bereits: {destination_path}")
            return

        shutil.move(src_path, destination_path)
        print(f"✅ Moved {filename} to {destination_path}")
