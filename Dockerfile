# Build frontend - Spiritual Guidance Platform
FROM node:18-alpine as frontend-build
WORKDIR /frontend
COPY package*.json ./
RUN npm ci
COPY src/ ./src/
COPY static/ ./static/
COPY templates/ ./templates/
RUN npm run build

# Build backend - Spiritual Guidance API
FROM python:3.12-slim as backend

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./backend/
COPY tests/ ./tests/

# Copy frontend build
COPY --from=frontend-build /frontend/dist/ ./static/

# Environment setup
ENV PYTHONPATH=/app
ENV FLASK_APP=backend/main.py
ENV FLASK_ENV=production
ENV PORT=5000

EXPOSE $PORT

# Run with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "backend.main:create_app()"]
