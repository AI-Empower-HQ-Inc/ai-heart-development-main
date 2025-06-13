from typing import Dict, Any
import openai
from backend.config.config import Config
from backend.models.database import SpiritualSession, db

class BojanGuruService:
    def __init__(self):
        self.name = "🌟 AI Bojan Guru"
        self.specialization = "Transformative spiritual coaching and self-realization"
        
    def get_response(self, question: str, user_id: str = None) -> Dict[str, Any]:
        """Get a response from Bojan Guru for the given question."""
        try:
            # Create ChatGPT prompt
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Using GPT-4 for deeper spiritual insights
                messages=[
                    {
                        "role": "system",
                        "content": """You are AI Bojan Guru, a transformative spiritual coach combining ancient wisdom 
                        with modern understanding. Your approach is direct, practical, and deeply transformative. 
                        You help people discover their true spiritual nature and integrate wisdom into daily life."""
                    },
                    {"role": "user", "content": question}
                ],
                temperature=0.7,
                max_tokens=800
            )
            
            # Extract the response
            guru_response = response.choices[0].message.content
            
            # Store the session if user_id is provided
            if user_id:
                session = SpiritualSession(
                    user_id=user_id,
                    guru_type='bojan',
                    question=question,
                    response=guru_response
                )
                db.session.add(session)
                db.session.commit()
            
            return {
                "success": True,
                "response": guru_response,
                "guru_name": self.name
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "guru_name": self.name
            }
            
    def get_teachings(self) -> list:
        """Get core teachings of Bojan Guru."""
        return [
            "Direct realization of your true nature",
            "Integration of spiritual wisdom in daily life",
            "Breaking through mental barriers",
            "Accessing higher consciousness",
            "Practical spiritual transformation"
        ]
