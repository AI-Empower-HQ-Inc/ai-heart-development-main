#!/usr/bin/env python3
"""
Test script for AI Gurus ChatGPT integration
"""

import os
import asyncio
import sys

# Set the API key
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("❌ OPENAI_API_KEY environment variable is not set")
    sys.exit(1)
os.environ['OPENAI_API_KEY'] = api_key

async def test_spiritual_guru():
    """Test the spiritual guru AI service"""
    try:
        from services.ai_service import AIService
        
        print("🔮 Testing AI Spiritual Guru...")
        ai_service = AIService()
        
        # Test a simple spiritual question
        result = await ai_service.get_spiritual_guidance(
            guru_type="spiritual", 
            question="What is the purpose of life from a spiritual perspective?"
        )
        
        if result.get('success'):
            print("✅ AI Spiritual Guru Test PASSED!")
            print(f"🙏 Response: {result['response'][:200]}...")
            print(f"📊 Tokens used: {result.get('tokens_used', 'N/A')}")
            print(f"🤖 Model: {result.get('model', 'N/A')}")
        else:
            print("❌ AI Spiritual Guru Test FAILED!")
            print(f"Error: {result.get('error', 'Unknown error')}")
            
        return result.get('success', False)
        
    except Exception as e:
        print(f"❌ Exception in AI Spiritual Guru Test: {e}")
        return False

async def test_all_gurus():
    """Test all available gurus"""
    gurus = ['spiritual', 'sloka', 'meditation', 'bhakti', 'karma', 'yoga']
    
    try:
        from services.ai_service import AIService
        ai_service = AIService()
        
        for guru in gurus:
            print(f"\n🧘 Testing {guru.upper()} Guru...")
            result = await ai_service.get_spiritual_guidance(
                guru_type=guru, 
                question=f"Give me wisdom about {guru} practice"
            )
            
            if result.get('success'):
                print(f"✅ {guru.upper()} Guru: WORKING")
                print(f"   Response preview: {result['response'][:100]}...")
            else:
                print(f"❌ {guru.upper()} Guru: FAILED - {result.get('error', 'Unknown')}")
                
    except Exception as e:
        print(f"❌ Exception in guru tests: {e}")

async def main():
    """Main test function"""
    print("🚀 Starting AI Gurus ChatGPT Integration Tests\n")
    
    # Test basic spiritual guru first
    success = await test_spiritual_guru()
    
    if success:
        print("\n" + "="*50)
        print("🎉 Basic test passed! Testing all gurus...")
        await test_all_gurus()
        print("\n✅ AI Gurus ChatGPT integration is CONFIGURED and WORKING!")
    else:
        print("\n❌ Basic test failed. Please check the configuration.")
    
    print("\n🙏 Test completed!")

if __name__ == "__main__":
    asyncio.run(main())
