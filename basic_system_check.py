import os
import shutil
total, used, free = shutil.disk_usage("/")
free_gb = free / (1024**3)
if free_gb < 100.0:
    print("ALERT: Storage critically low!")
else:
    print("SYSTEM HEALTH: Disk space is stable.")
