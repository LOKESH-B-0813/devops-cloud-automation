#!/usr/bin/env bash
# oom_killer_audit.sh - Inspects system kernel logs for historical OOM kill events
echo "=== OOM KILLER EVENTS AUDIT ==="
dmesg -T | grep -i -E "oom-killer|out of memory" || echo "No OOM Killer events detected."
