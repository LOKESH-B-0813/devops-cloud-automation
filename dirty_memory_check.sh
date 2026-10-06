#!/usr/bin/env bash
# dirty_memory_check.sh - Checks dirty pages waiting to be flushed to persistent storage
echo "=== KERNEL DIRTY MEMORY CACHE ==="
cat /proc/meminfo | grep -i dirty
echo "================================="
