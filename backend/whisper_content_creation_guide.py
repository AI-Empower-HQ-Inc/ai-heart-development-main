#!/usr/bin/env python3
"""
OpenAI Whisper Content Creation Guide
=====================================

Complete guide and demonstration of using OpenAI Whisper for spiritual content creation
in the AI Gurus platform.
"""

import requests
import json
from pathlib import Path
import tempfile
import wave
import numpy as np
from datetime import datetime

class WhisperContentCreationGuide:
    """Guide for using Whisper content creation system"""
    
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
        self.whisper_endpoint = f"{base_url}/api/whisper"
        
    def demo_content_creation_workflow(self):
        """Demonstrate the complete Whisper content creation workflow"""
        
        print("🎙️ WHISPER CONTENT CREATION WORKFLOW DEMO")
        print("=" * 60)
        print()
        
        # 1. Check available content types
        print("📋 STEP 1: Check Available Content Types")
        print("-" * 40)
        self.check_content_types()
        print()
        
        # 2. Check supported audio formats
        print("🎵 STEP 2: Check Supported Audio Formats")
        print("-" * 40)
        self.check_supported_formats()
        print()
        
        # 3. Create sample audio files for testing
        print("🎤 STEP 3: Create Sample Audio Content")
        print("-" * 40)
        self.create_sample_audio_content()
        print()
        
        # 4. Demonstrate API usage examples
        print("🔧 STEP 4: API Usage Examples")
        print("-" * 40)
        self.show_api_examples()
        print()
        
        # 5. Integration with AI Gurus
        print("🧘 STEP 5: AI Gurus Integration")
        print("-" * 40)
        self.show_guru_integration()
        print()
        
    def check_content_types(self):
        """Check available Whisper content types"""
        try:
            response = requests.get(f"{self.whisper_endpoint}/content-types")
            if response.status_code == 200:
                data = response.json()
                print("✅ Available Content Types:")
                for content_type in data.get('content_types', []):
                    print(f"   🎯 {content_type['name']}")
                    print(f"      Format: {content_type['format']}")
                    print(f"      Processing: {content_type['processing']}")
                    print(f"      Description: {content_type['description']}")
                    print()
            else:
                print(f"❌ Failed to get content types: {response.status_code}")
        except Exception as e:
            print(f"❌ Error checking content types: {e}")
    
    def check_supported_formats(self):
        """Check supported audio formats"""
        try:
            response = requests.get(f"{self.whisper_endpoint}/supported-formats")
            if response.status_code == 200:
                data = response.json()
                print("✅ Supported Audio Formats:")
                for format_info in data.get('formats', []):
                    print(f"   🎵 {format_info['extension']} - {format_info['description']}")
                print(f"\n📊 Max file size: {data.get('max_file_size', 'Unknown')}")
            else:
                print(f"❌ Failed to get supported formats: {response.status_code}")
        except Exception as e:
            print(f"❌ Error checking supported formats: {e}")
    
    def create_sample_audio_content(self):
        """Create sample audio content for different spiritual contexts"""
        
        sample_content = {
            "meditation_guide": {
                "title": "5-Minute Breathing Meditation",
                "script": """
                Welcome to this 5-minute breathing meditation. Find a comfortable seated position,
                close your eyes, and take a deep breath in through your nose. Hold for three seconds,
                then slowly exhale through your mouth. Feel your body relaxing with each breath.
                Now, simply observe your natural breath without trying to change it. If your mind
                wanders, gently bring your attention back to the sensation of breathing.
                """,
                "duration": "5 minutes",
                "voice_guidance": "Slow, calming pace with natural pauses"
            },
            
            "spiritual_teaching": {
                "title": "Understanding Inner Peace",
                "script": """
                Inner peace is not the absence of challenges, but the presence of calm awareness
                in the midst of life's storms. When we cultivate mindfulness and self-compassion,
                we develop the ability to remain centered regardless of external circumstances.
                The practice of meditation helps us discover this unchanging peace within ourselves.
                """,
                "duration": "3 minutes",
                "voice_guidance": "Clear, contemplative delivery"
            },
            
            "sloka_recitation": {
                "title": "Bhagavad Gita Chapter 2, Verse 47",
                "script": """
                कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।
                मा कर्मफलहेतुर्भूर्मा ते सङ्गोऽस्त्वकर्मणि॥
                
                Karmanye vadhikaraste ma phaleshu kadachana
                Ma karmaphalaheturbhur ma te sango'stvakarmani
                
                You have a right to perform your prescribed duty, but never to the fruits of action.
                Never consider yourself to be the cause of the results of your activities,
                and never be attached to not doing your duty.
                """,
                "duration": "2 minutes",
                "voice_guidance": "Sanskrit pronunciation with English translation"
            }
        }
        
        print("📝 Sample Content Created:")
        for content_type, details in sample_content.items():
            print(f"   🎯 {content_type.replace('_', ' ').title()}")
            print(f"      Title: {details['title']}")
            print(f"      Duration: {details['duration']}")
            print(f"      Guidance: {details['voice_guidance']}")
            print()
        
        return sample_content
    
    def show_api_examples(self):
        """Show practical API usage examples"""
        
        print("🔧 API Endpoint Examples:")
        print()
        
        # Transcription example
        print("1️⃣ AUDIO TRANSCRIPTION:")
        print("   POST /api/whisper/transcribe")
        print("   Content-Type: multipart/form-data")
        print("   Body:")
        print("     - audio_file: [audio file]")
        print("     - content_type: 'meditation_guide'")
        print("     - language: 'en' (optional)")
        print("     - include_timestamps: true")
        print()
        
        # Content creation example
        print("2️⃣ CONTENT CREATION:")
        print("   POST /api/whisper/create-content")
        print("   Content-Type: application/json")
        print("   Body:")
        print(json.dumps({
            "text": "Focus on your breath and find inner peace...",
            "content_type": "meditation_guide",
            "enhancement_level": "advanced",
            "target_duration": 300
        }, indent=6))
        print()
        
        # Health check example
        print("3️⃣ HEALTH CHECK:")
        print("   GET /api/whisper/health")
        print("   Response:")
        print(json.dumps({
            "status": "healthy",
            "model": "base",
            "device": "cpu",
            "supported_formats": [".mp3", ".wav", ".m4a"],
            "timestamp": "2024-01-01T12:00:00Z"
        }, indent=6))
        print()
    
    def show_guru_integration(self):
        """Show how Whisper integrates with AI Gurus"""
        
        print("🧘 AI Gurus Integration Examples:")
        print()
        
        guru_integrations = {
            "Meditation Guru": {
                "whisper_usage": "Transcribe guided meditations",
                "content_processing": "enhance_pauses, breathing_cues",
                "output_format": "guided_meditation_script",
                "example": "Convert voice-guided meditation into structured practice"
            },
            
            "Bhakti Guru": {
                "whisper_usage": "Transcribe devotional songs and prayers",
                "content_processing": "devotional_enhancement, sanskrit_recognition", 
                "output_format": "devotional_content",
                "example": "Process kirtan recordings with transliteration"
            },
            
            "Dharma Guru": {
                "whisper_usage": "Transcribe ethical teachings",
                "content_processing": "ethical_enhancement, wisdom_extraction",
                "output_format": "dharma_content",
                "example": "Extract moral principles from spiritual talks"
            },
            
            "Sloka Guru": {
                "whisper_usage": "Process Sanskrit recitations",
                "content_processing": "sanskrit_enhancement, verse_recognition",
                "output_format": "sanskrit_content", 
                "example": "Transcribe Vedic chants with meanings"
            }
        }
        
        for guru_name, integration in guru_integrations.items():
            print(f"🕉️ {guru_name}:")
            print(f"   Usage: {integration['whisper_usage']}")
            print(f"   Processing: {integration['content_processing']}")
            print(f"   Format: {integration['output_format']}")
            print(f"   Example: {integration['example']}")
            print()
    
    def create_audio_upload_example(self):
        """Create example code for uploading audio files"""
        
        upload_example = '''
import requests

def upload_audio_for_transcription(audio_file_path, content_type="spiritual_teaching"):
    """Upload audio file for Whisper transcription"""
    
    url = "http://localhost:5000/api/whisper/transcribe"
    
    with open(audio_file_path, 'rb') as audio_file:
        files = {'audio_file': audio_file}
        data = {
            'content_type': content_type,
            'language': 'en',
            'include_timestamps': 'true'
        }
        
        response = requests.post(url, files=files, data=data)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Transcription successful!")
            print(f"📝 Text: {result['transcription']['text']}")
            print(f"🌐 Language: {result['transcription']['language']}")
            return result
        else:
            print(f"❌ Transcription failed: {response.status_code}")
            return None

# Example usage
# result = upload_audio_for_transcription("meditation.mp3", "meditation_guide")
        '''
        
        print("💻 PYTHON UPLOAD EXAMPLE:")
        print(upload_example)
        
        javascript_example = '''
async function uploadAudioForTranscription(audioFile, contentType = 'spiritual_teaching') {
    const formData = new FormData();
    formData.append('audio_file', audioFile);
    formData.append('content_type', contentType);
    formData.append('language', 'en');
    formData.append('include_timestamps', 'true');
    
    try {
        const response = await fetch('/api/whisper/transcribe', {
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        
        if (response.ok) {
            console.log('✅ Transcription successful!');
            console.log('📝 Text:', result.transcription.text);
            return result;
        } else {
            console.error('❌ Transcription failed:', result.error);
            return null;
        }
    } catch (error) {
        console.error('❌ Error:', error);
        return null;
    }
}

// Example usage with file input
// const fileInput = document.getElementById('audioFile');
// const result = await uploadAudioForTranscription(fileInput.files[0], 'meditation_guide');
        '''
        
        print("🌐 JAVASCRIPT UPLOAD EXAMPLE:")
        print(javascript_example)

def main():
    """Run the Whisper content creation guide"""
    
    print("🎙️ OPENAI WHISPER CONTENT CREATION GUIDE")
    print("=" * 60)
    print(f"⏰ Guide started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    guide = WhisperContentCreationGuide()
    
    # Run the complete demo
    guide.demo_content_creation_workflow()
    
    print("💻 PROGRAMMING EXAMPLES:")
    print("-" * 40)
    guide.create_audio_upload_example()
    print()
    
    print("🎉 WHISPER CONTENT CREATION GUIDE COMPLETED!")
    print()
    print("📚 QUICK REFERENCE:")
    print("   • Health Check: GET /api/whisper/health")
    print("   • Upload Audio: POST /api/whisper/transcribe")
    print("   • Content Types: GET /api/whisper/content-types")
    print("   • Supported Formats: GET /api/whisper/supported-formats")
    print("   • Create Content: POST /api/whisper/create-content")
    print()
    print("🌟 Ready to create amazing spiritual content with Whisper!")

if __name__ == "__main__":
    main()
