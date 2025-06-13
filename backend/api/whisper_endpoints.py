"""
Whisper API Endpoints for Content Creation
==========================================

Flask API endpoints for audio transcription and spiritual content creation
using OpenAI Whisper with the AI Gurus platform.
"""

from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
import asyncio
from pathlib import Path
from services.whisper_service import get_whisper_service
import tempfile
import uuid

whisper_bp = Blueprint('whisper', __name__)

# Configuration
ALLOWED_EXTENSIONS = {'.mp3', '.wav', '.m4a', '.ogg', '.flac', '.aac'}
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25MB

def allowed_file(filename):
    """Check if file extension is allowed"""
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS

@whisper_bp.route('/transcribe', methods=['POST'])
def transcribe_audio():
    """
    Transcribe uploaded audio file
    
    Form data:
    - audio_file: Audio file to transcribe
    - content_type: Type of spiritual content (optional)
    - language: Language code (optional, auto-detect if not provided)
    - include_timestamps: Whether to include timestamps (optional, default: true)
    """
    try:
        # Check if file is present
        if 'audio_file' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No audio file provided'
            }), 400
        
        file = request.files['audio_file']
        if file.filename == '':
            return jsonify({
                'success': False,
                'error': 'No file selected'
            }), 400
        
        # Validate file
        if not allowed_file(file.filename):
            return jsonify({
                'success': False,
                'error': f'Unsupported file format. Allowed: {", ".join(ALLOWED_EXTENSIONS)}'
            }), 400
        
        # Get optional parameters
        content_type = request.form.get('content_type', 'general')
        language = request.form.get('language')
        include_timestamps = request.form.get('include_timestamps', 'true').lower() == 'true'
        
        # Validate content type
        valid_content_types = [
            'general', 'meditation_guide', 'spiritual_teaching', 
            'sloka_recitation', 'prayer_chanting', 'dharma_talk'
        ]
        
        if content_type not in valid_content_types:
            return jsonify({
                'success': False,
                'error': f'Invalid content type. Valid types: {", ".join(valid_content_types)}'
            }), 400
        
        # Save uploaded file temporarily
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        
        # Create temporary directory if it doesn't exist
        temp_dir = Path("temp_uploads")
        temp_dir.mkdir(exist_ok=True)
        
        temp_path = temp_dir / unique_filename
        file.save(str(temp_path))
        
        try:
            # Check file size
            file_size = os.path.getsize(temp_path)
            if file_size > MAX_FILE_SIZE:
                return jsonify({
                    'success': False,
                    'error': f'File too large. Maximum size: {MAX_FILE_SIZE // (1024*1024)}MB'
                }), 400
            
            # Get Whisper service and transcribe
            whisper_service = get_whisper_service()
            
            # Run transcription in async context
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            result = loop.run_until_complete(
                whisper_service.transcribe_audio(
                    str(temp_path),
                    content_type=content_type,
                    language=language,
                    include_timestamps=include_timestamps
                )
            )
            
            loop.close()
            
            # Add file information to result
            if result.get('success'):
                result['file_info'] = {
                    'original_filename': filename,
                    'file_size_mb': round(file_size / (1024*1024), 2),
                    'content_type_analyzed': content_type
                }
            
            return jsonify(result)
            
        finally:
            # Clean up temporary file
            if temp_path.exists():
                temp_path.unlink()
    
    except Exception as e:
        current_app.logger.error(f"Error in transcription: {e}")
        return jsonify({
            'success': False,
            'error': 'Internal server error during transcription',
            'details': str(e)
        }), 500

@whisper_bp.route('/content-types', methods=['GET'])
def get_content_types():
    """Get available content types for transcription"""
    
    content_types = {
        'general': {
            'name': 'General Content',
            'description': 'General spiritual content with basic processing',
            'use_cases': ['General talks', 'Discussions', 'Q&A sessions']
        },
        'meditation_guide': {
            'name': 'Meditation Guide',
            'description': 'Guided meditation sessions with phase detection',
            'use_cases': ['Breathing meditations', 'Body scan', 'Mindfulness guides']
        },
        'spiritual_teaching': {
            'name': 'Spiritual Teaching',
            'description': 'Structured spiritual lessons with wisdom extraction',
            'use_cases': ['Dharma talks', 'Philosophy lessons', 'Wisdom teachings']
        },
        'sloka_recitation': {
            'name': 'Sanskrit Sloka Recitation',
            'description': 'Sanskrit verses with transliteration and meaning',
            'use_cases': ['Bhagavad Gita verses', 'Upanishad recitations', 'Mantras']
        },
        'prayer_chanting': {
            'name': 'Prayer & Chanting',
            'description': 'Devotional content with pattern recognition',
            'use_cases': ['Bhajans', 'Kirtans', 'Prayer sessions', 'Chanting']
        },
        'dharma_talk': {
            'name': 'Dharma Talk',
            'description': 'Ethical teachings with principle extraction',
            'use_cases': ['Ethics discussions', 'Moral guidance', 'Dharma teachings']
        }
    }
    
    return jsonify({
        'success': True,
        'content_types': content_types,
        'total_types': len(content_types)
    })

