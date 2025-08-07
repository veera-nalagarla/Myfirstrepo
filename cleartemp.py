echo "Cleaning /tmp files older than 1 day..."
find /tmp -type f -mtime +1 -exec rm -f {} \;
