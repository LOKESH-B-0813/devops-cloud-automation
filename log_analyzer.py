"""import os
import shutil

def check_system_resources():
    print("=" * 50)
    print("🚀 LIVE DEVOPS MONITOR: Checking System Resources")
    print("=" * 50)
    
    # 1. Check Disk Space Usage
    # shutil.disk_usage returns total, used, and free bytes
    total, used, free = shutil.disk_usage("/")
    used_percent = (used / total) * 100
    
    print(f"🔹 Disk Usage: {used_percent:.2f}% used")
    if used_percent > 85:
        print("🔺 CRITICAL: Disk space usage is dangerously high!")
        
    # 2. Check System Memory (RAM) using Linux /proc/meminfo
    try:
        with open("/proc/meminfo", "r") as f:
            lines = f.readlines()
        
        # Extract Total and Free memory values from the system file
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

if __name__ == "__main__":
    check_system_resources()
"""
