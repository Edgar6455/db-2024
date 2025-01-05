#!/bin/bash

if [[ "$(id -u)" -ne 0 ]]; then
    echo "This script requires sudo privileges for system package installation."
    exit 1
fi

ROOT_DIR=$(dirname "$(dirname "$(realpath "$0")")")
VENV_DIR="${ROOT_DIR}/venv"

cd "$ROOT_DIR" || exit

echo "Installing required system packages..."
apt update -y
apt install -y python3 pip python3.11-venv libpq-dev

echo "Creating virtual environment in $VENV_DIR..."
python3 -m venv "$VENV_DIR"

echo "Activating the virtual environment..."
source "$VENV_DIR/bin/activate"

echo "Installing dependencies..."
pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy alembic psycopg2 requests faker

echo "Setup complete. Virtual environment created and dependencies installed."
echo "To activate the virtual environment later, run: source $VENV_DIR/bin/activate"

