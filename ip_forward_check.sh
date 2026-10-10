#!/usr/bin/env bash
# ip_forward_check.sh - Audits whether machine is configured to route packets
FORWARD_STATUS=$(cat /proc/sys/net/ipv4/ip_forward)
echo "IPv4 Packet Forwarding (Routing): $FORWARD_STATUS (0=Disabled, 1=Enabled)"
