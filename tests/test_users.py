from backend.models.database import db, User

def test_create_user(client):
    """Test user creation."""
    response = client.post('/api/users/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpass123'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['username'] == 'testuser'
    assert 'id' in data

def test_login_user(client):
    """Test user login."""
    # First create a user
    client.post('/api/users/register', json={
        'username': 'logintest',
        'email': 'login@example.com',
        'password': 'testpass123'
    })
    
    # Then try to login
    response = client.post('/api/users/login', json={
        'email': 'login@example.com',
        'password': 'testpass123'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'token' in data

def test_get_user_profile(client, auth_header):
    """Test getting user profile."""
    # Create a user first
    response = client.post('/api/users/register', json={
        'username': 'profiletest',
        'email': 'profile@example.com',
        'password': 'testpass123'
    })
    user_id = response.get_json()['id']
    
    # Get the profile
    response = client.get(f'/api/users/{user_id}', headers=auth_header)
    assert response.status_code == 200
    data = response.get_json()
    assert data['username'] == 'profiletest'

def test_invalid_login(client):
    """Test login with invalid credentials."""
    response = client.post('/api/users/login', json={
        'email': 'nonexistent@example.com',
        'password': 'wrongpass'
    })
    assert response.status_code == 401
    assert response.status_code == 401
