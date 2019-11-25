#!/bin/bash

# Exporting all environment variables to use in crontab
env | sed 's/^\(.*\)$/ \1/g' > /root/env


function_postgres_ready() {
python << END
import socket
import time
import os

port = int(os.environ["POSTGRES_PORT"])
host = os.environ["POSTGRES_HOST"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('db', port))
s.close()
END
}

>&2 echo "Postgres is up - executing commands...";

echo '======= MAKING MIGRATIONS'
python3 manage.py makemigrations

echo '======= RUNNING MIGRATIONS'
python3 manage.py migrate

echo '======= STARTING CRON'
cron

echo '======= RUNNING SERVER'
python3 manage.py runserver 0.0.0.0:4000
