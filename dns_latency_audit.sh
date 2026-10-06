#!/usr/bin/env bash
# dns_latency_audit.sh - Measures query roundtrip against primary nameservers
echo "=== DNS RESOLUTION LATENCY ==="
dig @8.8.8.8 google.com | grep "Query time"
echo "=============================="
