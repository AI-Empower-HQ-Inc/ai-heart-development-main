import json
import random
from datetime import datetime
from typing import Dict, List, Any

class SpiritualService:
    def __init__(self):
        self.core_teachings = {
            "sat_chit_ananda": {
                "sat": "Eternal existence, the ultimate truth",
                "chit": "Pure consciousness, awareness of the self",
                "ananda": "Divine bliss, the state of ultimate joy"
            },
            "soul_body": {
                "soul": "The eternal, conscious entity (Atman)",
                "body": "The temporary physical vessel",
                "mind": "The bridge between soul and body"
            },
            "mukti_paths": [
                "Self-realization through meditation",
                "Devotional service and surrender",
                "Knowledge and wisdom cultivation",
                "Righteous action without attachment"
            ]
        }
        
        self.wisdom_templates = {
            "soul_body_connection": """
🕉️ Divine Soul Wisdom:

The eternal question you ask about soul and body touches the very essence of spiritual understanding. Let me explain:

[Soul - आत्मा (Atma)]
• Eternal, conscious, and blissful
• Never born, never dies
• Pure awareness and witness
• Your true identity

[Body - शरीर (Sharira)]
• Temporary vessel
• Made of five elements
• Changes and eventually perishes
• Tool for spiritual growth

[The Connection Challenge]
{connection_challenge}

[The Solution Path]
{solution_path}

[Practical Steps]
{practical_steps}

Remember: You are not the body experiencing the soul; you are the soul experiencing the body. 

🙏 Reflection Question: 
{reflection_question}
""",
            "mukti_guidance": """
🕉️ Path to Mukti (Liberation):

Sat-Chit-Ananda: The Three Pillars of Ultimate Reality

1. Sat (सत्) - Eternal Existence
   • {sat_wisdom}
   
2. Chit (चित्) - Pure Consciousness
   • {chit_wisdom}
   
3. Ananda (आनंद) - Divine Bliss
   • {ananda_wisdom}

Your Journey to Liberation:
{liberation_path}

Practical Spiritual Practices:
{spiritual_practices}

🙏 Remember: 
{key_reminder}
"""
        }
    def __init__(self):
        self.slokas_database = self._load_slokas()
        self.meditation_tracks = self._load_meditation_tracks()
    
    def _load_slokas(self) -> List[Dict]:
        """Load Sanskrit slokas database"""
        return [
            {
                "id": 1,
                "sanskrit": "सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज",
                "transliteration": "sarva-dharman parityajya mam ekam saranam vraja",
                "translation": "Abandon all varieties of religion and just surrender unto Me.",
                "meaning": "This verse from Bhagavad Gita teaches complete surrender to the Divine.",
                "chapter": "Bhagavad Gita 18.66"
            },
            {
                "id": 2,
                "sanskrit": "तत्त्वमसि",
                "transliteration": "tat tvam asi",
                "translation": "Thou art That",
                "meaning": "One of the great statements declaring the identity of individual soul with Universal consciousness.",
                "chapter": "Chandogya Upanishad"
            }
        ]
    
    def _load_meditation_tracks(self) -> List[Dict]:
        """Load meditation guidance tracks"""
        return [
            {
                "id": 1,
                "title": "Breath Awareness Meditation",
                "duration": "10 minutes",
                "type": "breathing",
                "guidance": "Focus on the natural flow of breath..."
            },
            {
                "id": 2,
                "title": "Loving Kindness Meditation",
                "duration": "15 minutes", 
                "type": "bhakti",
                "guidance": "Cultivate unconditional love and compassion..."
            }
        ]
    
    def get_daily_sloka(self) -> Dict[str, Any]:
        """Get today's sloka"""
        sloka = random.choice(self.slokas_database)
        return {
            "success": True,
            "sloka": sloka,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
    
    def get_meditation_by_type(self, meditation_type: str) -> Dict[str, Any]:
        """Get meditation by type"""
        meditations = [m for m in self.meditation_tracks if m["type"] == meditation_type]
        if meditations:
            return {"success": True, "meditation": random.choice(meditations)}
        return {"success": False, "error": "Meditation type not found"}
    
    def get_spiritual_quote(self) -> Dict[str, Any]:
        """Get inspirational spiritual quote"""
        quotes = [
            "The mind is everything. What you think you become. - Buddha",
            "Be yourself; everyone else is already taken. - Oscar Wilde",
            "The only way to do great work is to love what you do. - Steve Jobs"
        ]
        return {
            "success": True,
            "quote": random.choice(quotes),
            "timestamp": datetime.now().isoformat()
        }
    
    def get_spiritual_guidance(self, question):
        if "soul" in question.lower() and "body" in question.lower():
            return self._generate_soul_body_wisdom()
        elif "mukti" in question.lower() or "liberation" in question.lower():
            return self._generate_mukti_wisdom()
        else:
            return self._generate_general_wisdom(question)

    def _generate_soul_body_wisdom(self):
        connection_challenges = [
            "The main challenge is our identification with the body and mind, forgetting our true spiritual nature.",
            "Our attachment to physical sensations and mental constructs creates the illusion of separation.",
            "The veil of Maya (illusion) makes us forget our true spiritual identity."
        ]
        
        solution_paths = [
            "Regular meditation to experience your conscious essence beyond the body",
            "Practicing witness consciousness - observing thoughts and sensations without attachment",
            "Understanding that you are the eternal observer, not the temporary observed"
        ]
        
        practical_steps = [
            "1. Start each day with 10 minutes of silent observation of your breath",
            "2. Practice being the witness of your thoughts rather than being lost in them",
            "3. Regular study of spiritual wisdom texts",
            "4. Cultivate awareness of being consciousness itself"
        ]
        
        reflection_questions = [
            "When you are in deep sleep, who is aware of that peace?",
            "If you are not the body, then who is the one observing these thoughts?",
            "Can the observed (body) be the same as the observer (consciousness)?"
        ]
        
        return self.wisdom_templates["soul_body_connection"].format(
            connection_challenge="\n".join(connection_challenges),
            solution_path="\n".join(solution_paths),
            practical_steps="\n".join(practical_steps),
            reflection_question=random.choice(reflection_questions)
        )

    def _generate_mukti_wisdom(self):
        sat_wisdom = [
            "Understanding your eternal nature beyond birth and death",
            "Recognizing the unchanging witness consciousness within",
            "Realizing your true existence beyond time and space"
        ]
        
        chit_wisdom = [
            "Experiencing pure awareness without thought modification",
            "Being the knower of all thoughts and experiences",
            "Recognizing consciousness as your fundamental nature"
        ]
        
        ananda_wisdom = [
            "Discovering joy that needs no external cause",
            "Experiencing the bliss of pure being",
            "Finding fulfillment in your own true nature"
        ]
        
        liberation_paths = [
            "1. Regular meditation and self-inquiry",
            "2. Cultivating witness consciousness",
            "3. Practice of detachment from temporary phenomena",
            "4. Understanding your true nature through wisdom teachings"
        ]
        
        practices = [
            "• Daily meditation on 'Who am I?'",
            "• Practice of mindfulness in daily activities",
            "• Study of sacred texts with contemplation",
            "• Service with detachment from results"
        ]
        
        reminders = [
            "You are already That which you seek. The journey is about removing what covers this truth.",
            "Liberation is not becoming something new, but recognizing what you eternally are.",
            "Your true nature is Sat-Chit-Ananda - existence, consciousness, and bliss absolute."
        ]
        
        return self.wisdom_templates["mukti_guidance"].format(
            sat_wisdom="\n   • ".join(sat_wisdom),
            chit_wisdom="\n   • ".join(chit_wisdom),
            ananda_wisdom="\n   • ".join(ananda_wisdom),
            liberation_path="\n".join(liberation_paths),
            spiritual_practices="\n".join(practices),
            key_reminder=random.choice(reminders)
        )
