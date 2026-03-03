from datetime import datetime

DEBUG = True  # You can toggle this later

def log(stage, message):
    if not DEBUG:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} [{stage}] {message}")