import pytest
from backend.api.gurus import AI_GURUS

def test_get_gurus_list(client):
    """Test getting the list of available gurus."""
    response = client.get('/api/gurus')
    assert response.status_code == 200
    data = response.get_json()
    assert all(guru in data for guru in AI_GURUS.keys())

def test_get_guru_response(client):
    """Test getting a response from a specific guru."""
    test_data = {
        'message': 'Tell me about karma yoga',
        'guru_type': 'karma'
    }
    response = client.post('/api/gurus/chat', json=test_data)
    assert response.status_code == 200
    data = response.get_json()
    assert 'response' in data

def test_invalid_guru_type(client):
    """Test request with invalid guru type."""
    test_data = {
        'message': 'Hello',
        'guru_type': 'invalid_guru'
    }
    response = client.post('/api/gurus/chat', json=test_data)
    assert response.status_code == 400

@pytest.mark.parametrize('guru_type', list(AI_GURUS.keys()))
def test_all_guru_types(client, guru_type):
    """Test each guru type responds correctly."""
    test_data = {
        'message': 'Tell me your purpose',
        'guru_type': guru_type
    }
    response = client.post('/api/gurus/chat', json=test_data)
    assert response.status_code == 200
    data = response.get_json()
    assert 'response' in data
