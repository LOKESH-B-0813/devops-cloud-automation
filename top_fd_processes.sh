#!/usr/bin/env bash
# top_fd_processes.sh - Lists top processes holding the most open file descriptors
echo "=== TOP PROCESSES BY FILE DESCRIPTOR COUNT ==="
ls -l /proc/[0-9]*/fd 2>/dev/null | awk '{print $11}' | cut -d/ -f3 | sort | uniq -c | sort -nr | head -n 5
echo "==============================================="
