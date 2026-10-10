#!/usr/bin/env bash
# sys_file_max_check.sh - Checks maximum open file handles allowed by OS kernel
echo "System-Wide fs.file-max: $(cat /proc/sys/fs/file-max)"
