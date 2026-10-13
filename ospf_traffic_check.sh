#!/usr/bin/env bash
# ospf_traffic_check.sh - Audits kernel socket counters for IP Protocol 89 (OSPF)
echo "=== RAW IP PROTOCOL 89 (OSPF) STATS ==="
grep -w "89" /proc/net/raw || echo "No active OSPF raw daemon sockets detected on host."
