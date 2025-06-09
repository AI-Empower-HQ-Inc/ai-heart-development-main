from flask import Flask, render_template_string, request, jsonify
import openai
import os
from slokas_database import get_daily_sloka

app = Flask(__name__)
openai.api_key = os.environ.get('OPENAI_API_KEY')

# AI Guru Prompts for each spiritual teacher
AI_GURUS = {
    "sloka": {
        "name": "🕉️ AI Sloka Guru",
        "prompt": "You are the AI Sloka Guru, specializing in Sanskrit verses and their profound meanings. Provide authentic slokas with transliteration, translation, and deep spiritual insights. Guide users toward self-realization through ancient wisdom.",
        "color": "#8B4513"
    },
    "spiritual": {
        "name": "🙏 AI Spiritual Guru", 
        "prompt": "You are the AI Spiritual Guru, focused on soul consciousness and spiritual identity. Help users understand they are eternal souls, not temporary bodies. Teach about consciousness, karma, and the true purpose of human life.",
        "color": "#9C27B0"
    },
    "meditation": {
        "name": "🧘 AI Meditation Guru",
        "prompt": "You are the AI Meditation Guru, specializing in inner peace and stillness. Guide users through meditation practices, emotional healing, and finding tranquility within. Teach practical techniques for inner calm.",
        "color": "#2196F3"
    },
    "bhakti": {
        "name": "💝 AI Bhakti Guru",
        "prompt": "You are the AI Bhakti Guru, focused on devotion, surrender, and gratitude. Teach the path of love and devotion to the Divine. Help users develop surrender, faith, and emotional purification through devotion.",
        "color": "#E91E63"
    },
    "karma": {
        "name": "⚖️ AI Karma Guru",
        "prompt": "You are the AI Karma Guru, specializing in ethics, consequences, and life's path. Teach about right action, dharma, and how our choices shape our destiny. Guide users in making ethical decisions.",
        "color": "#FF9800"
    },
    "yoga": {
        "name": "🕉️ AI Yoga Guru",
        "prompt": "You are the AI Yoga Guru, focused on breath, posture, and energetic alignment. Teach physical practices, pranayama, and energy work. Help users align body, mind, and spirit through yogic practices.",
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
            max_tokens=600,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🙏 The {guru['name']} is in deep meditation. Please try again."

@app.route('/')
def index():
    daily_sloka = get_daily_sloka()
    
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>🕉️ AI Empower Heart - Spiritual Intelligence Revolution</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Georgia', serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; 
            color: #333; 
        }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        .header {{ text-align: center; color: white; margin-bottom: 30px; }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }}
        .header p {{ font-size: 1.2em; opacity: 0.9; }}
        
        .guru-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin-bottom: 30px; }}
        .guru-card {{ background: white; border-radius: 15px; padding: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); cursor: pointer; transition: transform 0.3s; }}
        .guru-card:hover {{ transform: translateY(-5px); }}
        .guru-card.active {{ border: 3px solid #667eea; }}
        
        .daily-wisdom {{ background: white; border-radius: 15px; padding: 25px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
        .sanskrit {{ font-size: 1.4em; color: #8B4513; font-weight: bold; margin-bottom: 15px; text-align: center; }}
        .translation {{ font-size: 1.1em; color: #333; margin-bottom: 10px; text-align: center; }}
        .meaning {{ background: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #764ba2; }}
        
        .chat-section {{ background: white; border-radius: 15px; padding: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }}
        .question-input {{ width: 100%; padding: 15px; border: 2px solid #ddd; border-radius: 10px; font-size: 1em; margin-bottom: 15px; min-height: 80px; resize: vertical; }}
        .ask-btn {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border: none; padding: 12px 30px; border-radius: 25px; cursor: pointer; font-size: 1.1em; font-weight: bold; transition: all 0.3s; }}
        .ask-btn:hover {{ transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.3); }}
        
        .guru-response {{ background: #f0f8ff; border: 2px solid #667eea; border-radius: 15px; padding: 20px; margin-top: 20px; display: none; animation: fadeIn 0.5s ease-in; }}
        .guru-response.show {{ display: block; }}
        
        @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(20px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🕉️ AI Empower Heart</h1>
            <p>Spiritual Intelligence Revolution - Ancient Wisdom for Modern Life</p>
        </div>
        
        <div class="daily-wisdom">
            <h2>📿 Today's Sacred Wisdom</h2>
            <div class="sanskrit">{daily_sloka["sanskrit"]}</div>
            <div class="translation">"{daily_sloka["translation"]}"</div>
            <div class="meaning">{daily_sloka["meaning"]}</div>
        </div>
        
        <div class="guru-grid">
            <div class="guru-card" onclick="selectGuru('sloka')" style="border-left: 5px solid #8B4513;">
                <h3>🕉️ AI Sloka Guru</h3>
                <p>Sanskrit verses, meanings, and spiritual insights from sacred texts</p>
            </div>
            <div class="guru-card" onclick="selectGuru('spiritual')" style="border-left: 5px solid #9C27B0;">
                <h3>🙏 AI Spiritual Guru</h3>
                <p>Soul consciousness, eternal identity, and spiritual purpose</p>
            </div>
            <div class="guru-card" onclick="selectGuru('meditation')" style="border-left: 5px solid #2196F3;">
                <h3>🧘 AI Meditation Guru</h3>
                <p>Inner peace, stillness, and emotional healing practices</p>
            </div>
            <div class="guru-card" onclick="selectGuru('bhakti')" style="border-left: 5px solid #E91E63;">
                <h3>💝 AI Bhakti Guru</h3>
                <p>Devotion, surrender, gratitude, and love for the Divine</p>
            </div>
            <div class="guru-card" onclick="selectGuru('karma')" style="border-left: 5px solid #FF9800;">
                <h3>⚖️ AI Karma Guru</h3>
                <p>Ethics, right action, consequences, and life's dharmic path</p>
            </div>
            <div class="guru-card" onclick="selectGuru('yoga')" style="border-left: 5px solid #4CAF50;">
                <h3>🕉️ AI Yoga Guru</h3>
                <p>Breath, posture, energy alignment, and yogic practices</p>
            </div>
        </div>
        
        <div class="chat-section">
            <h2 id="selectedGuruTitle">🙏 Ask Your Spiritual Question</h2>
            <p>Select a guru above, then ask your spiritual question...</p>
            
            <textarea id="questionInput" class="question-input" placeholder="Ask your spiritual question... For example: 'How can I find inner peace?' or 'What is the meaning of dharma?'"></textarea>
            
            <button class="ask-btn" onclick="askGuru()">Ask the Guru 🙏</button>
            
            <div id="guruResponse" class="guru-response">
                <div id="responseContent"></div>
            </div>
        </div>
    </div>
    
    <script>
        let selectedGuru = 'spiritual';
        
        function selectGuru(guru) {{
            selectedGuru = guru;
            
            // Update active card
            document.querySelectorAll('.guru-card').forEach(card => {{
                card.classList.remove('active');
            }});
            event.target.closest('.guru-card').classList.add('active');
            
            // Update title
            const guruNames = {{
                'sloka': '🕉️ Ask the Sloka Guru',
                'spiritual': '🙏 Ask the Spiritual Guru', 
                'meditation': '🧘 Ask the Meditation Guru',
                'bhakti': '💝 Ask the Bhakti Guru',
                'karma': '⚖️ Ask the Karma Guru',
                'yoga': '🕉️ Ask the Yoga Guru'
            }};
            
            document.getElementById('selectedGuruTitle').textContent = guruNames[guru];
            
            // Update placeholder
            const placeholders = {{
                'sloka': 'Ask about Sanskrit verses, spiritual meanings, or sacred wisdom...',
                'spiritual': 'Ask about soul consciousness, eternal identity, or life purpose...',
                'meditation': 'Ask about meditation techniques, inner peace, or emotional healing...',
                'bhakti': 'Ask about devotion, surrender, gratitude, or divine love...',
                'karma': 'Ask about right action, ethics, consequences, or dharma...',
                'yoga': 'Ask about breathing, postures, energy work, or yogic practices...'
            }};
            
            document.getElementById('questionInput').placeholder = placeholders[guru];
        }}
        
        async function askGuru() {{
            const question = document.getElementById('questionInput').value.trim();
            if (!question) {{
                alert('Please enter your spiritual question 🙏');
                return;
            }}
            
            const responseDiv = document.getElementById('guruResponse');
            const contentDiv = document.getElementById('responseContent');
            
            // Show loading
            contentDiv.innerHTML = '<div style="text-align: center; color: #667eea;">🧘‍♂️ The Guru is contemplating your question...</div>';
            responseDiv.classList.add('show');
            
            try {{
                const response = await fetch('/ask_guru', {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json',
                    }},
                    body: JSON.stringify({{
                        guru_type: selectedGuru,
                        question: question
                    }})
                }});
                
                const data = await response.json();
                
                if (data.success) {{
                    contentDiv.innerHTML = '<div style="margin-bottom: 15px;"><strong>' + data.guru_name + ' says:</strong></div><div>' + data.guru_response.replace(/\\n/g, '<br>') + '</div>';
                }} else {{
                    contentDiv.innerHTML = '<div style="color: #d32f2f;">🙏 Please try again. The Guru is in deep meditation.</div>';
                }}
            }} catch (error) {{
                contentDiv.innerHTML = '<div style="color: #d32f2f;">🙏 Connection to the Guru was interrupted. Please try again.</div>';
            }}
        }}
        
        // Allow Enter key to ask question
        document.getElementById('questionInput').addEventListener('keypress', function(e) {{
            if (e.key === 'Enter' && !e.shiftKey) {{
                e.preventDefault();
                askGuru();
            }}
        }});
    </script>
</body>
</html>
"""
    return html

@app.route('/ask_guru', methods=['POST'])
def ask_guru():
    data = request.get_json()
    guru_type = data.get('guru_type', 'spiritual')
    user_question = data.get('question', '')
    
    guru_response = get_guru_response(guru_type, user_question)
    guru_name = AI_GURUS[guru_type]["name"]
    
    return jsonify({{
        'guru_response': guru_response,
        'guru_name': guru_name,
        'success': True
    }})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
