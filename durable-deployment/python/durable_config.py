"""
Durable configuration for AI Empower Heart
"""

DURABLE_CONFIG = {
    'site_url': 'https://empowerhub360.org',
    'api_url': 'https://api.empowerhub360.org',
    'webhook_secret': '',  # Set this in production
    'allowed_origins': [
        'https://empowerhub360.org',
        'https://www.empowerhub360.org',
        'https://api.empowerhub360.org'
    ]
}

# Durable widget configuration
WIDGET_CONFIG = {
    'position': 'bottom-right',
    'theme': 'light',
    'primary_color': '#667eea',
    'secondary_color': '#764ba2',
    'font_family': 'Arial, sans-serif'
}

# API rate limiting
RATE_LIMIT = {
    'requests_per_minute': 60,
    'burst': 10
}
