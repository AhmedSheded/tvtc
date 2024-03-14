#!/bin/bash

while true
do
    # Activate the virtual environment
    source ../venv/bin/activate

    # Run Gunicorn in the background with nohup
    nohup gunicorn --bind 0.0.0.0:8000 tvtc.wsgi > gunicorn.log 2>&1 &

    # Deactivate the virtual environment
    deactivate

    # Sleep for 1 hour
    sleep 1h
done

