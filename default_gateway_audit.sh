#!/usr/bin/env bash
# default_gateway_audit.sh - Inspects default gateway address and device
echo "=== ACTIVE DEFAULT GATEWAY ROUTE ==="
ip route show default
echo "===================================="
