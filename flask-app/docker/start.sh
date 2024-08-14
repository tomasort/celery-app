#!/bin/sh

# Enable strict error handling
# set -o errexit  # Exit on any command failure
# set -o pipefail # Exit if any command in a pipeline fails
# set -o nounset  # Exit on use of uninitialized variables

FLASK_CONFIG=${FLASK_CONFIG:-development}

# flask db init
echo "Running migration"
flask db migrate
echo "Running upgrade"
flask db upgrade

# Environment-specific actions
if [ "$FLASK_CONFIG" = "development" ]; then
    echo "Running in development mode"
    python application.py --host 0.0.0.0 --port $FLASK_PORT --debug
else
    echo "Running in production mode"
    python application.py --host 0.0.0.0 --port $FLASK_PORT
fi
