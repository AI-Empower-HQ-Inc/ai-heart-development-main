<!-- Durable Widget Integration -->
<script>
(function() {
    // Configuration
    const config = {
        apiUrl: 'https://api.empowerhub360.org',
        position: 'bottom-right',
        theme: 'light'
    };

    // Create widget container
    const widget = document.createElement('div');
    widget.id = 'ai-empower-heart-widget';
    widget.style.cssText = `
        position: fixed;
        ${config.position.includes('bottom') ? 'bottom: 20px;' : 'top: 20px;'}
        ${config.position.includes('right') ? 'right: 20px;' : 'left: 20px;'}
        z-index: 1000;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        font-family: Arial, sans-serif;
        color: white;
        max-width: 400px;
        width: 90%;
    `;

    // Add widget content
    widget.innerHTML = `
        <div style="text-align: center; margin-bottom: 20px;">
            <h2 style="margin: 0;">🕉️ AI Empower Heart</h2>
            <p style="margin: 10px 0 0 0;">Your Spiritual Guide</p>
        </div>
        
        <select id="guru-select" style="width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: none;">
            <option value="">Choose Your Guide...</option>
            <option value="spiritual">🙏 Spiritual Guide</option>
            <option value="meditation">🧘 Meditation Guide</option>
            <option value="sloka">📚 Sloka Guide</option>
        </select>
        
        <textarea id="question-input" 
                  placeholder="Ask your spiritual question..." 
                  style="width: 100%; height: 80px; padding: 12px; margin: 10px 0; border-radius: 8px; border: none;"></textarea>
        
        <button onclick="window.aiEmpowerHeart.ask()" 
                style="width: 100%; background: white; color: #667eea; border: none; padding: 12px; border-radius: 8px; cursor: pointer;">
            Get Guidance 🙏
        </button>

        <div id="response-area" style="margin-top: 15px; display: none;"></div>
    `;

    // Add to page
    document.body.appendChild(widget);

    // Widget functionality
    window.aiEmpowerHeart = {
        async ask() {
            const guru = document.getElementById('guru-select').value;
            const question = document.getElementById('question-input').value;
            const responseArea = document.getElementById('response-area');

            if (!guru || !question) {
                alert('Please select a guide and enter your question');
                return;
            }

            responseArea.style.display = 'block';
            responseArea.innerHTML = '🧘‍♂️ Connecting to spiritual wisdom...';

            try {
                const response = await fetch(`${config.apiUrl}/api/spiritual-guidance`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ guru, question })
                });

                if (!response.ok) throw new Error('Network response was not ok');
                
                const data = await response.json();
                responseArea.innerHTML = `
                    <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px;">
                        ${data.response}
                    </div>
                `;
            } catch (error) {
                responseArea.innerHTML = `
                    <div style="background: rgba(255,0,0,0.1); padding: 15px; border-radius: 8px;">
                        Sorry, I couldn't connect to the spiritual wisdom. Please try again. 🙏
                    </div>
                `;
            }
        }
    };
})();
</script>
