from flask import Blueprint, request, jsonify
import openai
import os

gurus_bp = Blueprint('gurus', __name__)

# Spiritual Gurus Configuration
SPIRITUAL_GURUS = {
    "spiritual": {
        "name": "🙏 AI Spiritual Guru",
        "specialization": "Soul consciousness and eternal identity",
        "prompt": "You are a wise spiritual teacher focused on soul consciousness and eternal identity..."
    },
    "sloka": {
        "name": "🕉️ AI Sloka Guru", 
        "specialization": "Sanskrit verses and sacred wisdom",
        "prompt": "You are a Sanskrit scholar specializing in ancient verses and their meanings..."
    },
    "meditation": {
        "name": "🧘 AI Meditation Guru",
        "specialization": "Inner peace and mindfulness",
        "prompt": "You are a meditation master teaching inner peace and mindfulness..."
    },
    "bhakti": {
        "name": "💝 AI Bhakti Guru",
        "specialization": "Devotion and divine love", 
        "prompt": "You are a devotion teacher focused on divine love and surrender..."
    },
    "karma": {
        "name": "⚖️ AI Karma Guru",
        "specialization": "Ethics and dharma",
        "prompt": "You are an ethics teacher focused on dharma and right action..."
    },
    "yoga": {
        "name": "🧘‍♀️ AI Yoga Guru",
        "specialization": "Breath and energy alignment",
        "prompt": "You are a yoga master teaching breath, posture, and energy work..."
    }
}

@gurus_bp.route('/', methods=['GET'])
def get_all_gurus():
    return jsonify({
        'success': True,
        'gurus': SPIRITUAL_GURUS,
        'total': len(SPIRITUAL_GURUS)
    })

@gurus_bp.route('/<guru_type>', methods=['GET'])
def get_guru(guru_type):
    if guru_type in SPIRITUAL_GURUS:
        return jsonify({
            'success': True,
            'guru': SPIRITUAL_GURUS[guru_type]
        })
    return jsonify({'success': False, 'error': 'Guru not found'}), 404

@gurus_bp.route('/ask', methods=['POST'])
def ask_guru():
    data = request.get_json()
    guru_type = data.get('guru_type')
    question = data.get('question')
    
    if not guru_type or not question:
        return jsonify({'success': False, 'error': 'Missing guru_type or question'}), 400
    
    if guru_type not in SPIRITUAL_GURUS:
        return jsonify({'success': False, 'error': 'Invalid guru type'}), 400
    
    try:
        # AI Response (placeholder for now)
        response = f"This is wisdom from {SPIRITUAL_GURUS[guru_type]['name']} about: {question}"
        
        return jsonify({
            'success': True,
            'guru_name': SPIRITUAL_GURUS[guru_type]['name'],
            'guru_type': guru_type,
            'question': question,
            'response': response,
            'specialization': SPIRITUAL_GURUS[guru_type]['specialization']
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