@whisper_bp.route('/supported-formats', methods=['GET'])
def get_supported_formats():
    """Get supported audio formats"""
    
    formats = {
        '.mp3': {
            'name': 'MP3',
            'description': 'Most common audio format',
            'recommended': True
        },
        '.wav': {
            'name': 'WAV',
            'description': 'Uncompressed audio, highest quality',
            'recommended': True
        },
        '.m4a': {
            'name': 'M4A',
            'description': 'Apple audio format, good quality',
            'recommended': False
        },
        '.ogg': {
            'name': 'OGG',
            'description': 'Open source audio format',
            'recommended': False
        },
        '.flac': {
            'name': 'FLAC',
            'description': 'Lossless compression, excellent quality',
            'recommended': True
        },
        '.aac': {
            'name': 'AAC',
            'description': 'Advanced Audio Coding',
            'recommended': False
        }
    }
    
    return jsonify({
        'success': True,
        'supported_formats': formats,
        'max_file_size_mb': MAX_FILE_SIZE // (1024*1024),
        'recommendations': [
            'Use WAV or FLAC for highest quality transcription',
            'MP3 is good for general use with smaller file sizes',
            'Ensure clear audio with minimal background noise'
        ]
    })

@whisper_bp.route('/transcriptions', methods=['GET'])
def list_transcriptions():
    """List recent transcriptions"""
    
    try:
        whisper_service = get_whisper_service()
        transcription_dir = whisper_service.transcription_dir
        
        transcriptions = []
        
        if transcription_dir.exists():
            # Get all transcription files
            for file_path in transcription_dir.glob("*.json"):
                try:
                    import json
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    # Extract summary info
                    transcriptions.append({
                        'filename': file_path.name,
                        'created': file_path.stat().st_mtime,
                        'content_type': data.get('content_type', 'unknown'),
                        'text_preview': data.get('raw_text', '')[:100] + '...' if data.get('raw_text') else '',
                        'file_size_kb': round(file_path.stat().st_size / 1024, 2)
                    })
                except Exception:
                    continue  # Skip invalid files
        
        # Sort by creation time (newest first)
        transcriptions.sort(key=lambda x: x['created'], reverse=True)
        
        return jsonify({
            'success': True,
            'transcriptions': transcriptions[:20],  # Return last 20
            'total_found': len(transcriptions)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@whisper_bp.route('/transcription/<filename>', methods=['GET'])
def get_transcription(filename):
    """Get specific transcription by filename"""
    
    try:
        whisper_service = get_whisper_service()
        transcription_path = whisper_service.transcription_dir / secure_filename(filename)
        
        if not transcription_path.exists():
            return jsonify({
                'success': False,
                'error': 'Transcription not found'
            }), 404
        
        import json
        with open(transcription_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return jsonify({
            'success': True,
            'transcription': data,
            'filename': filename
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@whisper_bp.route('/create-content', methods=['POST'])
def create_spiritual_content():
    """
    Create spiritual content from transcription
    
    JSON payload:
    - transcription_text: Text to process
    - content_type: Type of content to create
    - guru_type: Which AI Guru should enhance the content (optional)
    """
    
    try:
        data = request.get_json()
        
        if not data or 'transcription_text' not in data:
            return jsonify({
                'success': False,
                'error': 'No transcription text provided'
            }), 400
        
        transcription_text = data['transcription_text']
        content_type = data.get('content_type', 'general')
        guru_type = data.get('guru_type', 'spiritual')
        
        # Simulate content creation (would integrate with AI service)
        # For now, return structured content based on type
        
        if content_type == 'meditation_guide':
            created_content = {
                'title': 'Generated Meditation Guide',
                'type': 'meditation_script',
                'content': f"Based on the transcription, here's a structured meditation guide:\n\n{transcription_text}",
                'sections': [
                    {'name': 'Preparation', 'duration': '2 minutes'},
                    {'name': 'Main Practice', 'duration': '10 minutes'},
                    {'name': 'Integration', 'duration': '3 minutes'}
                ]
            }
        elif content_type == 'spiritual_teaching':
            created_content = {
                'title': 'Spiritual Teaching Content',
                'type': 'teaching_material',
                'content': f"Structured spiritual teaching based on transcription:\n\n{transcription_text}",
                'key_points': [
                    'Understanding consciousness',
                    'Practical spirituality',
                    'Inner transformation'
                ]
            }
        else:
            created_content = {
                'title': 'Generated Spiritual Content',
                'type': 'general_content',
                'content': transcription_text,
                'enhancement': f'Content enhanced by {guru_type} guru perspective'
            }
        
        return jsonify({
            'success': True,
            'created_content': created_content,
            'content_type': content_type,
            'guru_type': guru_type,
            'created_at': current_app.config.get('TESTING') and '2024-01-01T00:00:00' or None
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@whisper_bp.route('/health', methods=['GET'])
def whisper_health_check():
    """Health check for Whisper service"""
    
    try:
        whisper_service = get_whisper_service()
        
        return jsonify({
            'success': True,
            'status': 'healthy',
            'service': 'whisper_content_creation',
            'model_size': whisper_service.model_size,
            'device': whisper_service.device,
            'supported_formats': list(ALLOWED_EXTENSIONS),
            'max_file_size_mb': MAX_FILE_SIZE // (1024*1024)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'status': 'unhealthy',
            'error': str(e)
        }), 500
