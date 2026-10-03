#!/usr/bin/env bash
# network_interface_audit.sh - Quick Layer 2 and Layer 3 local state dump

echo "=== LAYER 2 INTERFACE STATE ==="
ip -br link
echo ""
echo "=== LAYER 3 ADDRESS MAPPINGS ==="
ip -br addr
echo ""
echo "=== ACTIVE LISTENING SOCKETS ==="
ss -tuln
