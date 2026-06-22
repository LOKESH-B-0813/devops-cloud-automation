import shutil

# 1. Get disk usage statistics for the root file system ("/")
# .total, .used, and .free return values in bytes
total, used, free = shutil.disk_usage("/")

# 2. Calculate the percentage of free space left
percent_free = (free / total) * 100

print(f"Current Free Space: {percent_free:.2f}%")

# 3. The DevOps Logic: Alerting
if percent_free < 20:
    print("⚠️ WARNING: Disk space is running dangerously low!")
else:
    print("✅ System healthy. Everything looks good!")