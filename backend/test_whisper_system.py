#!/usr/bin/env python3
"""
Whisper Content Creation Test
=============================

Test script to demonstrate OpenAI Whisper integration for spiritual content creation
in the AI Gurus platform.
"""

import os
import sys
import asyncio
import json
from pathlib import Path
from datetime import datetime

# Check for API key
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("❌ OPENAI_API_KEY environment variable is not set")
    sys.exit(1)

async def test_whisper_content_creation():
    """Test Whisper service for content creation"""
    
    print("🎙️ WHISPER CONTENT CREATION TEST")
    print("=" * 50)
    print(f"⏰ Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # Import the Whisper service
        from services.whisper_service import WhisperContentCreationService
        
        # Initialize service
        print("🔧 Initializing Whisper service...")
        whisper_service = WhisperContentCreationService()
        print("✅ Whisper service initialized successfully")
        print(f"📱 Device: {whisper_service.device}")
        print(f"🤖 Model: {whisper_service.model_size}")
        print()
        
        # Test content type configurations
        print("📋 AVAILABLE CONTENT TYPES:")
        print("-" * 30)
        for content_type, template in whisper_service.content_templates.items():
            print(f"🎯 {content_type.replace('_', ' ').title()}")
            print(f"   Format: {template['format']}")
            print(f"   Processing: {template['processing']}")
            print()
        
        # Create sample audio content for testing
        test_scenarios = [
            {
                "type": "meditation_guide",
                "sample_text": """
                Welcome to this breathing meditation. Find a comfortable position and close your eyes.
                Take a deep breath in through your nose, and slowly exhale through your mouth.
                Focus your attention on the breath as it flows in and out naturally.
                If your mind wanders, gently bring your attention back to the breath.
                Continue this practice for the next few minutes, finding peace in each breath.
                """,
                "description": "Guided breathing meditation"
            },
            {
                "type": "spiritual_teaching",
                "sample_text": """
                The journey of spiritual awakening begins with understanding our true nature.
                We are not merely physical bodies, but eternal souls on a path of growth.
                Consciousness is the foundation of all existence, and through meditation we can
                access deeper levels of awareness. The practice of self-inquiry leads us to
                discover the divine essence within ourselves and all beings.
                """,
                "description": "Teaching on consciousness and spiritual awakening"
            },
            {
                "type": "sloka_recitation",
                "sample_text": """
                Om Gam Ganapataye Namaha. This sacred mantra honors Lord Ganesha,
                the remover of obstacles. Om represents the cosmic sound,
                Gam is the seed syllable of Ganesha, and Namaha means salutations.
                Karmanye vadhikaraste Ma Phaleshu Kadachana. You have a right to perform
                your prescribed duty, but do not become attached to the fruits of action.
                """,
                "description": "Sanskrit mantras and Bhagavad Gita verse"
            },
            {
                "type": "prayer_chanting",
                "sample_text": """
                Hare Krishna Hare Krishna Krishna Krishna Hare Hare
                Hare Rama Hare Rama Rama Rama Hare Hare
                Om Namah Shivaya Om Namah Shivaya
                Om Mani Padme Hum Om Mani Padme Hum
                May all beings be happy and free from suffering
                """,
                "description": "Devotional chanting and prayer"
            },
            {
                "type": "dharma_talk",
                "sample_text": """
                The principles of dharma guide us in right action and ethical living.
                Truthfulness, non-violence, and compassion form the foundation of dharmic life.
                When we align our actions with these universal principles, we create harmony
                in our lives and contribute to the wellbeing of all. Every choice we make
                is an opportunity to practice dharma and grow spiritually.
                """,
                "description": "Teaching on dharmic principles"
            }
        ]
        
        results = []
        
        print("🧪 CONTENT PROCESSING TESTS:")
        print("=" * 40)
        
        for i, scenario in enumerate(test_scenarios, 1):
            print(f"\n📝 TEST {i}: {scenario['type'].upper().replace('_', ' ')}")
            print(f"📖 Description: {scenario['description']}")
            print("-" * 40)
            
            try:
                # Simulate audio transcription result
                mock_whisper_result = {
                    "text": scenario["sample_text"].strip(),
                    "language": "en",
                    "segments": [
                        {
                            "text": sentence.strip(),
                            "start": i * 3.0,
                            "end": (i + 1) * 3.0
                        }
                        for i, sentence in enumerate(scenario["sample_text"].split('.')) 
                        if sentence.strip()
                    ]
                }
                
                # Process content using Whisper service
                processed_content = await whisper_service._process_transcription(
                    mock_whisper_result,
                    scenario["type"],
                    f"sample_{scenario['type']}.wav"
                )
                
                print("✅ PROCESSING SUCCESSFUL!")
                print(f"📄 Raw text length: {len(processed_content['raw_text'])} characters")
                print(f"🔧 Processing applied: {processed_content['processing_applied']}")
                
                # Display type-specific results
                if scenario["type"] == "meditation_guide":
                    phases = processed_content.get("meditation_phases", [])
                    print(f"🧘 Meditation phases detected: {len(phases)}")
                    print(f"🎯 Meditation type: {processed_content.get('meditation_type', 'Unknown')}")
                    
                elif scenario["type"] == "spiritual_teaching":
                    concepts = processed_content.get("key_concepts", [])
                    quotes = processed_content.get("wisdom_quotes", [])
                    print(f"💡 Key concepts extracted: {len(concepts)}")
                    print(f"📜 Wisdom quotes found: {len(quotes)}")
                    if concepts:
                        print(f"🔍 Sample concepts: {', '.join(concepts[:3])}")
                
                elif scenario["type"] == "sloka_recitation":
                    sanskrit_segments = processed_content.get("sanskrit_segments", [])
                    detected_slokas = processed_content.get("detected_slokas", [])
                    print(f"🕉️ Sanskrit segments: {len(sanskrit_segments)}")
                    print(f"📿 Known slokas detected: {len(detected_slokas)}")
                
                elif scenario["type"] == "prayer_chanting":
                    chant_patterns = processed_content.get("chant_patterns", [])
                    devotional_phrases = processed_content.get("devotional_phrases", [])
                    print(f"🎵 Chant patterns: {len(chant_patterns)}")
                    print(f"🙏 Devotional phrases: {len(devotional_phrases)}")
                
                elif scenario["type"] == "dharma_talk":
                    ethical_points = processed_content.get("ethical_points", [])
                    dharma_principles = processed_content.get("dharma_principles", [])
                    print(f"⚖️ Ethical points: {len(ethical_points)}")
                    print(f"📚 Dharma principles: {len(dharma_principles)}")
                
                results.append({
                    "type": scenario["type"],
                    "success": True,
                    "processing": processed_content["processing_applied"]
                })
                
            except Exception as e:
                print(f"❌ PROCESSING FAILED: {e}")
                results.append({
                    "type": scenario["type"],
                    "success": False,
                    "error": str(e)
                })
        
        # Test summary
        print("\n" + "=" * 50)
        print("📊 WHISPER CONTENT CREATION TEST SUMMARY")
        print("=" * 50)
        
        successful_tests = [r for r in results if r['success']]
        failed_tests = [r for r in results if not r['success']]
        
        print(f"✅ Successful content types: {len(successful_tests)}/{len(results)}")
        print(f"❌ Failed content types: {len(failed_tests)}/{len(results)}")
        
        if successful_tests:
            print("\n🎯 SUCCESSFULLY PROCESSED CONTENT TYPES:")
            for result in successful_tests:
                print(f"   • {result['type'].replace('_', ' ').title()}: {result['processing']}")
        
        if failed_tests:
            print("\n⚠️ FAILED CONTENT TYPES:")
            for result in failed_tests:
                print(f"   • {result['type'].replace('_', ' ').title()}: {result.get('error', 'Unknown error')}")
        
        print(f"\n🌐 AVAILABLE API ENDPOINTS:")
        print("   • POST /api/whisper/transcribe - Upload audio for transcription")
        print("   • GET  /api/whisper/content-types - List available content types")
        print("   • GET  /api/whisper/supported-formats - Supported audio formats")
        print("   • POST /api/whisper/create-content - Create enhanced spiritual content")
        print("   • GET  /api/whisper/transcriptions - List recent transcriptions")
        print("   • GET  /api/whisper/health - Service health check")
        
        print(f"\n📁 CONTENT DIRECTORIES:")
        print(f"   • Audio uploads: {whisper_service.upload_dir}")
        print(f"   • Transcriptions: {whisper_service.transcription_dir}")
        
        # Calculate success rate
        success_rate = (len(successful_tests) / len(results)) * 100
        print(f"\n📈 Overall Success Rate: {success_rate:.1f}%")
        
        if success_rate >= 80:
            print("🌟 EXCELLENT! Whisper content creation system is working perfectly!")
        elif success_rate >= 60:
            print("👍 GOOD! Most content types are processing correctly.")
        else:
            print("⚠️ NEEDS ATTENTION: Some content types need debugging.")
        
        print("\n💡 NEXT STEPS:")
        print("   1. Upload audio files to test transcription")
        print("   2. Try different content types for specialized processing")
        print("   3. Integrate with AI Gurus for enhanced content creation")
        print("   4. Create meditation guides from audio sessions")
        print("   5. Build a library of transcribed spiritual teachings")
        
        print(f"\n🎉 WHISPER CONTENT CREATION TEST COMPLETED!")
        
    except Exception as e:
        print(f"❌ CRITICAL ERROR: Failed to initialize Whisper system")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_whisper_content_creation())
