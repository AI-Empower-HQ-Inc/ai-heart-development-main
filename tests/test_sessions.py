# import pytest  # Only needed if you use pytest-specific features or run tests directly with pytest
from datetime import datetime
from backend.models.database import db, Session

def test_create_session(client, auth_header):
    """Test creating a new meditation session."""
    response = client.post('/api/sessions', json={
        'type': 'meditation',
        'duration': 1800,  # 30 minutes
        'notes': 'Test meditation session'
    }, headers=auth_header)
    assert response.status_code == 201
    data = response.get_json()
    assert data['type'] == 'meditation'
    assert data['duration'] == 1800

def test_get_user_sessions(client, auth_header):
    """Test getting user's session history."""
    # Create a few sessions first
    for _ in range(3):
        client.post('/api/sessions', json={
            'type': 'meditation',
            'duration': 1800,
            'notes': 'Test session'
        }, headers=auth_header)
    
    response = client.get('/api/sessions', headers=auth_header)
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) >= 3

def test_get_session_stats(client, auth_header):
    """Test getting user's session statistics."""
    # Create sessions with different types
    sessions = [
        {'type': 'meditation', 'duration': 1800},
        {'type': 'yoga', 'duration': 3600},
        {'type': 'meditation', 'duration': 2400}
    ]
    
    for session in sessions:
        client.post('/api/sessions', json=session, headers=auth_header)
    
    response = client.get('/api/sessions/stats', headers=auth_header)
    assert response.status_code == 200
    data = response.get_json()
    assert 'total_duration' in data
    assert 'session_count' in data
    assert data['session_count'] >= 3

def test_update_session(client, auth_header):
    """Test updating a session."""
    # Create a session
    response = client.post('/api/sessions', json={
        'type': 'meditation',
        'duration': 1800,
        'notes': 'Original notes'
    }, headers=auth_header)
    
    session_id = response.get_json()['id']
    
    # Update the session
    response = client.put(f'/api/sessions/{session_id}', json={
        'notes': 'Updated notes'
    }, headers=auth_header)
    assert response.status_code == 200
    data = response.get_json()
    assert data['notes'] == 'Updated notes'
