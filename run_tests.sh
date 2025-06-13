#!/bin/bash

# Set up Python path
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Run Python tests with coverage
echo "Running Python tests..."
pytest tests/ --cov=backend --cov-report=term-missing --cov-report=html

# Run JavaScript tests
echo -e "\nRunning JavaScript tests..."
npm test

# Open coverage report if running in GUI environment
if [ -n "$DISPLAY" ]; then
    python -m webbrowser "htmlcov/index.html"
fi
