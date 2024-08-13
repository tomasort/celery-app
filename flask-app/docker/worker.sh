#!/bin/sh

celery -A application.celery_app worker --loglevel INFO