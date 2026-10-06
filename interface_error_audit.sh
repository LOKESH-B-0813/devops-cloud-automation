#!/usr/bin/env bash
# interface_error_audit.sh - Checks network interfaces for packet drops or frame errors
echo "=== INTERFACE ERROR AUDIT ==="
ip -s link show | grep -E "(RX:|TX:|errors|dropped)"
echo "============================="
