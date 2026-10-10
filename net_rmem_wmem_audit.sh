#!/usr/bin/env bash
# net_rmem_wmem_audit.sh - Audits default/max network read and write buffers
echo "=== TCP RMEM / WMEM CORE LIMITS ==="
sysctl net.core.rmem_max net.core.wmem_max net.ipv4.tcp_rmem net.ipv4.tcp_wmem
