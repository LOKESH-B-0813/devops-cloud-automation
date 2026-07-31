import os
import shutil
import stat

def check_disk_space():
    print("--- [1] DISK CAPACITY AUDIT ---")
    total, used, free = shutil.disk_usage("/")
    used_percent = (used / total) * 100
    print(f"Disk Usage: {used_percent:.2f}%")
    
    if used_percent > 80:
        print("ALERT: Storage space is critically low!")
    else:
        print("STATUS: Storage level is healthy.\n")

def check_security():
    print("--- [2] SECURITY PERMISSION AUDIT ---")
    file_path = "mock_passwd"
    
    if not os.path.exists(file_path):
        print("WARNING: Target file 'mock_passwd' does not exist. Skipping check.\n")
        return

    file_stats = os.stat(file_path)
    file_permissions = file_stats.st_mode

    if file_permissions & stat.S_IWOTH:
        print("CRITICAL ALERT: Security breach detected! Fixing permissions now...")
        os.chmod(file_path, 0o644)
        print("REMEDIATION SUCCESSFUL: File permissions locked back to 644.\n")
    else:
        print("SECURITY CHECK: File permissions are locked down and safe.\n")

# Run both audits
check_disk_space()
check_security()
