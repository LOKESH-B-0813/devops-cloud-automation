# mount_fs_inspector.py - Parses /proc/mounts to list persistent mounted filesystems
with open("/proc/mounts", "r") as f:
    for line in f:
        dev, mount_point, fs_type, opts, _, _ = line.split()
        if fs_type in ["ext4", "xfs", "btrfs", "vfat"]:
            print(f"Device: {dev:<15} | Mount: {mount_point:<15} | Type: {fs_type}")
