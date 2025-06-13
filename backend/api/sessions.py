from flask import Blueprint, request, jsonify
from models.database import db, UserSession
from datetime import datetime

sessions_bp = Blueprint('sessions', __name__)

@sessions_bp.route('/start', methods=['POST'])
def start_session():
    try:
        data = request.json
        user_id = data.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'message': 'User ID is required'}), 400
            
        session = UserSession(
            user_id=user_id,
            session_type=data.get('type', 'meditation'),
            duration=data.get('duration', 0),
            notes=data.get('notes', ''),
            start_time=datetime.utcnow(),
            status='active'
        )
        
        db.session.add(session)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'session_id': session.id,
            'type': session.session_type,
            'duration': session.duration,
            'message': f'Started {session.session_type} session'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@sessions_bp.route('/history', methods=['GET'])
def get_session_history():
    try:
        user_id = request.args.get('user_id')
        if not user_id:
            return jsonify({'success': False, 'message': 'User ID is required'}), 400
            
        sessions = UserSession.query.filter_by(user_id=user_id).order_by(UserSession.start_time.desc()).all()
        
        session_list = [{
            'id': session.id,
            'type': session.session_type,
            'duration': session.duration,
            'start_time': session.start_time.isoformat(),
            'end_time': session.end_time.isoformat() if session.end_time else None,
            'notes': session.notes,
            'reflection': session.reflection,
            'real_life_application': session.real_life_application,
            'status': session.status
        } for session in sessions]
        
        return jsonify({
            'success': True,
            'sessions': session_list,
            'message': 'Spiritual session history retrieved'
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@sessions_bp.route('/user_session', methods=['POST'])
def create_user_session():
    data = request.json
    session = UserSession(
        user_id=data['user_id'],
        duration_minutes=data['duration_minutes'],
        meditation_type=data['meditation_type'],
        voice_guide=data.get('voice_guide'),
        background_audio=data.get('background_audio'),
        started_at=datetime.fromisoformat(data['started_at']) if data.get('started_at') else datetime.utcnow(),
        webcam_recording_url=data.get('webcam_recording_url')
    )
    db.session.add(session)
    db.session.commit()
    return jsonify({'success': True, 'session_id': session.session_id})

@sessions_bp.route('/user_session/<session_id>/end', methods=['POST'])
def end_user_session(session_id):
    session = UserSession.query.get(session_id)
    if not session:
        return jsonify({'success': False, 'error': 'Session not found'}), 404
    session.ended_at = datetime.fromisoformat(request.json.get('ended_at')) if request.json.get('ended_at') else datetime.utcnow()
    db.session.commit()
    return jsonify({'success': True})

@sessions_bp.route('/user_session/<session_id>/reflect', methods=['POST'])
def reflect_on_session(session_id):
    session = UserSession.query.get(session_id)
    if not session:
        return jsonify({'success': False, 'error': 'Session not found'}), 404
    session.reflection = request.json.get('reflection', '')
    session.applied_in_life = request.json.get('applied_in_life', False)
    db.session.commit()
    return jsonify({'success': True})

@sessions_bp.route('/user_session/<user_id>/history', methods=['GET'])
def get_user_session_history(user_id):
    sessions = UserSession.query.filter_by(user_id=user_id).order_by(UserSession.started_at.desc()).all()
    return jsonify({'success': True, 'sessions': [s.to_dict() for s in sessions]})

@sessions_bp.route('/reflect', methods=['POST'])
def add_reflection():
    try:
        data = request.json
        session_id = data.get('session_id')
        if not session_id:
            return jsonify({'success': False, 'message': 'Session ID is required'}), 400
            
        session = UserSession.query.get(session_id)
        if not session:
            return jsonify({'success': False, 'message': 'Session not found'}), 404
            
        session.reflection = data.get('reflection', '')
        session.real_life_application = data.get('real_life_application', '')
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Reflection added successfully',
            'session': {
                'id': session.id,
                'reflection': session.reflection,
                'real_life_application': session.real_life_application
            }
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@sessions_bp.route('/end', methods=['POST'])
def end_session():
    try:
        data = request.json
        session_id = data.get('session_id')
        if not session_id:
            return jsonify({'success': False, 'message': 'Session ID is required'}), 400
            
        session = UserSession.query.get(session_id)
        if not session:
            return jsonify({'success': False, 'message': 'Session not found'}), 404
            
        session.end_time = datetime.utcnow()
        session.status = 'completed'
        session.duration = data.get('duration', session.duration)
        session.notes = data.get('notes', session.notes)
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Session completed successfully',
            'session': {
                'id': session.id,
                'duration': session.duration,
                'notes': session.notes
            }
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500

@sessions_bp.route('/reflection-prompts', methods=['GET'])
def get_reflection_prompts():
    session_type = request.args.get('type', 'meditation')
    
    prompts = {
        'meditation': [
            "What emotions or sensations arose during your meditation?",
            "What insights or realizations did you experience?",
            "How can you apply this meditation's lessons in your daily life?",
            "What obstacles or distractions did you notice? How did you work with them?",
            "How has this practice shifted your perspective or state of being?"
        ],
        'yoga': [
            "How did your body feel during and after the practice?",
            "What connection did you notice between breath and movement?",
            "What lessons from your practice can you take into your day?",
            "How did this practice affect your energy and mental state?",
            "What aspects of the practice challenged or surprised you?"
        ]
    }
    
    return jsonify({
        'success': True,
        'prompts': prompts.get(session_type, prompts['meditation']),
        'message': f'Reflection prompts for {session_type}'
    })
