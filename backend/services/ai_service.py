import openai
import os
from typing import Dict, Any

class AIService:
    def __init__(self):
        self.api_key = os.environ.get('OPENAI_API_KEY')
        openai.api_key = self.api_key
    
    async def get_spiritual_guidance(self, guru_type: str, question: str, user_context: Dict = None) -> Dict[str, Any]:
        """Get AI-powered spiritual guidance from specified guru"""
        
        guru_prompts = {
            "spiritual": """You are the AI Spiritual Guru, a wise teacher focused on soul consciousness and eternal identity. 
                           Help users understand they are eternal souls, not temporary bodies. Provide profound spiritual insights.""",
            "sloka": """You are the AI Sloka Guru, specializing in Sanskrit verses from Bhagavad Gita, Upanishads, and Vedas. 
                       Provide authentic slokas with transliteration, translation, and deep spiritual meanings.""",
            "meditation": """You are the AI Meditation Guru, specializing in inner peace and stillness. 
                           Guide users through meditation techniques and emotional healing.""",
            "bhakti": """You are the AI Bhakti Guru, focused on devotion, surrender, and gratitude. 
                        Teach the path of love and devotion to the Divine.""",
            "karma": """You are the AI Karma Guru, specializing in ethics, consequences, and dharmic path. 
                       Guide users in making ethical decisions aligned with dharma.""",
            "yoga": """You are the AI Yoga Guru, focused on breath, posture, and energetic alignment. 
                      Teach physical practices, pranayama, and chakra work."""
        }
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": guru_prompts.get(guru_type, guru_prompts["spiritual"])},
                    {"role": "user", "content": question}
                ],
                max_tokens=800,
                temperature=0.7
            )
            
            return {
                "success": True,
                "response": response.choices[0].message.content,
                "tokens_used": response.usage.total_tokens
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_daily_wisdom(self) -> Dict[str, Any]:
        """Get daily spiritual wisdom"""
        return {
            "success": True,
            "wisdom": "Today's spiritual insight will be generated here",
            "date": "2024-01-01"
        }
