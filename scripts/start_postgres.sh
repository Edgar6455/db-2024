#!/bin/bash

ROOT_DIR=$(dirname "$(dirname "$(realpath "$0")")")
cd "$ROOT_DIR" || exit

CONTAINER_NAME="db-2024-database"
DB_NAME="db-2024-database"
DB_USER="postgres"
DB_PASSWORD="db2024"
POSTGRES_PORT=6455
LOCAL_DB_PATH="$ROOT_DIR"/postgres

container_exists=$(docker ps -aq -f "name=$CONTAINER_NAME")

if [ -n "$container_exists" ]; then
    container_running=$(docker ps -q -f "name=$CONTAINER_NAME")
    
    if [ -n "$container_running" ]; then
        echo "The PostgreSQL container is already running."
    else
        echo "The PostgreSQL container exists but is stopped. Restarting..."
        docker start $CONTAINER_NAME
    fi
else
    echo "Starting the PostgreSQL container..."
    docker run --name $CONTAINER_NAME \
        -e POSTGRES_DB=$DB_NAME \
        -e POSTGRES_USER=$DB_USER \
        -e POSTGRES_PASSWORD=$DB_PASSWORD \
        -p $POSTGRES_PORT:5432 \
        -v $LOCAL_DB_PATH:/work \
        -w /work \
        -d postgres
fi

echo "PostgreSQL container is up and running on port $POSTGRES_PORT."

