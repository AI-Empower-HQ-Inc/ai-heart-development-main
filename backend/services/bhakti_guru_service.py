from typing import Dict, Any
from backend.config.config import Config
from backend.models.database import SpiritualSession, db

try:
    import openai
except ImportError:
    raise ImportError(
        "The 'openai' package is required for BhaktiGuruService. "
        "Install it with 'pip install openai'."
    )

class BhaktiGuruService:
    def __init__(self):
        self.name = "💝 AI Bhakti Guru"
        self.specialization = "Devotion and divine love"
        
    def get_response(self, question: str, user_id: str = None) -> Dict[str, Any]:
        """Get a response from Bhakti Guru for the given question."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are the AI Bhakti Guru, focused on devotion, surrender, and gratitude. Guide users in developing divine love and emotional purification through devotional practices."},
                    {"role": "user", "content": question}
                ],
                max_tokens=800,
                temperature=0.7
            )
            
            answer = response.choices[0].message.content
            
            # Store the interaction in database if user_id provided
            if user_id:
                session = SpiritualSession(
                    user_id=user_id,
                    guru_type="bhakti",
                    question=question,
                    response=answer
                )
                db.session.add(session)
                db.session.commit()
            
            return {
                "success": True,
                "message": answer,
                "guru_name": self.name,
                "specialization": self.specialization
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_teachings(self) -> list:
        """Get core teachings of Bhakti Guru."""
        return [
            "The path of divine love and devotion",
            "Surrender and acceptance of divine will",
            "Cultivation of spiritual gratitude",
            "Emotional purification through bhakti",
            "Service with love and dedication"
        ]
