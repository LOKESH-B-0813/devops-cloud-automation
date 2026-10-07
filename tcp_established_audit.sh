#!/usr/bin/env bash
# tcp_established_audit.sh - Audits active ESTABLISHED TCP streams
echo "=== ACTIVE ESTABLISHED TCP CONNECTIONS ==="
ss -t state established
echo "==========================================="
