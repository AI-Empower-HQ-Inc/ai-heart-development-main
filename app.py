"""
AI Empower Heart - Main Application
"""
import os
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Import heart module
from app.heart import calculate_heart_rate, classify_heart_rate

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Render the dashboard page."""
    # Placeholder for dashboard data
    sample_data = {
        'heart_rate': 75,
        'classification': 'normal',
        'daily_average': 72,
        'weekly_trend': 'stable'
    }
    return render_template('dashboard.html', data=sample_data)

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

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

@app.route('/api/health')
def health_check():
    """API health check endpoint."""
    return jsonify({
        "status": "healthy",
        "version": "1.0.0"
    })

if __name__ == '__main__':
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
