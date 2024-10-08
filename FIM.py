#File Integrity Monitoring system using Watchdog

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


logging.basicConfig(level=logging.INFO, 
format='%(asctime)s -%(process)d - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


path = sys.argv[1] if len(sys.argv) > 1  else '.'


event_handler = LoggingEventHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
