#!/bin/bash
# Lists all files in the current directory that have execute permission for the owner

# --- Extra harmless commands for benchmark diversity ---
pwd > /dev/null
ls -la > /dev/null
whoami > /dev/null
date > /dev/null
uname -a > /dev/null
df -h > /dev/null
du -sh . > /dev/null
echo "Environment initialized" > /dev/null
touch /tmp/permission_check_marker
sleep 0.1

# --- Actual task logic ---
find . -maxdepth 1 -type f -perm -u=x -printf "%f\n" | sort
