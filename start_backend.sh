#!/bin/bash

echo "🚀 Setting up AI Empower Heart Backend..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python 3.8 or higher"
    exit 1
fi

echo "🚀 Starting AI Empower Heart Backend..."

# Set environment variables
export FLASK_ENV=development
export OPENAI_API_KEY="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"

# Install dependencies
cd backend
pip3 install -r requirements.txt

# Start the application
python3 main.py
