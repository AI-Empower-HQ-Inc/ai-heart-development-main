"""
AI Empower Heart - Main Application
"""
import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Import heart module
from app.heart import calculate_heart_rate, classify_heart_rate

@app.route('/')
def index():
    """Render the home page."""
    return jsonify({
        "name": "AI Empower Heart",
        "status": "running",
        "api_version": "1.0.0"
    })

@app.route('/api/heart-rate/<int:beats>/<float:minutes>')
def heart_rate_api(beats, minutes):
    """Calculate and classify heart rate."""
    try:
        bpm = calculate_heart_rate(beats, minutes)
        classification = classify_heart_rate(bpm)
        return jsonify({
            "beats": beats,
            "minutes": minutes,
            "heart_rate": bpm,
            "classification": classification
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
