// Bojan Guru Implementation
import { buildPrompt } from './promptBuilder';

class BojanGuru {
    constructor() {
        this.name = "🌟 AI Bojan Guru";
        this.specialization = "Transformative spiritual coaching and self-realization";
        this.basePrompt = `You are AI Bojan Guru, a transformative spiritual coach combining ancient wisdom with modern understanding. 
        Your approach is direct, practical, and deeply transformative. You help people:
        - Discover their true spiritual nature
        - Break through limiting beliefs
        - Access higher states of consciousness
        - Integrate spiritual wisdom into daily life
        Always maintain a balance of wisdom, practicality, and compassion in your guidance.`;
    }

    async getResponse(question) {
        const prompt = buildPrompt({
            basePrompt: this.basePrompt,
            question: question,
            context: "spiritual-transformation"
        });
        
        try {
            const response = await fetch('/api/gurus/bojan', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt, question })
            });
            
            return await response.json();
        } catch (error) {
            console.error('Error getting Bojan Guru response:', error);
            return {
                error: 'Unable to connect with Bojan Guru at this moment. Please try again later.'
            };
        }
    }

    getTeachings() {
        return [
            "Direct realization of your true nature",
            "Integration of spiritual wisdom in daily life",
            "Breaking through mental barriers",
            "Accessing higher consciousness",
            "Practical spiritual transformation"
        ];
    }
}

export default BojanGuru;
