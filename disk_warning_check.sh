#!/usr/bin/env bash
df -h --output=source,pcent,target -x tmpfs -x devtmpfs
