import json
import random
from datetime import datetime
from typing import Dict, List, Any

class SpiritualService:
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
