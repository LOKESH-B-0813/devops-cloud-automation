import os
import stat
file_path = "mock_passwd"
file_stats = os.stat(file_path)
file_permissions = file_stats.st_mode
if file_permissions & stat.S_IWOTH:
    print("CRITICAL ALERT: /etc/passwd is writable by others! Security breach!")
    os.chmod(file_path, 0o644)
    print("REMEDIATION SUCCESSFUL: File permissions have been locked back to safe levels.")
else:
    print("SECURITY CHECK: /etc/passwd permissions are locked down down and safe.")
