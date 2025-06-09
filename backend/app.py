from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'spiritual-wisdom-key')
app.config['DEBUG'] = True

# Import API routes
from api.gurus import gurus_bp
from api.users import users_bp
from api.sessions import sessions_bp

# Register blueprints
app.register_blueprint(gurus_bp, url_prefix='/api/gurus')
app.register_blueprint(users_bp, url_prefix='/api/users') 
app.register_blueprint(sessions_bp, url_prefix='/api/sessions')

@app.route('/')
def home():
    return jsonify({
        'message': 'AI Empower Heart 360 API',
        'version': '1.0.0',
        'status': 'active',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'service': 'ai-empower-heart'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
