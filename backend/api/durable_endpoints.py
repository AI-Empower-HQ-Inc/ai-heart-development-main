from flask import Blueprint, request, jsonify, redirect, url_for, current_app
from flask_cors import cross_origin
from services.simple_ai_service import SimpleAIService
from services.sloka_guru_service import SlokaGuruService
from services.spiritual_service import SpiritualService
from models.database import db, UserSession
import json
from datetime import datetime
from backend.models.database import db, UserSession
from datetime import datetime

durable_bp = Blueprint('durable', __name__)
simple_ai = SimpleAIService()
sloka_guru = SlokaGuruService()
spiritual_service = SpiritualService()

@durable_bp.route('/api/spiritual-guidance', methods=['POST'])
@cross_origin(origins=['https://empowerhub360.org', 'https://www.empowerhub360.org'])
def get_spiritual_guidance():
    """Main endpoint for the Durable widget to get spiritual guidance"""
    try:
        data = request.json
        guru_type = data.get('guru')
        question = data.get('question')
        language = data.get('language', 'english')
        
        if not guru_type or not question:
            return jsonify({
                'success': False,
                'message': 'Both guru type and question are required'
            }), 400
            
        # Create an anonymous session
        session = UserSession(
            session_type=guru_type,
            notes=question,
            start_time=datetime.utcnow()
        )
        db.session.add(session)
        db.session.commit()
        
        # Get guidance based on guru type
        response = None
        if guru_type == 'sloka':
            response = sloka_guru.get_guidance(question, language=language)
        elif guru_type == 'spiritual':
            response = spiritual_service.get_guidance(question, language=language)
        else:
            response = simple_ai.get_response(question, guru_type, language)
            
        return jsonify({
            'success': True,
            'guru_name': f'AI {guru_type.title()} Guru',
            'response': response,
            'session_id': session.id
        })
        
    except Exception as e:
        current_app.logger.error(f"Error in spiritual guidance: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Internal server error'
        }), 500
        
@durable_bp.route('/api/save-reflection', methods=['POST'])
@cross_origin(origins=['https://empowerhub360.org', 'https://www.empowerhub360.org'])
def save_reflection():
    """Save user's reflection after receiving guidance"""
    try:
        data = request.json
        session_id = data.get('session_id')
        reflection = data.get('reflection')
        
        if not session_id or not reflection:
            return jsonify({
                'success': False,
                'message': 'Both session_id and reflection are required'
            }), 400
            
        session = UserSession.query.get(session_id)
        if not session:
            return jsonify({
                'success': False,
                'message': 'Session not found'
            }), 404
            
        session.reflection = reflection
        session.end_time = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Reflection saved successfully'
        })
        
    except Exception as e:
        current_app.logger.error(f"Error saving reflection: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Internal server error'
        }), 500
