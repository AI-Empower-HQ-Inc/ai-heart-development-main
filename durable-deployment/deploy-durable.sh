#!/bin/bash

# Deploy the AI Empower Heart API to Durable
echo "Deploying AI Empower Heart to empowerhub360.org..."

# Check for required environment variables
if [ -z "$OPENAI_API_KEY" ]; then
    echo "Error: OPENAI_API_KEY environment variable is not set"
    exit 1
fi

# Set up Python virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r durable-deployment/python/requirements.txt

# Start the Flask application with Gunicorn
echo "Starting Flask application with Gunicorn..."
gunicorn --bind 0.0.0.0:8000 --workers 4 durable_flask_api:app
