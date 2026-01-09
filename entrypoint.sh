#!/bin/sh
set -e

# Start app
flask --app api/wsgi.py run --host=0.0.0.0 --port=5000