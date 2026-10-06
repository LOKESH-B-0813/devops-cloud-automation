#!/usr/bin/env bash
# inode_monitor.sh - Audits filesystem inode allocation
echo "=== FILESYSTEM INODE USAGE ==="
df -i -x tmpfs -x devtmpfs
echo "=============================="
