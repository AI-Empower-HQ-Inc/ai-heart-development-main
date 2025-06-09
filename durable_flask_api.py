from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS
import openai
import os
from slokas_database import get_daily_sloka

app = Flask(__name__)
CORS(app)  # Enable CORS for Durable websites to access the API

# Production configuration
app.config['ENV'] = 'production'
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Enhanced AI Gurus with detailed prompts for Durable integration
AI_GURUS = {
    "sloka": {
        "name": "🕉️ AI Sloka Guru",
        "prompt": "You are the AI Sloka Guru, specializing in Sanskrit verses from Bhagavad Gita, Upanishads, and Vedas. Provide authentic slokas with transliteration, translation, and deep spiritual meanings. Guide users toward self-realization through ancient wisdom. Always end with a reflective question.",
        "color": "#8B4513"
    },
    "spiritual": {
        "name": "🙏 AI Spiritual Guru", 
        "prompt": "You are the AI Spiritual Guru, focused on soul consciousness and eternal identity. Help users understand they are eternal souls, not temporary bodies. Teach about consciousness, karma, dharma, and the true purpose of human life. Provide profound spiritual insights.",
        "color": "#9C27B0"
    },
    "meditation": {
        "name": "🧘 AI Meditation Guru",
        "prompt": "You are the AI Meditation Guru, specializing in inner peace and stillness. Guide users through meditation techniques, emotional healing, and finding tranquility within. Teach practical methods for achieving mental clarity and inner calm.",
        "color": "#2196F3"
    },
    "bhakti": {
        "name": "💝 AI Bhakti Guru",
        "prompt": "You are the AI Bhakti Guru, focused on devotion, surrender, and gratitude. Teach the path of love and devotion to the Divine. Help users develop surrender, faith, humility, and emotional purification through devotional practices.",
        "color": "#E91E63"
    },
    "karma": {
        "name": "⚖️ AI Karma Guru",
        "prompt": "You are the AI Karma Guru, specializing in ethics, consequences, and life's dharmic path. Teach about right action, moral principles, and how our choices shape destiny. Guide users in making ethical decisions aligned with dharma.",
        "color": "#FF9800"
    },
    "yoga": {
        "name": "🕉️ AI Yoga Guru",
        "prompt": "You are the AI Yoga Guru, focused on breath, posture, and energetic alignment. Teach physical practices, pranayama, chakra work, and energy cultivation. Help users align body, mind, and spirit through authentic yogic practices.",
        "color": "#4CAF50"
    }
}

def get_guru_response(guru_type, user_question):
    """Get AI response from specific spiritual guru"""
    guru = AI_GURUS.get(guru_type, AI_GURUS["spiritual"])
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": guru["prompt"]},
                {"role": "user", "content": user_question}
            ],
            max_tokens=800,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🙏 The {guru['name']} is in deep meditation. Please try again. (Error: {str(e)})"

# API Endpoints for Durable Websites

