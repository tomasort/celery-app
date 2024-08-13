#!/bin/sh

celery -A application.celery_app flower --port=$FLOWER_PORT