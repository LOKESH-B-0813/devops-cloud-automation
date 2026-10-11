#!/usr/bin/env bash
# tcp_congestion_check.sh - Audits active TCP congestion control algorithm (e.g. cubic, bbr)
echo "=== CURRENT TCP CONGESTION CONTROL ==="
sysctl net.ipv4.tcp_congestion_control net.ipv4.tcp_available_congestion_control
echo "======================================"
