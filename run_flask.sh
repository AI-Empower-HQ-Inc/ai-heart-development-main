#!/bin/bash

export FLASK_APP=backend/main.py
export FLASK_ENV=development
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r backend/requirements.txt

# Run Flask application
flask run --host=0.0.0.0 --port=5000
