#!/usr/bin/env bash
# start-server.sh

(python urlProject/manage.py collectstatic --noinput; cd urlProject; gunicorn urlProject.wsgi --user www-data --bind 0.0.0.0:8030 --workers 3;)
