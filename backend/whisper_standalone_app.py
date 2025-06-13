#!/usr/bin/env python3
"""
Standalone Whisper Flask App for Testing
========================================

Simple Flask app to test OpenAI Whisper content creation functionality
without dependencies on other services.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import sys
import asyncio
from pathlib import Path
import tempfile
from werkzeug.utils import secure_filename

# Check for API key
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("❌ OPENAI_API_KEY environment variable is not set")
    sys.exit(1)

app = Flask(__name__)
CORS(app)

# Import Whisper service
from services.whisper_service import WhisperContentCreationService

# Initialize Whisper service
print("🎙️ Initializing Whisper service...")
whisper_service = WhisperContentCreationService()
print("✅ Whisper service ready!")

# Configuration
ALLOWED_EXTENSIONS = {'.mp3', '.wav', '.m4a', '.ogg', '.flac', '.aac'}
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25MB

def allowed_file(filename):
    """Check if file extension is allowed"""
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS

@app.route('/api/whisper/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'OpenAI Whisper Content Creation',
        'model': whisper_service.model_size,
        'device': whisper_service.device,
        'supported_formats': list(whisper_service.supported_formats),
        'max_file_size_mb': MAX_FILE_SIZE // (1024 * 1024),
        'version': '1.0.0'
    })

@app.route('/api/whisper/content-types', methods=['GET'])
def get_content_types():
    """Get available content types"""
    content_types = []
    for content_type, template in whisper_service.content_templates.items():
        content_types.append({
            'name': content_type,
            'display_name': content_type.replace('_', ' ').title(),
            'format': template['format'],
            'processing': template['processing'],
            'description': template['prompt']
        })
    
    return jsonify({
        'success': True,
        'content_types': content_types,
        'total_types': len(content_types)
    })

@app.route('/api/whisper/supported-formats', methods=['GET'])
def get_supported_formats():
    """Get supported audio formats"""
    formats = []
    format_descriptions = {
        '.mp3': 'MPEG Audio Layer 3 - Most common audio format',
        '.wav': 'Waveform Audio File - Uncompressed high quality',
        '.m4a': 'MPEG-4 Audio - iTunes/Apple format',
        '.ogg': 'Ogg Vorbis - Open source audio format',
        '.flac': 'Free Lossless Audio Codec - High quality lossless',
        '.aac': 'Advanced Audio Coding - Modern compressed format'
    }
    
    for ext in ALLOWED_EXTENSIONS:
        formats.append({
            'extension': ext,
            'description': format_descriptions.get(ext, 'Supported audio format')
        })
    
    return jsonify({
        'success': True,
        'formats': formats,
        'max_file_size': f"{MAX_FILE_SIZE // (1024 * 1024)}MB"
    })

@app.route('/api/whisper/transcribe', methods=['POST'])
def transcribe_audio():
    """Transcribe uploaded audio file"""
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
                'error': f'Unsupported file format. Supported: {", ".join(ALLOWED_EXTENSIONS)}'
            }), 400
        
        # Get parameters
        content_type = request.form.get('content_type', 'spiritual_teaching')
        language = request.form.get('language', None)
        include_timestamps = request.form.get('include_timestamps', 'true').lower() == 'true'
        
        # Save uploaded file temporarily
        filename = secure_filename(file.filename)
        temp_dir = Path("temp_uploads")
        temp_dir.mkdir(exist_ok=True)
        
        temp_file_path = temp_dir / filename
        file.save(str(temp_file_path))
        
        try:
            # Transcribe with Whisper
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(
                whisper_service.transcribe_audio(
                    str(temp_file_path),
                    content_type=content_type,
                    language=language,
                    include_timestamps=include_timestamps
                )
            )
            loop.close()
            
            # Clean up temp file
            temp_file_path.unlink()
            
            return jsonify(result)
            
        except Exception as e:
            # Clean up temp file on error
            if temp_file_path.exists():
                temp_file_path.unlink()
            raise e
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }), 500

@app.route('/api/whisper/create-content', methods=['POST'])
def create_content():
    """Create enhanced spiritual content from text"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'error': 'Text content is required'
            }), 400
        
        text = data['text']
        content_type = data.get('content_type', 'spiritual_teaching')
        enhancement_level = data.get('enhancement_level', 'standard')
        
        # Process text content
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # Create a mock whisper result for text processing
        mock_result = {
            'text': text,
            'language': 'en',
            'segments': [],
            'words': []
        }
        
        processed_content = loop.run_until_complete(
            whisper_service._process_transcription(
                mock_result, content_type, "text_input"
            )
        )
        loop.close()
        
        return jsonify({
            'success': True,
            'original_text': text,
            'content_type': content_type,
            'enhancement_level': enhancement_level,
            'processed_content': processed_content
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'error_type': type(e).__name__
        }), 500

@app.route('/api/whisper/transcriptions', methods=['GET'])
def list_transcriptions():
    """List recent transcriptions"""
    try:
        transcription_dir = Path("transcriptions")
        if not transcription_dir.exists():
            return jsonify({
                'success': True,
                'transcriptions': [],
                'total': 0
            })
        
        transcriptions = []
        for file_path in transcription_dir.glob("*.json"):
            transcriptions.append({
                'filename': file_path.name,
                'created': file_path.stat().st_mtime,
                'size_bytes': file_path.stat().st_size
            })
        
        # Sort by creation time (most recent first)
        transcriptions.sort(key=lambda x: x['created'], reverse=True)
        
        return jsonify({
            'success': True,
            'transcriptions': transcriptions[:20],  # Return latest 20
            'total': len(transcriptions)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/', methods=['GET'])
def index():
    """Root endpoint with API documentation"""
    return jsonify({
        'service': 'OpenAI Whisper Content Creation API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': {
            'health': 'GET /api/whisper/health',
            'content_types': 'GET /api/whisper/content-types',
            'supported_formats': 'GET /api/whisper/supported-formats', 
            'transcribe': 'POST /api/whisper/transcribe',
            'create_content': 'POST /api/whisper/create-content',
            'transcriptions': 'GET /api/whisper/transcriptions'
        },
        'documentation': 'Upload audio files for spiritual content transcription and enhancement'
    })

@app.route('/demo', methods=['GET'])
def demo():
    """Serve the demo HTML interface"""
    try:
        with open('whisper_demo.html', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Demo HTML file not found", 404

if __name__ == '__main__':
    print("🎙️ Starting Whisper Content Creation API...")
    print("📡 Server will be available at: http://localhost:5001")
    print("📚 API Documentation: http://localhost:5001")
    print("🔗 Health Check: http://localhost:5001/api/whisper/health")
    
    app.run(host='0.0.0.0', port=5001, debug=True)
