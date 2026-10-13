#!/usr/bin/env bash
# bgp_port_audit.sh - Inspects local port 179 for active BGP peering engines (FRR/BIRD/Quagga)
echo "=== BGP (TCP PORT 179) LISTENER CHECK ==="
ss -tlnp sport = :179
