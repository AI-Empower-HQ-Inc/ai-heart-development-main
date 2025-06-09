from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

# Import configurations
from config.config import config
from models.database import db
from utils.logger import app_logger

def create_app(config_name='development'):
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    CORS(app, origins=app.config['CORS_ORIGINS'])
    
    # Import and register blueprints
    from api.gurus import gurus_bp
    from api.users import users_bp  
    from api.sessions import sessions_bp
    
    app.register_blueprint(gurus_bp, url_prefix='/api/gurus')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(sessions_bp, url_prefix='/api/sessions')
    
    # Main routes
    @app.route('/')
    def home():
        return jsonify({
            'service': 'AI Empower Heart 360 Backend',
            'version': '1.0.0',
            'status': 'active',
            'endpoints': {
                'gurus': '/api/gurus',
                'users': '/api/users', 
                'sessions': '/api/sessions'
            },
            'timestamp': datetime.utcnow().isoformat()
        })
    
    @app.route('/health')
    def health():
        return jsonify({
            'status': 'healthy',
            'database': 'connected',
            'timestamp': datetime.utcnow().isoformat()
        })
    
    # Create database tables
    with app.app_context():
        db.create_all()
        app_logger.info("Database tables created successfully")
    
    app_logger.info(f"AI Empower Heart backend started in {config_name} mode")
    return app

if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_ENV', 'development'))
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
