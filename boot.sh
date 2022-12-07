#!/bin/sh -e

exec gunicorn -b 0.0.0.0:8000 --access-logfile - --error-logfile - learning_platform.wsgi
