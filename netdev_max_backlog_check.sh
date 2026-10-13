#!/usr/bin/env bash
# netdev_max_backlog_check.sh - Checks maximum packets queued on input network card ring buffers
echo "=== NETDEV MAX BACKLOG QUEUE SIZE ==="
sysctl net.core.netdev_max_backlog
