#!/bin/bash

echo "🚀 Starting AI Empower Heart Backend..."

# Activate virtual environment or create if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -r backend/requirements.txt

# Start the Flask application
echo "🌟 Starting Flask server..."
export FLASK_APP=backend/app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
