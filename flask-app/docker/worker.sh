#!/bin/sh

# Enable strict error handling
set -o errexit  # Exit on any command failure
set -o pipefail # Exit if any command in a pipeline fails
set -o nounset  # Exit on use of uninitialized variables

# Check if FLASK_ENV is set, if not, default to 'production'
FLASK_CONFIG=${FLASK_CONFIG:-production}

if [ "$FLASK_CONFIG" = "development" ]; then
    echo "Running Celery worker in development mode with watchmedo"
    watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- \
        celery -A application.celery_app worker --concurrency=1 --loglevel=INFO
else
    echo "Running Celery worker in production mode"
    celery -A application.celery_app worker --concurrency=10 --loglevel=INFO
fi
