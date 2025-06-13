import json
import random
from pathlib import Path
from datetime import datetime

class SlokaDatabase:
    """Comprehensive Slokas Database for AI Gurus Platform"""
    
    def __init__(self):
        self.database_file = Path(__file__).parent.parent / "comprehensive_slokas_database.json"
        self.slokas_data = self._load_slokas()
        
    def _load_slokas(self):
        """Load slokas from comprehensive database"""
        try:
            with open(self.database_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Slokas database not found at {self.database_file}")
            return self._get_fallback_data()
        except Exception as e:
            print(f"Error loading slokas database: {e}")
            return self._get_fallback_data()
    
    def _get_fallback_data(self):
        """Fallback data if main database is unavailable"""
        return {
            "metadata": {"total_slokas": 1},
            "slokas": [{
                "id": "BG_2_47",
                "sanskrit": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन",
                "transliteration": "karmaṇy-evādhikāras te mā phaleṣu kadācana",
                "translation": "You have a right to perform your duty, but never to the fruits of action",
                "meaning": "Focus on your duty and effort, release attachment to outcomes",
                "source": "Bhagavad Gita Chapter 2, Verse 47",
                "category": "karma_yoga",
                "guru_assignment": "karma_guru"
            }]
        }
    
    def get_daily_sloka(self):
        """Get a random sloka for daily wisdom"""
        slokas = self.slokas_data.get("slokas", [])
        if not slokas:
            return None
        return random.choice(slokas)
    
    def get_sloka_by_id(self, sloka_id):
        """Get a specific sloka by ID"""
        slokas = self.slokas_data.get("slokas", [])
        for sloka in slokas:
            if sloka.get("id") == sloka_id:
                return sloka
        return None
    
    def get_slokas_by_category(self, category):
        """Get all slokas in a specific category"""
        slokas = self.slokas_data.get("slokas", [])
        return [sloka for sloka in slokas if sloka.get("category") == category]
    
    def get_slokas_by_guru(self, guru_name):
        """Get slokas assigned to a specific guru"""
        slokas = self.slokas_data.get("slokas", [])
        return [sloka for sloka in slokas if sloka.get("guru_assignment") == guru_name]
    
    def get_slokas_by_source(self, source):
        """Get slokas from a specific source text"""
        slokas = self.slokas_data.get("slokas", [])
        return [sloka for sloka in slokas if source.lower() in sloka.get("source", "").lower()]
    
    def search_slokas(self, search_term):
        """Search slokas by keyword in translation, meaning, or concepts"""
        slokas = self.slokas_data.get("slokas", [])
        results = []
        search_term = search_term.lower()
        
        for sloka in slokas:
            # Search in translation, meaning, and related concepts
            if (search_term in sloka.get("translation", "").lower() or
                search_term in sloka.get("meaning", "").lower() or
                any(search_term in concept.lower() for concept in sloka.get("related_concepts", []))):
                results.append(sloka)
        
        return results
    
    def get_database_stats(self):
        """Get statistics about the slokas database"""
        slokas = self.slokas_data.get("slokas", [])
        metadata = self.slokas_data.get("metadata", {})
        
        categories = {}
        gurus = {}
        sources = {}
        
        for sloka in slokas:
            # Count categories
            category = sloka.get("category", "unknown")
            categories[category] = categories.get(category, 0) + 1
            
            # Count guru assignments
            guru = sloka.get("guru_assignment", "unassigned")
            gurus[guru] = gurus.get(guru, 0) + 1
            
            # Count sources
            source = sloka.get("source", "unknown")
            sources[source] = sources.get(source, 0) + 1
        
        return {
            "total_slokas": len(slokas),
            "database_version": metadata.get("version", "1.0"),
            "categories": categories,
            "guru_assignments": gurus,
            "sources": sources,
            "available_sources": metadata.get("sources", [])
        }
    
    def get_formatted_sloka(self, sloka_id=None):
        """Get a beautifully formatted sloka for display"""
        if sloka_id:
            sloka = self.get_sloka_by_id(sloka_id)
        else:
            sloka = self.get_daily_sloka()
        
        if not sloka:
            return "No sloka available"
        
        formatted = f"""
🕉️ {sloka.get('source', 'Sacred Text')}
{'=' * 50}

Sanskrit:
{sloka.get('sanskrit', '')}

Transliteration:
{sloka.get('transliteration', '')}

Translation:
{sloka.get('translation', '')}

Meaning:
{sloka.get('meaning', '')}

Daily Application:
{sloka.get('daily_application', 'Contemplate this wisdom throughout your day.')}

Reflection Questions:
"""
        
        questions = sloka.get('reflection_questions', [])
        for i, question in enumerate(questions, 1):
            formatted += f"{i}. {question}\n"
        
        formatted += f"\nRelated Concepts: {', '.join(sloka.get('related_concepts', []))}"
        formatted += f"\nAssigned Guru: {sloka.get('guru_assignment', 'General Wisdom')}"
        
        return formatted

# Create global instance
sloka_db = SlokaDatabase()

# Legacy function for backward compatibility
def get_daily_sloka():
    """Legacy function - returns daily sloka"""
    return sloka_db.get_daily_sloka()

# Make database accessible
slokas_database = sloka_db.slokas_data
