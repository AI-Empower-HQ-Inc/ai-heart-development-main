#!/usr/bin/env python3
"""
Simple ChatGPT test for AI Gurus
"""

import os
import openai
import sys

# Set API key
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("❌ OPENAI_API_KEY environment variable is not set")
    sys.exit(1)

def test_chatgpt():
    """Test basic ChatGPT functionality"""
    try:
        print("🔮 Testing ChatGPT connection...")
        
        # Initialize OpenAI client
        client = openai.OpenAI(api_key=api_key)
        
        # Test with a simple spiritual question
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a wise spiritual guru. Provide brief, insightful spiritual guidance."
                },
                {
                    "role": "user", 
                    "content": "What is the key to inner peace?"
                }
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        answer = response.choices[0].message.content
        print("✅ ChatGPT connection successful!")
        print(f"🙏 Spiritual wisdom: {answer}")
        print(f"📊 Tokens used: {response.usage.total_tokens}")
        return True
        
    except Exception as e:
        print(f"❌ ChatGPT test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 AI Gurus - ChatGPT Configuration Test\n")
    
    if test_chatgpt():
        print("\n🎉 SUCCESS: ChatGPT is properly configured for AI Gurus!")
        print("✅ You can now use all spiritual gurus with AI-powered responses.")
    else:
        print("\n❌ FAILED: ChatGPT configuration needs attention.")
    
    print("\n🙏 Test completed!")
