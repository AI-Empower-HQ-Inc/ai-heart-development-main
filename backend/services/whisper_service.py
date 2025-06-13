"""
OpenAI Whisper Service for AI Gurus Content Creation
====================================================

This service provides audio transcription, content creation, and voice processing
capabilities for the AI Gurus spiritual platform using OpenAI Whisper.
"""

import os
import whisper
import torch
import tempfile
from pathlib import Path
from typing import Dict, Any, List, Optional, Union
import json
from datetime import datetime
import asyncio
from flask import current_app
import logging

class WhisperContentCreationService:
    """
    Advanced Whisper service for spiritual content creation and transcription
    """
    
    def __init__(self):
        """Initialize the Whisper service with optimal configuration"""
        
        # Load Whisper model
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_size = "base"  # Options: tiny, base, small, medium, large
        
        print(f"🎙️ Initializing Whisper model '{self.model_size}' on device: {self.device}")
        self.model = whisper.load_model(self.model_size, device=self.device)
        
        # Supported audio formats
        self.supported_formats = [
            '.mp3', '.wav', '.m4a', '.ogg', '.flac', '.aac'
        ]
        
        # Content creation templates for different spiritual contexts
        self.content_templates = {
            "meditation_guide": {
                "prompt": "Transform this meditation guidance into a structured meditation script",
                "format": "guided_meditation",
                "processing": "enhance_pauses"
            },
            "spiritual_teaching": {
                "prompt": "Convert this spiritual teaching into a structured lesson format",
                "format": "teaching_content",
                "processing": "add_wisdom_insights"
            },
            "sloka_recitation": {
                "prompt": "Transcribe this Sanskrit recitation with transliteration and meaning",
                "format": "sanskrit_content",
                "processing": "sanskrit_enhancement"
            },
            "prayer_chanting": {
                "prompt": "Transcribe this prayer or chanting with spiritual context",
                "format": "devotional_content",
                "processing": "devotional_enhancement"
            },
            "dharma_talk": {
                "prompt": "Transform this dharma talk into structured spiritual content",
                "format": "dharma_content",
                "processing": "ethical_enhancement"
            }
        }
        
        # Upload directory for audio files
        self.upload_dir = Path("uploads/audio")
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        
        # Transcription output directory
        self.transcription_dir = Path("transcriptions")
        self.transcription_dir.mkdir(parents=True, exist_ok=True)
        
        logging.info("✅ Whisper Content Creation Service initialized successfully")
    
    async def transcribe_audio(
        self, 
        audio_file_path: str, 
        content_type: str = "general",
        language: Optional[str] = None,
        include_timestamps: bool = True
    ) -> Dict[str, Any]:
        """
        Transcribe audio file with content-specific processing
        
        Args:
            audio_file_path: Path to audio file
            content_type: Type of spiritual content (meditation_guide, spiritual_teaching, etc.)
            language: Language code (auto-detect if None)
            include_timestamps: Whether to include word-level timestamps
            
        Returns:
            Dict containing transcription and metadata
        """
        try:
            print(f"🎙️ Starting transcription for: {Path(audio_file_path).name}")
            print(f"📝 Content type: {content_type}")
            
            # Validate file exists and format
            if not os.path.exists(audio_file_path):
                raise FileNotFoundError(f"Audio file not found: {audio_file_path}")
            
            file_ext = Path(audio_file_path).suffix.lower()
            if file_ext not in self.supported_formats:
                raise ValueError(f"Unsupported audio format: {file_ext}")
            
            # Transcribe with Whisper
            result = self.model.transcribe(
                audio_file_path,
                language=language,
                word_timestamps=include_timestamps,
                verbose=True
            )
            
            # Process based on content type
            processed_content = await self._process_transcription(
                result, content_type, audio_file_path
            )
            
            # Save transcription
            transcription_file = await self._save_transcription(
                processed_content, audio_file_path, content_type
            )
            
            return {
                "success": True,
                "transcription": {
                    "text": result["text"],
                    "language": result["language"],
                    "segments": result.get("segments", []),
                    "words": result.get("words", []) if include_timestamps else []
                },
                "processed_content": processed_content,
                "content_type": content_type,
                "audio_duration": self._get_audio_duration(result),
                "transcription_file": str(transcription_file),
                "timestamp": datetime.utcnow().isoformat(),
                "model_used": self.model_size,
                "device_used": self.device
            }
            
        except Exception as e:
            logging.error(f"❌ Transcription failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }
    
    async def _process_transcription(
        self, 
        whisper_result: Dict, 
        content_type: str, 
        audio_file_path: str
    ) -> Dict[str, Any]:
        """Process transcription based on content type"""
        
        template = self.content_templates.get(content_type, self.content_templates["spiritual_teaching"])
        text = whisper_result["text"]
        
        processed = {
            "raw_text": text,
            "content_type": content_type,
            "processing_applied": template["processing"]
        }
        
        # Apply content-specific processing
        if content_type == "meditation_guide":
            processed.update(await self._process_meditation_guide(text, whisper_result))
        elif content_type == "spiritual_teaching":
            processed.update(await self._process_spiritual_teaching(text, whisper_result))
        elif content_type == "sloka_recitation":
            processed.update(await self._process_sloka_recitation(text, whisper_result))
        elif content_type == "prayer_chanting":
            processed.update(await self._process_prayer_chanting(text, whisper_result))
        elif content_type == "dharma_talk":
            processed.update(await self._process_dharma_talk(text, whisper_result))
        else:
            processed.update(await self._process_general_content(text, whisper_result))
        
        return processed
    
    async def _process_meditation_guide(self, text: str, result: Dict) -> Dict[str, Any]:
        """Process meditation guidance content"""
        
        # Extract meditation phases
        segments = result.get("segments", [])
        meditation_phases = []
        
        current_phase = {"type": "preparation", "text": "", "duration": 0, "start_time": 0}
        
        for segment in segments:
            segment_text = segment["text"].lower()
            
            # Detect phase transitions
            if any(word in segment_text for word in ["breathe", "breathing", "breath"]):
                if current_phase["type"] != "breathing":
                    meditation_phases.append(current_phase.copy())
                    current_phase = {
                        "type": "breathing", 
                        "text": segment["text"], 
                        "duration": segment["end"] - segment["start"],
                        "start_time": segment["start"]
                    }
            elif any(word in segment_text for word in ["relax", "release", "let go"]):
                if current_phase["type"] != "relaxation":
                    meditation_phases.append(current_phase.copy())
                    current_phase = {
                        "type": "relaxation",
                        "text": segment["text"],
                        "duration": segment["end"] - segment["start"],
                        "start_time": segment["start"]
                    }
            elif any(word in segment_text for word in ["focus", "attention", "concentrate"]):
                if current_phase["type"] != "concentration":
                    meditation_phases.append(current_phase.copy())
                    current_phase = {
                        "type": "concentration",
                        "text": segment["text"],
                        "duration": segment["end"] - segment["start"],
                        "start_time": segment["start"]
                    }
            else:
                current_phase["text"] += " " + segment["text"]
                current_phase["duration"] += segment["end"] - segment["start"]
        
        meditation_phases.append(current_phase)
        
        return {
            "meditation_phases": meditation_phases,
            "total_phases": len(meditation_phases),
            "guided_meditation_script": self._format_meditation_script(meditation_phases),
            "meditation_type": self._detect_meditation_type(text)
        }
    
    async def _process_spiritual_teaching(self, text: str, result: Dict) -> Dict[str, Any]:
        """Process spiritual teaching content"""
        
        # Extract key concepts and teachings
        segments = result.get("segments", [])
        key_concepts = []
        wisdom_quotes = []
        
        for segment in segments:
            segment_text = segment["text"]
            
            # Detect wisdom quotes (sentences with spiritual keywords)
            if any(word in segment_text.lower() for word in [
                "soul", "consciousness", "divine", "eternal", "spiritual", 
                "wisdom", "enlightenment", "awakening", "truth"
            ]):
                wisdom_quotes.append({
                    "quote": segment_text.strip(),
                    "timestamp": segment["start"],
                    "duration": segment["end"] - segment["start"]
                })
            
            # Extract concepts (nouns with spiritual context)
            concepts = self._extract_spiritual_concepts(segment_text)
            key_concepts.extend(concepts)
        
        return {
            "key_concepts": list(set(key_concepts)),
            "wisdom_quotes": wisdom_quotes[:10],  # Top 10 quotes
            "teaching_structure": self._analyze_teaching_structure(segments),
            "spiritual_themes": self._identify_spiritual_themes(text)
        }
    
    async def _process_sloka_recitation(self, text: str, result: Dict) -> Dict[str, Any]:
        """Process Sanskrit sloka recitation"""
        
        # Detect Sanskrit words and phrases
        sanskrit_segments = []
        transliteration_segments = []
        
        segments = result.get("segments", [])
        
        for segment in segments:
            segment_text = segment["text"]
            
            # Simple Sanskrit detection (contains Devanagari-like sounds)
            if self._is_likely_sanskrit(segment_text):
                sanskrit_segments.append({
                    "sanskrit": segment_text,
                    "timestamp": segment["start"],
                    "duration": segment["end"] - segment["start"]
                })
            else:
                transliteration_segments.append({
                    "transliteration": segment_text,
                    "timestamp": segment["start"],
                    "duration": segment["end"] - segment["start"]
                })
        
        return {
            "sanskrit_segments": sanskrit_segments,
            "transliteration_segments": transliteration_segments,
            "detected_slokas": self._detect_known_slokas(text),
            "pronunciation_guide": self._generate_pronunciation_guide(sanskrit_segments)
        }
    
    async def _process_prayer_chanting(self, text: str, result: Dict) -> Dict[str, Any]:
        """Process prayer and chanting content"""
        
        segments = result.get("segments", [])
        chant_patterns = []
        devotional_phrases = []
        
        for segment in segments:
            segment_text = segment["text"]
            
            # Detect repetitive patterns (chanting)
            if self._is_repetitive_pattern(segment_text):
                chant_patterns.append({
                    "pattern": segment_text,
                    "timestamp": segment["start"],
                    "repetitions": self._count_repetitions(segment_text)
                })
            
            # Detect devotional phrases
            if any(word in segment_text.lower() for word in [
                "om", "namah", "hare", "krishna", "rama", "shiva", "devi"
            ]):
                devotional_phrases.append({
                    "phrase": segment_text,
                    "timestamp": segment["start"],
                    "devotional_type": self._classify_devotional_type(segment_text)
                })
        
        return {
            "chant_patterns": chant_patterns,
            "devotional_phrases": devotional_phrases,
            "prayer_type": self._classify_prayer_type(text),
            "rhythm_analysis": self._analyze_chanting_rhythm(segments)
        }
    
    async def _process_dharma_talk(self, text: str, result: Dict) -> Dict[str, Any]:
        """Process dharma talk content"""
        
        segments = result.get("segments", [])
        ethical_points = []
        dharma_principles = []
        
        for segment in segments:
            segment_text = segment["text"]
            
            # Detect ethical discussions
            if any(word in segment_text.lower() for word in [
                "right", "wrong", "ethical", "moral", "dharma", "karma", "duty"
            ]):
                ethical_points.append({
                    "point": segment_text,
                    "timestamp": segment["start"],
                    "ethical_category": self._classify_ethical_category(segment_text)
                })
            
            # Extract dharma principles
            principles = self._extract_dharma_principles(segment_text)
            dharma_principles.extend(principles)
        
        return {
            "ethical_points": ethical_points,
            "dharma_principles": list(set(dharma_principles)),
            "talk_structure": self._analyze_dharma_talk_structure(segments),
            "practical_applications": self._extract_practical_applications(text)
        }
    
    async def _process_general_content(self, text: str, result: Dict) -> Dict[str, Any]:
        """Process general spiritual content"""
        
        return {
            "summary": text[:200] + "..." if len(text) > 200 else text,
            "word_count": len(text.split()),
            "key_topics": self._extract_key_topics(text),
            "spiritual_score": self._calculate_spiritual_content_score(text)
        }
    
    def _get_audio_duration(self, result: Dict) -> float:
        """Get audio duration from Whisper result"""
        segments = result.get("segments", [])
        if segments:
            return segments[-1]["end"]
        return 0.0
    
    async def _save_transcription(
        self, 
        content: Dict, 
        audio_file_path: str, 
        content_type: str
    ) -> Path:
        """Save transcription to file"""
        
        audio_name = Path(audio_file_path).stem
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"{audio_name}_{content_type}_{timestamp}.json"
        
        transcription_file = self.transcription_dir / filename
        
        with open(transcription_file, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        
        return transcription_file
    
    # Helper methods for content analysis
    def _format_meditation_script(self, phases: List[Dict]) -> str:
        """Format meditation phases into a guided script"""
        script_lines = []
        for i, phase in enumerate(phases):
            script_lines.append(f"Phase {i+1}: {phase['type'].title()}")
            script_lines.append(f"Duration: {phase['duration']:.1f} seconds")
            script_lines.append(f"Guidance: {phase['text']}")
            script_lines.append("")
        return "\n".join(script_lines)
    
    def _detect_meditation_type(self, text: str) -> str:
        """Detect the type of meditation from text"""
        text_lower = text.lower()
        if "breath" in text_lower:
            return "breathing_meditation"
        elif "mantra" in text_lower:
            return "mantra_meditation"
        elif "loving" in text_lower and "kindness" in text_lower:
            return "loving_kindness_meditation"
        elif "body" in text_lower and "scan" in text_lower:
            return "body_scan_meditation"
        else:
            return "general_meditation"
    
    def _extract_spiritual_concepts(self, text: str) -> List[str]:
        """Extract spiritual concepts from text"""
        spiritual_keywords = [
            "consciousness", "awareness", "enlightenment", "awakening",
            "dharma", "karma", "soul", "atman", "brahman", "moksha",
            "meditation", "mindfulness", "compassion", "wisdom"
        ]
        
        concepts = []
        text_lower = text.lower()
        for keyword in spiritual_keywords:
            if keyword in text_lower:
                concepts.append(keyword)
        
        return concepts
    
    def _analyze_teaching_structure(self, segments: List[Dict]) -> Dict[str, Any]:
        """Analyze the structure of a spiritual teaching"""
        total_segments = len(segments)
        avg_segment_length = sum(s["end"] - s["start"] for s in segments) / total_segments if total_segments > 0 else 0
        
        return {
            "total_segments": total_segments,
            "average_segment_duration": avg_segment_length,
            "teaching_flow": "structured" if avg_segment_length > 5 else "conversational"
        }
    
    def _identify_spiritual_themes(self, text: str) -> List[str]:
        """Identify spiritual themes in the text"""
        themes = []
        text_lower = text.lower()
        
        theme_keywords = {
            "meditation": ["meditat", "mindful", "awareness"],
            "devotion": ["devot", "love", "surrender", "bhakti"],
            "wisdom": ["wisdom", "knowledge", "understanding", "jnana"],
            "karma": ["karma", "action", "duty", "service"],
            "liberation": ["liberation", "freedom", "moksha", "enlightenment"]
        }
        
        for theme, keywords in theme_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                themes.append(theme)
        
        return themes
    
    def _is_likely_sanskrit(self, text: str) -> bool:
        """Simple heuristic to detect Sanskrit content"""
        sanskrit_indicators = ["om", "aum", "namah", "svaha", "mantra", "sloka"]
        return any(indicator in text.lower() for indicator in sanskrit_indicators)
    
    def _detect_known_slokas(self, text: str) -> List[str]:
        """Detect known Sanskrit slokas"""
        # This would be expanded with a database of known slokas
        known_slokas = [
            "Om Gam Ganapataye Namaha",
            "Gayatri Mantra",
            "Maha Mantra"
        ]
        
        detected = []
        text_lower = text.lower()
        for sloka in known_slokas:
            if sloka.lower() in text_lower:
                detected.append(sloka)
        
        return detected
    
    def _generate_pronunciation_guide(self, sanskrit_segments: List[Dict]) -> List[Dict]:
        """Generate pronunciation guide for Sanskrit"""
        # Simplified pronunciation guide
        guides = []
        for segment in sanskrit_segments:
            guides.append({
                "sanskrit": segment["sanskrit"],
                "pronunciation": segment["sanskrit"],  # Would be enhanced with actual pronunciation
                "timestamp": segment["timestamp"]
            })
        return guides
    
    def _is_repetitive_pattern(self, text: str) -> bool:
        """Detect if text contains repetitive patterns (chanting)"""
        words = text.split()
        if len(words) < 2:
            return False
        
        # Simple repetition detection
        unique_words = set(words)
        repetition_ratio = len(words) / len(unique_words)
        return repetition_ratio > 2
    
    def _count_repetitions(self, text: str) -> int:
        """Count repetitions in text"""
        words = text.split()
        if not words:
            return 0
        
        most_common_word = max(set(words), key=words.count)
        return words.count(most_common_word)
    
    def _classify_devotional_type(self, text: str) -> str:
        """Classify type of devotional content"""
        text_lower = text.lower()
        if "krishna" in text_lower or "hare" in text_lower:
            return "vaishnava"
        elif "shiva" in text_lower or "om namah" in text_lower:
            return "shaiva"
        elif "devi" in text_lower or "shakti" in text_lower:
            return "shakta"
        else:
            return "general"
    
    def _classify_prayer_type(self, text: str) -> str:
        """Classify type of prayer"""
        text_lower = text.lower()
        if "gratitude" in text_lower or "thank" in text_lower:
            return "gratitude_prayer"
        elif "help" in text_lower or "guidance" in text_lower:
            return "petition_prayer"
        elif "peace" in text_lower or "harmony" in text_lower:
            return "peace_prayer"
        else:
            return "general_prayer"
    
    def _analyze_chanting_rhythm(self, segments: List[Dict]) -> Dict[str, Any]:
        """Analyze rhythm of chanting"""
        if not segments:
            return {"rhythm": "none"}
        
        durations = [s["end"] - s["start"] for s in segments]
        avg_duration = sum(durations) / len(durations)
        duration_variance = sum((d - avg_duration) ** 2 for d in durations) / len(durations)
        
        rhythm_type = "steady" if duration_variance < 0.5 else "varied"
        
        return {
            "rhythm": rhythm_type,
            "average_segment_duration": avg_duration,
            "rhythm_variance": duration_variance
        }
    
    def _classify_ethical_category(self, text: str) -> str:
        """Classify ethical category"""
        text_lower = text.lower()
        if "truth" in text_lower or "honesty" in text_lower:
            return "truthfulness"
        elif "compassion" in text_lower or "kindness" in text_lower:
            return "compassion"
        elif "non-violence" in text_lower or "ahimsa" in text_lower:
            return "non_violence"
        else:
            return "general_ethics"
    
    def _extract_dharma_principles(self, text: str) -> List[str]:
        """Extract dharma principles from text"""
        principles = []
        text_lower = text.lower()
        
        dharma_concepts = [
            "right action", "right speech", "right livelihood",
            "truthfulness", "non-violence", "compassion",
            "selfless service", "detachment"
        ]
        
        for concept in dharma_concepts:
            if concept in text_lower:
                principles.append(concept)
        
        return principles
    
    def _analyze_dharma_talk_structure(self, segments: List[Dict]) -> Dict[str, Any]:
        """Analyze structure of dharma talk"""
        return {
            "total_segments": len(segments),
            "talk_style": "formal" if len(segments) > 20 else "informal",
            "estimated_talk_duration": segments[-1]["end"] if segments else 0
        }
    
    def _extract_practical_applications(self, text: str) -> List[str]:
        """Extract practical applications from dharma talk"""
        applications = []
        text_lower = text.lower()
        
        practical_keywords = [
            "practice", "apply", "daily life", "meditation",
            "mindfulness", "compassion practice", "service"
        ]
        
        sentences = text.split('.')
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in practical_keywords):
                applications.append(sentence.strip())
        
        return applications[:5]  # Top 5 applications
    
    def _extract_key_topics(self, text: str) -> List[str]:
        """Extract key topics from text"""
        # Simple keyword extraction - would be enhanced with NLP
        spiritual_topics = [
            "meditation", "mindfulness", "compassion", "wisdom",
            "dharma", "karma", "consciousness", "enlightenment"
        ]
        
        topics = []
        text_lower = text.lower()
        for topic in spiritual_topics:
            if topic in text_lower:
                topics.append(topic)
        
        return topics
    
    def _calculate_spiritual_content_score(self, text: str) -> float:
        """Calculate spiritual content score (0-1)"""
        spiritual_words = [
            "spiritual", "divine", "sacred", "holy", "blessed",
            "meditation", "prayer", "consciousness", "soul",
            "dharma", "karma", "enlightenment", "awakening"
        ]
        
        text_words = text.lower().split()
        spiritual_word_count = sum(1 for word in text_words if word in spiritual_words)
        
        if not text_words:
            return 0.0
        
        return min(spiritual_word_count / len(text_words) * 10, 1.0)

# Initialize global instance
whisper_service = None

def get_whisper_service() -> WhisperContentCreationService:
    """Get or create Whisper service instance"""
    global whisper_service
    if whisper_service is None:
        whisper_service = WhisperContentCreationService()
    return whisper_service
