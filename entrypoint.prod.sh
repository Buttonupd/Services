#!/bin/sh

if ["$DATABASE = "dockerr_prod"]
then
    echo echo "Waiting for postgres..."
    while ! nc -z $DB_HOST $SQL_PORT; do
      sleep 0.1
    done
    
    echo "PostgresQL started"
fi

exec "$@"