@app.route('/')
def home():
    """API Documentation for Durable Integration"""
    docs = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Empower Heart API - Durable Integration</title>
        <style>
            body { font-family: Arial; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; }
            .container { max-width: 800px; margin: 0 auto; background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; }
            .endpoint { background: rgba(255,255,255,0.2); padding: 15px; margin: 10px 0; border-radius: 10px; }
            code { background: rgba(0,0,0,0.3); padding: 5px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🕉️ AI Empower Heart API</h1>
            <p>Spiritual Intelligence Revolution - API for Durable Websites</p>
            
            <div class="endpoint">
                <h3>POST /api/ask-guru</h3>
                <p>Get spiritual guidance from any of the 6 AI Gurus</p>
                <code>
                {
                    "guru_type": "spiritual|sloka|meditation|bhakti|karma|yoga",
                    "question": "Your spiritual question here"
                }
                </code>
            </div>
            
            <div class="endpoint">
                <h3>GET /api/daily-wisdom</h3>
                <p>Get daily Sanskrit verse with meaning</p>
            </div>
            
            <div class="endpoint">
                <h3>GET /api/gurus</h3>
                <p>List all available AI Gurus</p>
            </div>
            
            <div class="endpoint">
                <h3>POST /api/widget</h3>
                <p>Get embeddable HTML widget for Durable websites</p>
            </div>
        </div>
    </body>
    </html>
    """
    return docs

@app.route('/api/ask-guru', methods=['POST', 'OPTIONS'])
def ask_guru_api():
    """Main API endpoint for Durable websites to get spiritual guidance"""
    if request.method == 'OPTIONS':
        # Handle preflight CORS request
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response
    
    try:
        data = request.get_json()
        guru_type = data.get('guru_type', 'spiritual')
        user_question = data.get('question', '')
        
        if not user_question:
            return jsonify({
                'success': False,
                'error': 'Question is required',
                'platform': 'AI Empower Heart'
            }), 400
        
        guru_response = get_guru_response(guru_type, user_question)
        guru = AI_GURUS[guru_type]
        
        return jsonify({
            'success': True,
            'guru_name': guru['name'],
            'guru_type': guru_type,
            'guru_color': guru['color'],
            'question': user_question,
            'response': guru_response,
            'platform': 'AI Empower Heart - Spiritual Intelligence Revolution',
            'timestamp': str(os.urandom(8).hex())
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'platform': 'AI Empower Heart'
        }), 500

@app.route('/api/daily-wisdom', methods=['GET'])
def daily_wisdom_api():
    """Get daily Sanskrit wisdom for Durable websites"""
    try:
        daily_sloka = get_daily_sloka()
        return jsonify({
            'success': True,
            'daily_wisdom': daily_sloka,
            'platform': 'AI Empower Heart'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/gurus', methods=['GET'])
def gurus_list_api():
    """List all available AI Gurus for Durable integration"""
    gurus_info = {}
    for key, guru in AI_GURUS.items():
        gurus_info[key] = {
            'name': guru['name'],
            'color': guru['color'],
            'description': guru['prompt'][:100] + '...'
        }
    
    return jsonify({
        'success': True,
        'gurus': gurus_info,
        'total_gurus': len(AI_GURUS),
        'platform': 'AI Empower Heart'
    })

@app.route('/api/widget', methods=['POST'])
def durable_widget_api():
    """Generate embeddable widget HTML for Durable websites"""
    data = request.get_json() or {}
    widget_style = data.get('style', 'default')
    api_base_url = request.url_root
    
    widget_html = f"""
    <div id="ai-empower-heart-widget" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 15px; color: white; font-family: Arial;">
        <h3 style="margin-top: 0;">🕉️ AI Empower Heart - Spiritual Guidance</h3>
        
        <select id="guru-select" style="width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: none;">
            <option value="spiritual">🙏 Spiritual Guru - Soul & Consciousness</option>
            <option value="sloka">🕉️ Sloka Guru - Sanskrit Wisdom</option>
            <option value="meditation">🧘 Meditation Guru - Inner Peace</option>
            <option value="bhakti">💝 Bhakti Guru - Devotion & Love</option>
            <option value="karma">⚖️ Karma Guru - Ethics & Dharma</option>
            <option value="yoga">🕉️ Yoga Guru - Body & Energy</option>
        </select>
        
        <textarea id="spiritual-question" placeholder="Ask your spiritual question..." style="width: 100%; height: 80px; padding: 10px; margin: 10px 0; border-radius: 5px; border: none; resize: vertical;"></textarea>
        
        <button onclick="askSpiritual()" style="background: white; color: #667eea; border: none; padding: 12px 24px; border-radius: 25px; cursor: pointer; font-weight: bold;">Get Spiritual Guidance 🙏</button>
        
        <div id="spiritual-response" style="margin-top: 15px; padding: 15px; background: rgba(255,255,255,0.1); border-radius: 10px; display: none;"></div>
    </div>
    
    <script>
        async function askSpiritual() {{
            const guru = document.getElementById('guru-select').value;
            const question = document.getElementById('spiritual-question').value.trim();
            const responseDiv = document.getElementById('spiritual-response');
            
            if (!question) {{
                alert('Please enter your spiritual question 🙏');
                return;
            }}
            
            responseDiv.style.display = 'block';
            responseDiv.innerHTML = '🧘‍♂️ The Guru is contemplating your question...';
            
            try {{
                const response = await fetch('{api_base_url}api/ask-guru', {{
                    method: 'POST',
                    headers: {{'Content-Type': 'application/json'}},
                    body: JSON.stringify({{guru_type: guru, question: question}})
                }});
                
                const data = await response.json();
                
                if (data.success) {{
                    responseDiv.innerHTML = `
                        <div style="margin-bottom: 10px;"><strong>${{data.guru_name}} says:</strong></div>
                        <div style="line-height: 1.6;">${{data.response.replace(/\\n/g, '<br>')}}</div>
                    `;
                }} else {{
                    responseDiv.innerHTML = '🙏 Please try again. The Guru is in deep meditation.';
                }}
            }} catch (error) {{
                responseDiv.innerHTML = '🙏 Connection interrupted. Please try again.';
            }}
        }}
    </script>
    """
    
    return jsonify({
        'success': True,
        'widget_html': widget_html,
        'api_base_url': api_base_url,
        'usage': 'Copy the widget_html and paste it into your Durable website'
    })

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'platform': 'AI Empower Heart API',
        'version': '1.0.0',
        'gurus_available': len(AI_GURUS)
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
