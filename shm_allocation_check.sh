#!/usr/bin/env bash
# shm_allocation_check.sh - Audits POSIX and IPC shared memory allocation
echo "=== IPC SHARED MEMORY SEGMENTS ==="
ipcs -m
