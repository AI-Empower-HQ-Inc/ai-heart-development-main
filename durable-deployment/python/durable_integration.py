from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from functools import wraps
import requests
import hmac
import hashlib
import time
from .durable_config import DURABLE_CONFIG, WIDGET_CONFIG, RATE_LIMIT

app = Flask(__name__)
CORS(app)

def verify_durable_webhook(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not DURABLE_CONFIG['webhook_secret']:
            return f(*args, **kwargs)
            
        signature = request.headers.get('X-Durable-Signature')
        if not signature:
            abort(401, description="No signature provided")
            
        # Verify webhook signature
        expected = hmac.new(
            DURABLE_CONFIG['webhook_secret'].encode(),
            request.data,
            hashlib.sha256
        ).hexdigest()
        
        if not hmac.compare_digest(signature, expected):
            abort(401, description="Invalid signature")
            
        return f(*args, **kwargs)
    return decorated_function

@app.route('/durable/webhook', methods=['POST'])
@verify_durable_webhook
def durable_webhook():
    """Handle Durable website builder webhooks"""
    data = request.get_json()
    timestamp = data.get('timestamp', time.time())
    
    # Process Durable requests and return spiritual guidance
    return jsonify({
        "status": "success",
        "timestamp": timestamp,
        "guru_response": "Spiritual wisdom delivered!"
    })

@app.route('/api/spiritual-guidance', methods=['POST'])
def spiritual_api():
    """API endpoint for Durable websites to get spiritual guidance"""
    question = request.json.get('question', '')
    guru_type = request.json.get('guru', 'spiritual')
    
    # Return AI Guru response
    return jsonify({
        "guru": guru_type,
        "response": f"Spiritual guidance for: {question}",
        "platform": "AI Empower Heart"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
