"""
AI Gurus ChatGPT Workflow Assignment Configuration
==================================================

This module demonstrates how ChatGPT is assigned to different 
AI Guru workflows in the spiritual guidance platform.
"""

from typing import Dict, Any
import os

class ChatGPTWorkflowManager:
    """
    Manages ChatGPT workflow assignments for different AI Gurus
    """
    
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        
        # Define workflow configurations for each AI Guru
        self.guru_workflows = {
            
            # 🧘 SPIRITUAL GURU WORKFLOW
            "spiritual": {
                "name": "🧘 AI Spiritual Guru",
                "chatgpt_model": "gpt-3.5-turbo",  # Use available model
                "temperature": 0.8,        # Higher creativity for spiritual insights
                "max_tokens": 800,         # Longer responses for deep guidance
                "system_prompt": """You are the AI Spiritual Guru, a wise teacher focused on 
                                  soul consciousness and eternal identity. Help users understand 
                                  they are eternal souls, not temporary bodies. Provide profound 
                                  spiritual insights with compassion and wisdom.""",
                "workflow_type": "deep_guidance",
                "priority": "high"
            },
            
            # 🕉️ SLOKA GURU WORKFLOW  
            "sloka": {
                "name": "🕉️ AI Sloka Guru",
                "chatgpt_model": "gpt-3.5-turbo",  # Use available model
                "temperature": 0.6,        # Lower temperature for accuracy
                "max_tokens": 1000,        # Longer for verse + explanation
                "system_prompt": """You are the AI Sloka Guru, specializing in Sanskrit verses 
                                  from Bhagavad Gita, Upanishads, and Vedas. Provide authentic 
                                  slokas with transliteration, translation, and deep meanings.""",
                "workflow_type": "scholarly_guidance",
                "priority": "high"
            },
            
            # 🧘‍♀️ MEDITATION GURU WORKFLOW
            "meditation": {
                "name": "🧘‍♀️ AI Meditation Guru",
                "chatgpt_model": "gpt-3.5-turbo",  # Cost-effective for guided practice
                "temperature": 0.7,                # Balanced creativity
                "max_tokens": 500,                 # Medium length for instructions
                "system_prompt": """You are the AI Meditation Guru, specializing in inner peace 
                                  and stillness. Guide users through meditation techniques and 
                                  emotional healing with gentle, soothing language.""",
                "workflow_type": "guided_practice",
                "priority": "medium",
                "streaming": True  # Enable real-time guidance
            },
            
            # 💝 BHAKTI GURU WORKFLOW
            "bhakti": {
                "name": "💝 AI Bhakti Guru", 
                "chatgpt_model": "gpt-3.5-turbo",  # Use available model
                "temperature": 0.9,        # High creativity for devotional content
                "max_tokens": 600,         # Medium-long for devotional guidance
                "system_prompt": """You are the AI Bhakti Guru, focused on devotion, surrender, 
                                  and gratitude. Teach the path of love and devotion to the Divine 
                                  with warmth and spiritual emotion.""",
                "workflow_type": "devotional_guidance",
                "priority": "high"
            },
            
            # ⚖️ KARMA GURU WORKFLOW
            "karma": {
                "name": "⚖️ AI Karma Guru",
                "chatgpt_model": "gpt-3.5-turbo",  # Use available model
                "temperature": 0.5,        # Lower temperature for clear ethics
                "max_tokens": 700,         # Detailed ethical guidance
                "system_prompt": """You are the AI Karma Guru, specializing in ethics, 
                                  consequences, and dharmic path. Guide users in making ethical 
                                  decisions aligned with dharma and universal principles.""",
                "workflow_type": "ethical_guidance", 
                "priority": "high"
            },
            
            # 🧘‍♀️ YOGA GURU WORKFLOW
            "yoga": {
                "name": "🧘‍♀️ AI Yoga Guru",
                "chatgpt_model": "gpt-3.5-turbo",  # Practical guidance
                "temperature": 0.6,                # Structured responses
                "max_tokens": 400,                 # Shorter for practical steps
                "system_prompt": """You are the AI Yoga Guru, focused on breath, posture, 
                                  and energetic alignment. Teach physical practices, pranayama, 
                                  and chakra work with clear, practical instructions.""",
                "workflow_type": "practical_guidance",
                "priority": "medium"
            }
        }
        
        # Rate limiting per workflow
        self.rate_limits = {
            "spiritual": {"per_hour": 20, "per_day": 100},
            "sloka": {"per_hour": 15, "per_day": 80},
            "meditation": {"per_hour": 50, "per_day": 200},  # Higher for practice sessions
            "bhakti": {"per_hour": 25, "per_day": 120},
            "karma": {"per_hour": 20, "per_day": 100},
            "yoga": {"per_hour": 30, "per_day": 150}
        }
    
    def get_workflow_config(self, guru_type: str) -> Dict[str, Any]:
        """Get the ChatGPT configuration for a specific guru workflow"""
        if guru_type not in self.guru_workflows:
            # Default to spiritual guru workflow
            guru_type = "spiritual"
            
        config = self.guru_workflows[guru_type].copy()
        config['rate_limit'] = self.rate_limits[guru_type]
        return config
    
    def assign_chatgpt_to_workflow(self, guru_type: str, user_context: Dict = None) -> Dict[str, Any]:
        """
        Assign ChatGPT configuration to a specific workflow
        """
        base_config = self.get_workflow_config(guru_type)
        
        # Customize based on user context
        if user_context:
            if user_context.get('experience_level') == 'beginner':
                base_config['temperature'] = max(0.3, base_config['temperature'] - 0.2)
                base_config['max_tokens'] = min(400, base_config['max_tokens'])
            elif user_context.get('experience_level') == 'advanced':
                base_config['max_tokens'] = min(1000, base_config['max_tokens'] + 200)
        
        return {
            "guru_info": {
                "name": base_config['name'],
                "type": guru_type,
                "workflow_type": base_config['workflow_type']
            },
            "chatgpt_config": {
                "model": base_config['chatgpt_model'],
                "temperature": base_config['temperature'],
                "max_tokens": base_config['max_tokens'],
                "system_prompt": base_config['system_prompt']
            },
            "workflow_settings": {
                "priority": base_config['priority'],
                "streaming": base_config.get('streaming', False),
                "rate_limit": base_config['rate_limit']
            }
        }
    
    def get_available_workflows(self) -> Dict[str, str]:
        """Get list of available guru workflows"""
        return {
            guru_type: config['name'] 
            for guru_type, config in self.guru_workflows.items()
        }

