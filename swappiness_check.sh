#!/usr/bin/env bash
# swappiness_check.sh - Checks kernel tendency to swap anonymous memory
echo "Current Swappiness: $(cat /proc/sys/vm/swappiness)"
