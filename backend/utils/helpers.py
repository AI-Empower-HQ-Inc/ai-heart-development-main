import hashlib
import secrets
from datetime import datetime
from typing import Dict, Any
import re

def generate_session_id() -> str:
    """Generate secure session ID"""
    return secrets.token_urlsafe(32)

def hash_string(text: str) -> str:
    """Hash string using SHA256"""
    return hashlib.sha256(text.encode()).hexdigest()

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def sanitize_input(text: str) -> str:
    """Sanitize user input"""
    # Remove potential harmful characters
    sanitized = re.sub(r'[<>"\']', '', text)
    return sanitized.strip()

def format_response(success: bool, data: Any = None, message: str = None, error: str = None) -> Dict:
    """Standardize API responses"""
    response = {
        'success': success,
        'timestamp': datetime.utcnow().isoformat()
    }
    
    if data is not None:
        response['data'] = data
    if message:
        response['message'] = message
    if error:
        response['error'] = error
        
    return response

def get_spiritual_level(session_count: int) -> str:
    """Determine user's spiritual level based on session count"""
    if session_count < 5:
        return 'beginner'
    elif session_count < 20:
        return 'intermediate'
    elif session_count < 50:
        return 'advanced'
    else:
        return 'master'
