#!/usr/bin/env bash
# coredump_audit.sh - Verifies core dump pattern and limits
echo "=== KERNEL CORE PATTERN ==="
sysctl kernel.core_pattern
echo "=== ULIMIT CORE DUMP SETTING ==="
ulimit -c
