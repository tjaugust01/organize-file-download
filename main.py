from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from utils import *

if __name__ == "__main__":   
    Settings = Settings() 
    Handler = FileHandler(Settings)
    Observer = Observer()
    print(f"Watching folder: {Settings.watchFolders[0]}")
    Observer.schedule(Handler, path=Settings.watchFolders[0], recursive=False)
    Observer.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            Observer.stop()
            break
    # observers = []
    # for ordner in Settings.watchFolders:
    #     observer = Observer()
    #     observer.schedule(Handler, path=ordner, recursive=False)
    #     observer.start()
    #     observers.append(observer)
    #     print(f"Started watching: {ordner}")

    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     for obs in observers:
    #         obs.stop()
    #     for obs in observers:
    #         obs.join()