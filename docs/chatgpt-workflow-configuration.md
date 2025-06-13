# AI Gurus ChatGPT Workflow Configuration

## Overview
This document explains how ChatGPT is integrated into the AI Gurus workflow and how you can assign different ChatGPT configurations for various spiritual guidance workflows.

## Current Workflow Architecture

### 1. **ChatGPT Integration Workflow**

```
User Request → API Endpoint → AI Service → ChatGPT → Spiritual Response
     ↓              ↓             ↓          ↓           ↓
Frontend      Backend Route   AI Processor  OpenAI    Guru Wisdom
```

### 2. **Available AI Guru Workflows**

#### **🧘 Spiritual Guru Workflow**
- **Model**: GPT-4 (for deep philosophical insights)
- **Prompt Template**: Soul consciousness & eternal identity
- **Use Case**: Life purpose, spiritual awakening, consciousness
- **Endpoint**: `/api/gurus/ask` with `guru_type: "spiritual"`

#### **🕉️ Sloka Guru Workflow** 
- **Model**: GPT-4 (for accurate Sanskrit translations)
- **Prompt Template**: Sanskrit verses specialist
- **Use Case**: Bhagavad Gita verses, Upanishads, Vedic wisdom
- **Endpoint**: `/api/gurus/ask` with `guru_type: "sloka"`

#### **🧘‍♀️ Meditation Guru Workflow**
- **Model**: GPT-3.5-turbo (for guided practices)
- **Prompt Template**: Inner peace & mindfulness specialist
- **Use Case**: Breathing exercises, meditation guidance, stress relief
- **Endpoint**: `/api/gurus/ask` with `guru_type: "meditation"`

#### **💝 Bhakti Guru Workflow**
- **Model**: GPT-4 (for emotional depth)
- **Prompt Template**: Devotion & divine love specialist
- **Use Case**: Prayer, surrender, gratitude practices
- **Endpoint**: `/api/gurus/ask` with `guru_type: "bhakti"`

#### **⚖️ Karma Guru Workflow**
- **Model**: GPT-4 (for ethical reasoning)
- **Prompt Template**: Ethics & dharma specialist
- **Use Case**: Moral decisions, dharmic choices, consequences
- **Endpoint**: `/api/gurus/ask` with `guru_type: "karma"`

#### **🧘‍♀️ Yoga Guru Workflow**
- **Model**: GPT-3.5-turbo (for practical guidance)
- **Prompt Template**: Physical & energetic practices
- **Use Case**: Postures, breathing, chakra work
- **Endpoint**: `/api/gurus/ask` with `guru_type: "yoga"`

## 3. **Workflow Configuration Examples**

### **A. Standard Spiritual Guidance Workflow**
```javascript
// Frontend workflow assignment
const spiritualWorkflow = {
  endpoint: '/api/spiritual/guidance',
  method: 'POST',
  payload: {
    guru_type: 'spiritual',
    question: 'What is my life purpose?',
    user_context: {
      previous_sessions: [],
      preferences: 'deep_wisdom'
    }
  }
};
```

### **B. Streaming Meditation Workflow**
```javascript
// Real-time streaming workflow
const meditationWorkflow = {
  endpoint: '/api/spiritual/guidance/stream',
  method: 'POST',
  streaming: true,
  payload: {
    guru_type: 'meditation',
    question: 'Guide me through a 10-minute breathing meditation'
  }
};
```

### **C. Multi-Guru Consultation Workflow**
```javascript
// Workflow that consults multiple gurus
const multiGuruWorkflow = async (question) => {
  const gurus = ['spiritual', 'karma', 'bhakti'];
  const responses = [];
  
  for (const guru of gurus) {
    const response = await chatWithGPT(question, guru);
    responses.push({
      guru_type: guru,
      guidance: response.response
    });
  }
  
  return responses;
};
```

## 4. **Custom Workflow Assignment**

