#!/usr/bin/env bash
# port_scanner.sh - Inspect all active TCP sockets and their associated process names

echo "=== ACTIVE TCP LISTENING SERVICES ==="
ss -tulpn | grep LISTEN
echo "====================================="
