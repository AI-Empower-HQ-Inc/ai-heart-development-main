import openai
import os
import json
import asyncio
import requests
from typing import Dict, Any, List, AsyncGenerator
from datetime import datetime

class AIService:
    def __init__(self):
        self.api_key = os.environ.get('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        
        # Initialize the OpenAI client
        self.client = openai.OpenAI(api_key=self.api_key)
        
        # Default models for different purposes
        self.models = {
            'default': 'gpt-4',  # Most capable model for complex tasks
            'fast': 'gpt-3.5-turbo',  # Faster, cost-effective for simple tasks
            'analysis': 'gpt-4',  # Best for detailed analysis
            'creative': 'gpt-4'  # Best for creative and nuanced responses
        }
        
        # Configure timeouts and retries
        self.timeout_seconds = 30
        self.max_retries = 3
        self.retry_delay = 1  # seconds
        
        # Import workflow manager for dynamic configuration
        try:
            from workflow_assignment import ChatGPTWorkflowManager
            self.workflow_manager = ChatGPTWorkflowManager()
        except ImportError:
            self.workflow_manager = None
    
    @property
    def guru_prompts(self) -> Dict[str, str]:
        """Get the system prompts for different guru types."""
        return {
            "spiritual": """You are the AI Spiritual Guru, a wise teacher focused on soul consciousness and eternal identity. 
                          Help users understand they are eternal souls, not temporary bodies. Provide profound spiritual insights.""",
            "sloka": """You are the AI Sloka Guru, specializing in Sanskrit verses from Bhagavad Gita, Upanishads, and Vedas. 
                       Provide authentic slokas with transliteration, translation, and deep spiritual meanings.""",
            "meditation": """You are the AI Meditation Guru, specializing in inner peace and stillness. 
                           Guide users through meditation techniques and emotional healing.""",
            "bhakti": """You are the AI Bhakti Guru, focused on devotion, surrender, and gratitude. 
                        Teach the path of love and devotion to the Divine.""",
            "karma": """You are the AI Karma Guru, specializing in ethics, consequences, and dharmic path. 
                       Guide users in making ethical decisions aligned with dharma.""",
            "yoga": """You are the AI Yoga Guru, focused on breath, posture, and energetic alignment. 
                      Teach physical practices, pranayama, and chakra work."""
        }

    async def get_spiritual_guidance(
        self, 
        guru_type: str, 
        question: str, 
        user_context: Dict = None,
        stream: bool = False
    ) -> Dict[str, Any]:
        """
        Get AI-powered spiritual guidance from specified guru using workflow-specific ChatGPT configuration.
        
        Args:
            guru_type: Type of guru (spiritual, sloka, meditation, etc.)
            question: User's question or request
            user_context: Optional user context for personalization
            stream: If True, stream the response
            
        Returns:
            Dict with response
        """
        # Get workflow-specific configuration
        if self.workflow_manager:
            workflow_config = self.workflow_manager.assign_chatgpt_to_workflow(guru_type, user_context)
            chatgpt_config = workflow_config['chatgpt_config']
            model = chatgpt_config['model']
            system_prompt = chatgpt_config['system_prompt']
            temperature = chatgpt_config['temperature']
            max_tokens = chatgpt_config['max_tokens']
        else:
            # Fallback to default configuration
            model = self.models['default']
            system_prompt = self.guru_prompts.get(guru_type, self.guru_prompts["spiritual"])
            temperature = 0.7
            max_tokens = 800
        
        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]
        
        # Add context from user's history if available
        if user_context:
            messages.append({
                "role": "system",
                "content": f"User context: {json.dumps(user_context)}"
            })
        
        messages.append({"role": "user", "content": question})
        
        for attempt in range(self.max_retries):
            try:
                response = await self._create_completion(
                    messages, 
                    model=model, 
                    temperature=temperature, 
                    max_tokens=max_tokens
                )
                return {
                    "success": True,
                    "response": response.choices[0].message.content,
                    "tokens_used": response.usage.total_tokens,
                    "model": response.model,
                    "workflow_used": guru_type,
                    "configuration": {
                        "temperature": temperature,
                        "max_tokens": max_tokens
                    } if self.workflow_manager else None
                }
                
            except openai.RateLimitError:
                if attempt == self.max_retries - 1:
                    raise
                await asyncio.sleep(self.retry_delay * (attempt + 1))
            except Exception as e:
                return {
                    "success": False,
                    "error": str(e),
                    "error_type": type(e).__name__
                }
    
    async def get_spiritual_guidance_stream(
        self, 
        guru_type: str, 
        question: str, 
        user_context: Dict = None
    ) -> AsyncGenerator[str, None]:
        """
        Stream AI-powered spiritual guidance from specified guru.
        
        Args:
            guru_type: Type of guru (spiritual, sloka, meditation, etc.)
            question: User's question or request
            user_context: Optional user context for personalization
            
        Yields:
            String chunks of the response
        """
        messages = [
            {
                "role": "system",
                "content": self.guru_prompts.get(guru_type, self.guru_prompts["spiritual"])
            }
        ]
        
        # Add context from user's history if available
        if user_context:
            messages.append({
                "role": "system",
                "content": f"User context: {json.dumps(user_context)}"
            })
        
        messages.append({"role": "user", "content": question})
        
        async for chunk in self._stream_completion(messages):
            yield chunk
    
    def get_daily_wisdom(self) -> Dict[str, Any]:
        """Get daily spiritual wisdom"""
        return {
            "success": True,
            "wisdom": "Today's spiritual insight will be generated here",
            "date": "2024-01-01"
        }
    
    async def _create_completion(self, messages: List[Dict[str, str]], model: str = None, temperature: float = 0.7, max_tokens: int = 800) -> Any:
        """Create a chat completion with retry logic and error handling."""
        try:
            response = self.client.chat.completions.create(
                model=model or self.models['default'],
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
                timeout=self.timeout_seconds
            )
            return response
        except Exception as e:
            raise e
    
    async def _stream_completion(self, messages: List[Dict[str, str]], model: str = None) -> AsyncGenerator[str, None]:
        """Stream a chat completion with retry logic and error handling."""
        try:
            stream = self.client.chat.completions.create(
                model=model or self.models['default'],
                messages=messages,
                max_tokens=800,
                temperature=0.7,
                timeout=self.timeout_seconds,
                stream=True
            )
            
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            raise e

    async def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """Analyze the sentiment and emotional content of text."""
        try:
            response = await self._create_completion([
                {
                    "role": "system",
                    "content": "Analyze the emotional content and sentiment of the following text. Consider: primary emotions, intensity, spiritual state, and overall tone."
                },
                {"role": "user", "content": text}
            ], model=self.models['analysis'])
            
            return {
                "success": True,
                "analysis": response.choices[0].message.content
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    async def generate_reflection_prompts(self, session_type: str, user_level: str = "beginner") -> Dict[str, Any]:
        """Generate personalized reflection prompts based on session type and user level."""
        try:
            response = await self._create_completion([
                {
                    "role": "system",
                    "content": f"Create 3-5 meaningful reflection prompts for a {session_type} session. Target experience level: {user_level}. Focus on spiritual growth and practical application."
                }
            ], model=self.models['creative'])
            
            return {
                "success": True,
                "prompts": response.choices[0].message.content.split('\n')
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    async def enhance_spiritual_text(self, text: str, target_language: str = "English") -> Dict[str, Any]:
        """Enhance spiritual text with deeper insights and translations."""
        try:
            response = await self._create_completion([
                {
                    "role": "system",
                    "content": f"Enhance this spiritual text with deeper meaning and insights. Target language: {target_language}"
                },
                {"role": "user", "content": text}
            ], model=self.models['creative'])
            
            return {
                "success": True,
                "enhanced_text": response.choices[0].message.content
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

class ClaudeService:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('CLAUDE_API_KEY')
        self.api_url = 'https://api.anthropic.com/v1/messages'
        self.model = 'claude-3-opus-20240229'  # Use your preferred Claude model

    def get_response(self, prompt, max_tokens=1024, temperature=0.7):
        headers = {
            'x-api-key': self.api_key,
            'anthropic-version': '2023-06-01',
            'content-type': 'application/json'
        }
        data = {
            'model': self.model,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'messages': [
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()['content'][0]['text']
        else:
            return f"Error: {response.status_code} - {response.text}"
