#!/usr/bin/env python3
"""
Complete AI Gurus Workflow Test
================================

This script tests the complete ChatGPT workflow assignment system
for different AI Gurus, showing how each guru gets different 
ChatGPT configurations for optimal spiritual guidance.
"""

import os
import asyncio
import json
from datetime import datetime
import sys

# Set up environment
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("❌ OPENAI_API_KEY environment variable is not set")
    sys.exit(1)
os.environ['OPENAI_API_KEY'] = api_key

async def test_complete_workflow_system():
    """Test the complete AI Gurus workflow assignment system"""
    
    print("🔮 AI GURUS CHATGPT WORKFLOW SYSTEM TEST")
    print("=" * 60)
    print(f"⏰ Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # Import the services
        from workflow_assignment import ChatGPTWorkflowManager
        from services.ai_service import AIService
        
        # Initialize managers
        workflow_manager = ChatGPTWorkflowManager()
        ai_service = AIService()
        
        print("✅ Workflow system initialized successfully")
        print()
        
        # Test scenarios for each guru type
        test_scenarios = [
            {
                "guru_type": "spiritual",
                "question": "What is the ultimate purpose of human existence?",
                "user_context": {"experience_level": "intermediate"}
            },
            {
                "guru_type": "meditation", 
                "question": "Guide me through a 5-minute breathing meditation.",
                "user_context": {"experience_level": "beginner"}
            },
            {
                "guru_type": "sloka",
                "question": "Share a Sanskrit verse about inner peace with meaning.",
                "user_context": {"experience_level": "advanced"}
            },
            {
                "guru_type": "bhakti",
                "question": "How can I cultivate devotion in my daily life?",
                "user_context": {"experience_level": "intermediate"}
            },
            {
                "guru_type": "karma",
                "question": "I'm facing an ethical dilemma at work. How should I approach it?",
                "user_context": {"experience_level": "beginner"}
            }
        ]
        
        results = []
        
        for i, scenario in enumerate(test_scenarios, 1):
            print(f"🧘 TEST {i}: {scenario['guru_type'].upper()} GURU WORKFLOW")
            print("-" * 40)
            
            # Get workflow configuration
            workflow_config = workflow_manager.assign_chatgpt_to_workflow(
                scenario['guru_type'], 
                scenario['user_context']
            )
            
            # Display workflow assignment
            guru_info = workflow_config['guru_info']
            chatgpt_config = workflow_config['chatgpt_config']
            workflow_settings = workflow_config['workflow_settings']
            
            print(f"👤 Guru: {guru_info['name']}")
            print(f"🤖 ChatGPT Model: {chatgpt_config['model']}")
            print(f"🌡️ Temperature: {chatgpt_config['temperature']}")
            print(f"📏 Max Tokens: {chatgpt_config['max_tokens']}")
            print(f"⚡ Priority: {workflow_settings['priority']}")
            print(f"📡 Streaming: {workflow_settings.get('streaming', False)}")
            print()
            print(f"❓ Question: {scenario['question']}")
            print()
            
            try:
                # Get AI response using the assigned workflow
                response = await ai_service.get_spiritual_guidance(
                    scenario['guru_type'],
                    scenario['question'], 
                    scenario['user_context']
                )
                
                if response.get('success'):
                    print("✅ SUCCESS!")
                    print(f"📝 Response: {response['response'][:200]}...")
                    print(f"🔧 Model Used: {response.get('model', 'Unknown')}")
                    print(f"🧮 Tokens Used: {response.get('tokens_used', 'Unknown')}")
                    print(f"⚙️ Workflow: {response.get('workflow_used', 'Unknown')}")
                    
                    if response.get('configuration'):
                        config = response['configuration']
                        print(f"🎛️ Temperature: {config['temperature']}, Max Tokens: {config['max_tokens']}")
                    
                    results.append({
                        "guru_type": scenario['guru_type'],
                        "success": True,
                        "model": response.get('model'),
                        "tokens": response.get('tokens_used'),
                        "workflow": response.get('workflow_used')
                    })
                else:
                    print(f"❌ FAILED: {response.get('error')}")
                    results.append({
                        "guru_type": scenario['guru_type'],
                        "success": False,
                        "error": response.get('error')
                    })
                    
            except Exception as e:
                print(f"❌ ERROR: {e}")
                results.append({
                    "guru_type": scenario['guru_type'],
                    "success": False,
                    "error": str(e)
                })
            
            print()
            print("=" * 60)
            print()
        
        # Test summary
        print("📊 WORKFLOW SYSTEM TEST SUMMARY")
        print("=" * 40)
        
        successful_workflows = [r for r in results if r['success']]
        failed_workflows = [r for r in results if not r['success']]
        
        print(f"✅ Successful workflows: {len(successful_workflows)}/{len(results)}")
        print(f"❌ Failed workflows: {len(failed_workflows)}/{len(results)}")
        
        if successful_workflows:
            print()
            print("🎯 SUCCESSFUL WORKFLOWS:")
            for result in successful_workflows:
                print(f"   • {result['guru_type'].title()} Guru: {result.get('model', 'Unknown')} ({result.get('tokens', 'Unknown')} tokens)")
        
        if failed_workflows:
            print()
            print("⚠️ FAILED WORKFLOWS:")
            for result in failed_workflows:
                print(f"   • {result['guru_type'].title()} Guru: {result.get('error', 'Unknown error')}")
        
        print()
        
        # Show available workflow endpoints
        print("🌐 AVAILABLE API ENDPOINTS:")
        print("   • GET  /api/gurus/workflows - List all workflows")
        print("   • GET  /api/gurus/workflow/<type>/config - Get workflow config")
        print("   • POST /api/gurus/ask - Ask guru (uses workflow assignment)")
        print("   • POST /api/spiritual/guidance - Direct guidance (workflow-enabled)")
        
        print()
        print("🎉 WORKFLOW SYSTEM TEST COMPLETED!")
        
        # Calculate success rate
        success_rate = (len(successful_workflows) / len(results)) * 100
        print(f"📈 Overall Success Rate: {success_rate:.1f}%")
        
        if success_rate >= 80:
            print("🌟 EXCELLENT! Your AI Gurus workflow system is working great!")
        elif success_rate >= 60:
            print("👍 GOOD! Most workflows are functioning properly.")
        else:
            print("⚠️ NEEDS ATTENTION: Some workflows need debugging.")
            
    except Exception as e:
        print(f"❌ CRITICAL ERROR: Failed to initialize workflow system")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_complete_workflow_system())
