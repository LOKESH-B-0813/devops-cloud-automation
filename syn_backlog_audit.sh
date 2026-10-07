#!/usr/bin/env bash
# syn_backlog_audit.sh - Inspects system TCP SYN backlog threshold
echo "=== TCP MAX SYN BACKLOG THRESHOLD ==="
sysctl net.ipv4.tcp_max_syn_backlog
echo "======================================"