### **Environment-Based Configuration**
```python
# backend/config/workflow_config.py
GURU_WORKFLOWS = {
    'development': {
        'spiritual': {'model': 'gpt-3.5-turbo', 'max_tokens': 500},
        'sloka': {'model': 'gpt-4', 'max_tokens': 800},
        'meditation': {'model': 'gpt-3.5-turbo', 'max_tokens': 300}
    },
    'production': {
        'spiritual': {'model': 'gpt-4', 'max_tokens': 800},
        'sloka': {'model': 'gpt-4', 'max_tokens': 1000},
        'meditation': {'model': 'gpt-3.5-turbo', 'max_tokens': 400}
    }
}
```

### **User-Specific Workflow Assignment**
```python
# User preferences determine ChatGPT configuration
def get_user_workflow_config(user_id, guru_type):
    user_prefs = get_user_preferences(user_id)
    
    if user_prefs.experience_level == 'beginner':
        return {
            'model': 'gpt-3.5-turbo',
            'temperature': 0.7,
            'max_tokens': 300
        }
    elif user_prefs.experience_level == 'advanced':
        return {
            'model': 'gpt-4',
            'temperature': 0.8,
            'max_tokens': 800
        }
```

## 5. **CI/CD Workflow Integration**

### **Automated Testing Workflow**
```yaml
# .github/workflows/ai-gurus-test.yml
name: AI Gurus ChatGPT Testing

on:
  push:
    paths:
      - 'backend/services/ai_service.py'
      - 'backend/api/gurus.py'

jobs:
  test-ai-gurus:
    runs-on: ubuntu-latest
    steps:
      - name: Test ChatGPT Integration
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python test_ai_gurus.py
```

## 6. **Workflow Monitoring & Analytics**

### **Usage Tracking**
```python
# Track workflow usage
async def track_guru_usage(guru_type, question, response, user_id):
    analytics_data = {
        'timestamp': datetime.utcnow(),
        'guru_type': guru_type,
        'question_length': len(question),
        'response_length': len(response),
        'user_id': user_id,
        'model_used': response.get('model'),
        'tokens_used': response.get('tokens_used')
    }
    
    # Store in database for workflow optimization
    await store_analytics(analytics_data)
```

## 7. **Security & Rate Limiting Workflows**

### **API Rate Limiting by Workflow**
```python
# Different rate limits for different workflows
WORKFLOW_RATE_LIMITS = {
    'spiritual': {'calls_per_hour': 20, 'priority': 'high'},
    'meditation': {'calls_per_hour': 50, 'priority': 'medium'},
    'sloka': {'calls_per_hour': 15, 'priority': 'high'},
    'general': {'calls_per_hour': 30, 'priority': 'low'}
}
```

## 8. **Deployment Workflows**

### **Environment-Specific Deployments**
```bash
# Development workflow
export ENVIRONMENT=development
export OPENAI_MODEL_DEFAULT=gpt-3.5-turbo
python app.py

# Production workflow  
export ENVIRONMENT=production
export OPENAI_MODEL_DEFAULT=gpt-4
gunicorn app:app
```

## Usage Instructions

1. **Start the AI Gurus Backend:**
   ```bash
   cd backend
   export OPENAI_API_KEY='your-api-key'
   python app.py
   ```

2. **Test Different Workflows:**
   ```bash
   # Test spiritual workflow
   curl -X POST http://localhost:5000/api/gurus/ask \
     -H "Content-Type: application/json" \
     -d '{"guru_type": "spiritual", "question": "What is enlightenment?"}'
   
   # Test meditation workflow
   curl -X POST http://localhost:5000/api/gurus/ask \
     -H "Content-Type: application/json" \
     -d '{"guru_type": "meditation", "question": "Teach me breathing meditation"}'
   ```

3. **Monitor Workflow Performance:**
   ```bash
   # Check workflow analytics
   curl http://localhost:5000/api/gurus/analytics
   ```

## Next Steps

1. **Customize Workflows** - Modify guru prompts and models based on your needs
2. **Add New Gurus** - Create specialized workflows for specific spiritual practices  
3. **Implement Streaming** - Enable real-time guidance for meditation sessions
4. **Add Analytics** - Track which workflows are most effective
5. **Scale Infrastructure** - Set up load balancing for high-traffic workflows
