#!/bin/sh
# Health check for HyperCode services

# Exit immediately if a command exits with a non-zero status
set -e

# Check if the API server is running
if ! curl -sSf http://localhost:8000/health > /dev/null; then
    echo "Health check failed: API server is not responding"
    exit 1
fi

# Check if required services are running
# Example: Check if Redis is accessible
# if ! redis-cli ping > /dev/null; then
#     echo "Health check failed: Redis is not accessible"
#     exit 1
# fi

echo "All services are healthy"
exit 0
