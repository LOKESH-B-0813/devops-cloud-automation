#!/usr/bin/env bash
# arp_gc_threshold_audit.sh - Displays kernel neighbor table garbage collector thresholds
echo "=== KERNEL ARP NEIGH GC THRESHOLDS ==="
sysctl net.ipv4.neigh.default.gc_thresh1 net.ipv4.neigh.default.gc_thresh2 net.ipv4.neigh.default.gc_thresh3
