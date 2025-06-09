from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/durable/webhook', methods=['POST'])
def durable_webhook():
    """Handle Durable website builder webhooks"""
    data = request.get_json()
    # Process Durable requests and return spiritual guidance
    return jsonify({"status": "success", "guru_response": "Spiritual wisdom delivered!"})

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
