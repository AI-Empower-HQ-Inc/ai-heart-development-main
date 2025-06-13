#!/bin/bash

# Setup script for Durable deployment
echo "Setting up AI Empower Heart for Durable deployment..."

# Create necessary directories
mkdir -p /var/www/empowerhub360
mkdir -p /var/log/ai-empower-heart

# Install required packages
pip install -r requirements.txt

# Set environment variables
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << EOL
DURABLE_WEBHOOK_SECRET=
OPENAI_API_KEY=
FLASK_ENV=production
FLASK_APP=durable_integration.py
HOST=0.0.0.0
PORT=5000
EOL
    echo "Please edit .env file and add your secrets"
fi

# Set up SSL certificates
if [ ! -d "/etc/letsencrypt/live/api.empowerhub360.org" ]; then
    echo "Setting up SSL certificates..."
    certbot certonly --standalone -d api.empowerhub360.org
fi

# Create systemd service
cat > /etc/systemd/system/ai-empower-heart.service << EOL
[Unit]
Description=AI Empower Heart Durable Integration
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/empowerhub360
Environment=PATH=/var/www/empowerhub360/venv/bin
EnvironmentFile=/var/www/empowerhub360/.env
ExecStart=/var/www/empowerhub360/venv/bin/gunicorn --workers 4 --bind 0.0.0.0:5000 durable_integration:app
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# Start and enable the service
systemctl daemon-reload
systemctl enable ai-empower-heart
systemctl start ai-empower-heart

echo "Setup complete! Please configure your Durable site with the following:"
echo "1. Add the widget code to your Durable site"
echo "2. Set up the webhook URL: https://api.empowerhub360.org/durable/webhook"
echo "3. Configure your environment variables in .env"
