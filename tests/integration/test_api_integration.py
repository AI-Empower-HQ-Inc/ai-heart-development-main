import requests
from backend.config.config import Config

class TestAPIIntegration:
    base_url = f"http://localhost:{Config.PORT}"
    
    def test_guru_chat_flow(self):
        """Test the complete flow of chatting with different gurus."""
        # Register a test user
        register_response = requests.post(
            f"{self.base_url}/api/users/register",
            json={
                "username": "testuser",
                "email": "test@example.com",
                "password": "testpass123"
            }
        )
        assert register_response.status_code == 201
        
        # Login to get token
        login_response = requests.post(
            f"{self.base_url}/api/users/login",
            json={
                "email": "test@example.com",
                "password": "testpass123"
            }
        )
        assert login_response.status_code == 200
        token = login_response.json()["token"]
        headers = {"Authorization": f"Bearer {token}"}
        
        # Test chat with different gurus
        gurus = ["karma", "bhakti", "meditation", "yoga", "spiritual", "sloka"]
        for guru in gurus:
            chat_response = requests.post(
                f"{self.base_url}/api/gurus/chat",
                headers=headers,
                json={
                    "guru_type": guru,
                    "message": "What is your teaching?"
                }
            )
            assert chat_response.status_code == 200
            assert "response" in chat_response.json()
            
        # Create and retrieve a session
        session_response = requests.post(
            f"{self.base_url}/api/sessions",
            headers=headers,
            json={
                "type": "meditation",
                "duration": 1800,
                "notes": "Integration test session"
            }
        )
        assert session_response.status_code == 201
        
        # Get session history
        history_response = requests.get(
            f"{self.base_url}/api/sessions",
            headers=headers
        )
        assert history_response.status_code == 200
        assert len(history_response.json()) > 0
        assert len(history_response.json()) > 0
