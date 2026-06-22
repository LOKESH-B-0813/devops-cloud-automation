import shutil
from datetime import datetime

# 1. Get live system data
total, used, free = shutil.disk_usage("/")
percent_free = (free / total) * 100

# 2. Get the current timestamp so we know exactly WHEN this happened
# This uses the current year (2026) and live time
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Determine the status message
if percent_free < 20:
    status = "⚠️ WARNING: Disk space low!"
else:
    status = "✅ System healthy."

log_entry = f"[{timestamp}] Free Space: {percent_free:.2f}% | Status: {status}\n"

# 4. The DevOps Automation: Write it to a persistent log file
# 'a' means append mode, so it keeps adding lines without deleting old ones
with open("/home/lokesh-b/Desktop/system_logs.txt", "a") as file:
    file.write(log_entry)

print("Log successfully written to system_logs.txt!")

