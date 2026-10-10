#!/usr/bin/env bash
# tcp_keepalive_audit.sh - Inspects kernel TCP keepalive timing intervals
echo "=== KERNEL TCP KEEPALIVE INTERVALS ==="
sysctl net.ipv4.tcp_keepalive_time net.ipv4.tcp_keepalive_intvl net.ipv4.tcp_keepalive_probes
