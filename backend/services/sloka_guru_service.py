from typing import Dict, Any
from .simple_ai_service import SimpleAIService
from backend.models.database import SpiritualSession, User, db
from backend.models.slokas_database import get_daily_sloka

class SlokaGuruService:
    def __init__(self):
        self.name = "🕉️ AI Sloka Guru"
        self.specialization = "Universal wisdom from sacred verses"
        self.ai_service = SimpleAIService()
        
    def _understand_user_context(self, question: str) -> dict:
        """Analyze question to understand user's context and needs."""
        context = {
            "setting": "general",  # general, work, home, relationship
            "need": "wisdom",      # wisdom, peace, clarity, strength, harmony
            "time": "any"          # morning, evening, specific_situation
        }
        
        # Analyze question context
        question = question.lower()
        
        # Detect setting
        if any(word in question for word in ["work", "office", "business", "career"]):
            context["setting"] = "work"
        elif any(word in question for word in ["home", "family", "house"]):
            context["setting"] = "home"
        elif any(word in question for word in ["relationship", "partner", "friend"]):
            context["setting"] = "relationship"
            
        # Detect specific need
        if any(word in question for word in ["peace", "calm", "quiet"]):
            context["need"] = "peace"
        elif any(word in question for word in ["clear", "clarity", "confused"]):
            context["need"] = "clarity"
        elif any(word in question for word in ["strength", "courage", "confidence"]):
            context["need"] = "strength"
        elif any(word in question for word in ["harmony", "balance", "relationship"]):
            context["need"] = "harmony"
            
        # Detect time context
        if any(word in question for word in ["morning", "sunrise", "wake"]):
            context["time"] = "morning"
        elif any(word in question for word in ["evening", "night", "sleep"]):
            context["time"] = "evening"
            
        return context

    def _create_system_prompt(self) -> str:
        return """You are the AI Sloka Guru, a wise and practical spiritual guide.
        Your purpose is to make ancient wisdom relevant and practical for daily life.
        
        When sharing slokas:
        1. Make it immediately relevant to the person's situation
        2. Use simple, everyday language and examples
        3. Give clear, actionable steps they can take today
        4. Connect it to their daily experiences
        5. Provide specific applications for work, home, and relationships
        
        Key aspects to emphasize:
        - The universal consciousness (Sat-Chit-Ananda) that all traditions point to
        - How this teaching appears in various wisdom traditions
        - Practical ways to apply this wisdom in daily life
        - The unity of all spiritual paths while respecting their uniqueness
        
        Format your responses with clear sections:
        [Original Verse]
        [Translation]
        [Spiritual Essence]
        [Universal Connection]
        [Practical Application]
        """
    
    def get_user_level(self, user_id: str) -> str:
        """Determine user's spiritual learning level."""
        if not user_id:
            return "basic"
            
        try:
            # Query user from database
            user = db.session.query(User).get(user_id)
            if user and hasattr(user, 'spiritual_level'):
                # Map user levels to response levels
                level_mapping = {
                    'beginner': 'basic',
                    'intermediate': 'intermediate',
                    'advanced': 'enterprise'
                }
                return level_mapping.get(user.spiritual_level, 'basic')
        except Exception:
            pass
            
        return "basic"

    def get_user_language(self, user_id: str) -> str:
        """Determine user's preferred language."""
        if not user_id:
            return "english"
            
        try:
            # Query user from database
            user = db.session.query(User).get(user_id)
            if user and hasattr(user, 'preferred_language'):
                return user.preferred_language
        except Exception:
            pass
            
        return "english"

    def get_response(self, question: str, user_id: str = None, language: str = None) -> Dict[str, Any]:
        """Get a response from Sloka Guru for the given question."""
        try:
            # Get user's level, language preference, and context
            user_level = self.get_user_level(user_id)
            user_language = language or self.get_user_language(user_id)
            user_context = self._understand_user_context(question)
            
            # If question is about daily wisdom, include today's sloka
            if "daily" in question.lower():
                daily_sloka = get_daily_sloka()
                question = f"Please explain today's sacred verse:\n{daily_sloka['sanskrit']}\n\nQuestion: {question}"
            
            # Get response from simple AI service with appropriate level and language
            ai_response = self.ai_service.get_response(
                question, 
                level=user_level, 
                language=user_language,
                context="sloka"
            )
            response = ai_response["response"]
            
            # Store the session if user_id is provided
            if user_id:
                session = SpiritualSession(
                    user_id=user_id,
                    guru_type='sloka',
                    question=question,
                    response=response
                )
                db.session.add(session)
                db.session.commit()
            
            return {
                "success": True,
                "response": response,
                "guru_name": self.name,
                "specialization": self.specialization
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def explain_sloka(self, sloka_text: str, user_id: str = None) -> Dict[str, Any]:
        """Get a detailed explanation of a specific sloka."""
        try:
            system_prompt = self._create_system_prompt()
            
            prompt = f"""Please provide a complete analysis of this sacred verse:

{sloka_text}

Please include:
1. Word-by-word translation if applicable
2. Full verse translation
3. Deeper spiritual meaning
4. Connection to universal truth
5. Practical applications for modern life"""
            
            ai_response = self.ai_service.explain_text(sloka_text, context="sloka")
            response = ai_response["response"]
            
            if user_id:
                session = SpiritualSession(
                    user_id=user_id,
                    guru_type='sloka',
                    question=f"Explain sloka: {sloka_text}",
                    response=response
                )
                db.session.add(session)
                db.session.commit()
            
            return {
                "success": True,
                "response": response,
                "guru_name": self.name
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
