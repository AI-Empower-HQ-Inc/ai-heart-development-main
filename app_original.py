import os
import logging
import openai
from flask import Flask, request, jsonify, render_template_string
from google.cloud import secretmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def get_openai_key():
    """Get OpenAI API key from Secret Manager"""
    try:
        client = secretmanager.SecretManagerServiceClient()
        project_id = os.environ.get('GOOGLE_CLOUD_PROJECT', 'chatgpt-connector-462102')
        name = f"projects/{project_id}/secrets/openai-api-key/versions/latest"
        response = client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")
    except Exception as e:
        logger.error(f"Failed to load API key: {e}")
        return os.environ.get('OPENAI_API_KEY', '')

# Initialize OpenAI
openai.api_key = get_openai_key()

@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>ChatGPT Business</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f5f5f5; }
        .container { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header { text-align: center; color: #333; margin-bottom: 30px; }
        .chat-box { border: 1px solid #ddd; height: 400px; overflow-y: scroll; padding: 15px; margin-bottom: 15px; background: #fafafa; }
        .message { margin: 10px 0; padding: 10px; border-radius: 8px; }
        .user { background: #007bff; color: white; text-align: right; }
        .assistant { background: #e9ecef; color: #333; }
        .input-area { display: flex; gap: 10px; }
        input { flex: 1; padding: 12px; border: 1px solid #ddd; border-radius: 5px; }
        button { padding: 12px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background: #0056b3; }
        button:disabled { background: #6c757d; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 ChatGPT Business Assistant</h1>
            <p>Your AI-powered business companion</p>
        </div>
        <div id="chat-box" class="chat-box">
            <div class="message assistant">
                <strong>Assistant:</strong> Hello! I'm your ChatGPT Business Assistant. How can I help you today?
            </div>
        </div>
        <div class="input-area">
            <input type="text" id="message-input" placeholder="Type your message..." 
                   onkeypress="if(event.key==='Enter') sendMessage()">
            <button onclick="sendMessage()" id="send-btn">Send</button>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('message-input');
            const sendBtn = document.getElementById('send-btn');
            const message = input.value.trim();
            
            if (!message) return;

            sendBtn.disabled = true;
            sendBtn.textContent = 'Sending...';
            
            addMessage('user', message);
            input.value = '';

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: message})
                });
                const data = await response.json();
                addMessage('assistant', data.response || data.error);
            } catch (error) {
                addMessage('assistant', 'Sorry, I encountered an error.');
            } finally {
                sendBtn.disabled = false;
                sendBtn.textContent = 'Send';
            }
        }

        function addMessage(type, content) {
            const chatBox = document.getElementById('chat-box');
            const div = document.createElement('div');
            div.className = `message ${type}`;
            div.innerHTML = `<strong>${type === 'user' ? 'You' : 'Assistant'}:</strong> ${content}`;
            chatBox.appendChild(div);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>
    ''')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful business assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500
        )
        
        return jsonify({
            "response": response.choices[0].message.content
        })
    except Exception as e:
        logger.error(f"Chat error: {e}")
        return jsonify({"error": f"Error: {str(e)}"}), 500

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "chatgpt-business"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
