import os
import shutil

def check_system_resources():
    print("=" * 50)
    print("🚀 LIVE DEVOPS MONITOR: Checking System Resources")
    print("=" * 50)
    
    # 1. Check Disk Space Usage
    total, used, free = shutil.disk_usage("/")
    used_percent = (used / total) * 100
    
    print(f"🔹 Disk Usage: {used_percent:.2f}% used")
    if used_percent > 85:
        print("🔺 CRITICAL: Disk space usage is dangerously high!")
        
    # 2. Check System Memory (RAM) using Linux /proc/meminfo
    ram_percent = 0
    try:
        with open("/proc/meminfo", "r") as f:
            lines = f.readlines()
        
        mem_total = int(lines[0].split()[1])
        mem_available = int(lines[2].split()[1])
        mem_used = mem_total - mem_available
        ram_percent = (mem_used / mem_total) * 100
        
        print(f"🔹 RAM Usage: {ram_percent:.2f}% used")
        if ram_percent > 90:
            print("🔺 CRITICAL: RAM allocation has exceeded safety thresholds!")
            
    except Exception as e:
        print(f"⚠️ Error reading memory resources: {e}")
        
    print("-" * 50)
    if used_percent <= 85 and ram_percent <= 90:
        print("✅ System health is optimal. No issues detected.")
    print("=" * 50)

def check_security_threats():
    print("\n" + "=" * 50)
    print("🛡️  CYBERSECURITY SHIELD: Auditing Authentication Logs")
    print("=" * 50)
    
    auth_log_path = "/var/log/auth.log"
    
    # Check if the script has permissions to read the system security logs
    if not os.path.exists(auth_log_path):
        print("⚠️  Security alert: Cannot access /var/log/auth.log.")
        print("💡 Tip: Run this script with 'sudo' to inspect real security metrics.")
        print("=" * 50)
        return

    try:
        failed_logins = 0
        sudo_commands = []
        
        with open(auth_log_path, "r") as f:
            for line in f:
                # Catching brute-force attempts or bad passwords
                if "FAILURE" in line or "Failed password" in line:
                    failed_logins += 1
                # Catching when admin rights are executed
                if "COMMAND=" in line:
                    sudo_commands.append(line.strip())
                    
        print(f"🔹 Failed Login Attempts Detected: {failed_logins}")
        if failed_logins > 5:
            print("🚨 WARNING: High number of failed login attempts! Potential Brute Force!")
            
        print(f"🔹 Sudo/Admin Commands Executed Today: {len(sudo_commands)}")
        if len(sudo_commands) > 0:
            print("📋 Last executed admin action:")
            print(f"   👉 {sudo_commands[-1][:80]}...") # Shows the most recent admin action
            
    except Exception as e:
        print(f"⚠️ Error parsing security logs: {e}")
        
    print("=" * 50)

if __name__ == "__main__":
    check_system_resources()
    check_security_threats()
