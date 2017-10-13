#!/bin/bash

NAME="geekbeacon"                                      # Name of the application
DJANGODIR=##DJANGODIR##                                # Django project directory
SOCKFILE=##GUNICORNSOCKDIR##/gunicorn.sock             # We will communicte using this unix socket
VENV_ACTIVATE=##VENVDIR##/bin/activate                 # Virtual environment activate script
USER=core                                              # The user to run as
GROUP=core                                             # The group to run as
NUM_WORKERS=5                                          # How many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=geekbeacon.settings.production  # Which settings file should Django use, here we use production
DJANGO_WSGI_MODULE=geekbeacon.wsgi                     # WSGI module name
WORKER_TIMEOUT=120

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source $VENV_ACTIVATE
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/core/djangodev/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --timeout=$WORKER_TIMEOUT \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
