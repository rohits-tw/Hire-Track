#!/bin/bash
# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000

if ["$database" "postgres"]
then 
    echo "Waiting for postgres"

    while !nc -z $database_host $database_port; do 
      sleep 0.1
    done

    echo "PostgreSQL is availabe. Proceeding with migrations."
fi

exec "$@"