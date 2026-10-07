#!/usr/bin/env bash
# ephemeral_ports.sh - Displays range of outbound ephemeral ports allocated by OS
echo "=== LINUX IP LOCAL PORT RANGE ==="
cat /proc/sys/net/ipv4/ip_local_port_range
echo "=================================="
