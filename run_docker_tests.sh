#!/bin/bash

echo "🧪 Running all tests in Docker..."

# Ensure we're using the latest images
docker-compose -f docker-compose.test.yml build

# Run backend tests
echo "🐍 Running Python backend tests..."
docker-compose -f docker-compose.test.yml run --rm backend-tests

# Run frontend tests
echo "🌐 Running JavaScript frontend tests..."
docker-compose -f docker-compose.test.yml run --rm frontend-tests

# Clean up
docker-compose -f docker-compose.test.yml down --volumes

echo "✅ All tests completed!"