# Example usage functions
def demonstrate_workflow_assignment():
    """
    Demonstrate how ChatGPT is assigned to different workflows
    """
    workflow_manager = ChatGPTWorkflowManager()
    
    print("🔮 AI Gurus ChatGPT Workflow Assignment Demo")
    print("=" * 50)
    
    # Example 1: Spiritual Guidance Workflow
    spiritual_config = workflow_manager.assign_chatgpt_to_workflow("spiritual")
    print(f"\n1. {spiritual_config['guru_info']['name']} Workflow:")
    print(f"   Model: {spiritual_config['chatgpt_config']['model']}")
    print(f"   Temperature: {spiritual_config['chatgpt_config']['temperature']}")
    print(f"   Max Tokens: {spiritual_config['chatgpt_config']['max_tokens']}")
    print(f"   Priority: {spiritual_config['workflow_settings']['priority']}")
    
    # Example 2: Meditation Practice Workflow  
    meditation_config = workflow_manager.assign_chatgpt_to_workflow("meditation")
    print(f"\n2. {meditation_config['guru_info']['name']} Workflow:")
    print(f"   Model: {meditation_config['chatgpt_config']['model']}")
    print(f"   Streaming: {meditation_config['workflow_settings']['streaming']}")
    print(f"   Rate Limit: {meditation_config['workflow_settings']['rate_limit']['per_hour']}/hour")
    
    # Example 3: Personalized Workflow
    user_context = {"experience_level": "beginner", "preferences": ["simple_language"]}
    beginner_config = workflow_manager.assign_chatgpt_to_workflow("karma", user_context)
    print(f"\n3. Beginner {beginner_config['guru_info']['name']} Workflow:")
    print(f"   Adjusted Temperature: {beginner_config['chatgpt_config']['temperature']}")
    print(f"   Adjusted Max Tokens: {beginner_config['chatgpt_config']['max_tokens']}")

# API Integration example
def create_chatgpt_request(guru_type: str, question: str, user_context: Dict = None):
    """
    Create a ChatGPT request based on workflow assignment
    """
    workflow_manager = ChatGPTWorkflowManager()
    config = workflow_manager.assign_chatgpt_to_workflow(guru_type, user_context)
    
    # This would be sent to OpenAI API
    chatgpt_request = {
        "model": config['chatgpt_config']['model'],
        "messages": [
            {
                "role": "system", 
                "content": config['chatgpt_config']['system_prompt']
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "temperature": config['chatgpt_config']['temperature'],
        "max_tokens": config['chatgpt_config']['max_tokens']
    }
    
    return chatgpt_request, config

if __name__ == "__main__":
    demonstrate_workflow_assignment()
