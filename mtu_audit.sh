#!/usr/bin/env bash
# mtu_audit.sh - Reports MTU and txqueuelen across network devices
echo "=== INTERFACE MTU & QUEUE DEPTH ==="
ip link show | grep -E "mtu|qdisc"
echo "==================================="
