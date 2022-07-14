#!/bin/sh
flask db upgrade
gunicorn --bind=0.0.0.0:8000 --log-level info --workers 4 app:app