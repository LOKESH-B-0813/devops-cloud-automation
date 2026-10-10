#!/usr/bin/env bash
# disk_scheduler_audit.sh - Inspects active I/O scheduler across block disks
for sched in /sys/block/*/queue/scheduler; do
    echo "$sched: $(cat $sched)"
done
