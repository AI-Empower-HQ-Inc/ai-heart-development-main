#!/bin/bash

# Install requirements
echo "Installing requirements..."
pip install -r backend/requirements.txt

# Start the Flask application
echo "Starting Flask application..."
python backend/app.py
