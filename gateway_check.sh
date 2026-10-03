#!/usr/bin/env bash
# gateway_check.sh - Identifies default gateway IP and interface path

GATEWAY_IP=$(ip route | grep default | awk '{print $3}')
INTERFACE=$(ip route | grep default | awk '{print $5}')

echo "Default Gateway: $GATEWAY_IP"
echo "Outbound Device: $INTERFACE"

# Ping default gateway to test local subnet connectivity
ping -c 2 "$GATEWAY_IP"
