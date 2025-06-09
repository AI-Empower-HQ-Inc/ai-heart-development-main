from flask import Flask
import os
from slokas_database import get_daily_sloka

app = Flask(__name__)

@app.route('/')
def index():
    sloka = get_daily_sloka()
    
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>AI Sloka Guru</title>
    <style>
        body {{ font-family: Arial; background: #f0f8ff; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        .sloka-box {{ background: white; padding: 20px; margin: 20px 0; border-radius: 10px; }}
        .sanskrit {{ font-size: 18px; color: #8B4513; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🕉️ AI Sloka Guru</h1>
        <p>Spiritual Intelligence Revolution</p>
        
        <div class="sloka-box">
            <h2>Today's Sacred Wisdom</h2>
            <div class="sanskrit">{sloka["sanskrit"]}</div>
            <p><strong>Translation:</strong> {sloka["translation"]}</p>
            <p><strong>Meaning:</strong> {sloka["meaning"]}</p>
        </div>
        
        <div class="sloka-box">
            <h2>Ask the Sloka Guru</h2>
            <p>Your spiritual AI assistant is ready! 🙏</p>
            <p>This is the foundation of your AI Empower Heart platform.</p>
        </div>
    </div>
</body>
</html>
"""
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
