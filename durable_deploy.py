# Durable-optimized version of AI Empower Heart
from flask import Flask, render_template_string, request, jsonify
import openai
import os

app = Flask(__name__)

# Durable-compatible configuration
app.config['ENV'] = 'production'
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Your complete 6-Guru system (same as before)
AI_GURUS = {
    "sloka": {"name": "🕉️ AI Sloka Guru", "prompt": "You are the AI Sloka Guru..."},
    "spiritual": {"name": "🙏 AI Spiritual Guru", "prompt": "You are the AI Spiritual Guru..."},
    "meditation": {"name": "🧘 AI Meditation Guru", "prompt": "You are the AI Meditation Guru..."},
    "bhakti": {"name": "💝 AI Bhakti Guru", "prompt": "You are the AI Bhakti Guru..."},
    "karma": {"name": "⚖️ AI Karma Guru", "prompt": "You are the AI Karma Guru..."},
    "yoga": {"name": "🕉️ AI Yoga Guru", "prompt": "You are the AI Yoga Guru..."}
}

@app.route('/')
def index():
    return "AI Empower Heart - Ready for Durable!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
