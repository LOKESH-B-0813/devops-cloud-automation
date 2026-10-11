#!/usr/bin/env bash
# tcp_fin_timeout_audit.sh - Inspects tcp_fin_timeout socket reclaim duration
echo "=== TCP FIN TIMEOUT DURATION ==="
sysctl net.ipv4.tcp_fin_timeout
echo "================================"
