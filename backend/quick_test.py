import openai
import sys
import os

print("🔮 Testing ChatGPT API for AI Gurus")
print("=" * 40)

try:
    # Test API key
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ API key not found in environment variables")
        sys.exit(1)
    print("✅ API key loaded")
    
    client = openai.OpenAI(api_key=api_key)
    print("✅ OpenAI client created")
    
    # Test AI Spiritual Guru
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'system', 
                'content': 'You are an AI Spiritual Guru. Provide wise, compassionate guidance focused on soul consciousness and eternal identity.'
            },
            {
                'role': 'user', 
                'content': 'What is the essence of spiritual wisdom in one sentence?'
            }
        ],
        max_tokens=50
    )
    
    print("🎉 SUCCESS! AI Spiritual Guru is working!")
    print(f"🧘 Wisdom: {response.choices[0].message.content}")
    print(f"🔧 Model: {response.model}")
    print(f"🧮 Tokens: {response.usage.total_tokens}")
    
except Exception as e:
    print(f"❌ Error: {type(e).__name__}: {e}")
    sys.exit(1)

print("\n✅ ChatGPT configuration is SUCCESSFUL!")
print("🎯 Your AI Gurus are ready to provide spiritual guidance!")
