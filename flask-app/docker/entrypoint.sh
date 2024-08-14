#!/bin/sh

# Enable strict error handling
set -o errexit  # Exit on any command failure
set -o pipefail # Exit if any command in a pipeline fails
set -o nounset  # Exit on use of uninitialized variables

# Function to wait for a service to be ready
wait_for_service() {
  local host=$1
  local port=$2
  echo "Waiting for ${host}:${port} to be ready..."
  while ! nc -z "$host" "$port"; do
    sleep 1
  done
  echo "${host}:${port} is up!"
}

# Wait for PostgreSQL
wait_for_service "postgres" 5432

# Wait for Redis
wait_for_service "redis" 6379

# Wait for rabbitMQ
# wait_for_service "rabbit" 5672

# Execute the command provided as arguments to the script
exec "$@"