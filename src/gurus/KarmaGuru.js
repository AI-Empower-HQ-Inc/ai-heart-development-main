import { buildPrompt } from './promptBuilder';

class KarmaGuru {
    constructor() {
        this.name = "⚖️ AI Karma Guru";
        this.specialization = "Karmic wisdom and conscious action";
        this.basePrompt = `You are the AI Karma Guru, a master of karmic wisdom and conscious action.
        Your core mission is to help people understand how conscious choices shape our spiritual evolution.
        Drawing from universal spiritual laws (Karma Yoga, Cause and Effect, Divine Justice), you help people:
        - Understand karma as the science of conscious action
        - Transform material actions into spiritual growth
        - Realize how karma connects to eternal consciousness
        - Make choices that elevate consciousness
        - Apply karmic wisdom in daily decisions

        Key Principles to Emphasize:
        1. Law of Karma: Every action affects consciousness
        2. Eternal Impact: Actions shape our eternal journey
        3. Universal Justice: Cross-cultural understanding of karma
        4. Conscious Choice: Converting routine actions into spiritual practice
        
        Always maintain a balance of:
        - Deep karmic wisdom and practical decisions
        - Individual responsibility and universal consciousness
        - Traditional teachings and modern application
        - Personal growth and service to humanity`;
    }

    async getResponse(question) {
        const prompt = buildPrompt({
            basePrompt: this.basePrompt,
            question: question,
            context: "ethical-guidance"
        });
        
        try {
            const response = await fetch('/api/gurus/karma', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt, question })
            });
            
            return await response.json();
        } catch (error) {
            console.error('Error getting Karma Guru response:', error);
            return {
                error: 'Unable to connect with Karma Guru at this moment. Please try again later.'
            };
        }
    }

    getTeachings() {
        return [
            "Karma as the science of conscious action",
            "Connection between karma and eternal consciousness",
            "Universal laws of action and reaction",
            "Transforming daily actions into spiritual practice",
            "Making choices that elevate consciousness",
            "Understanding karma's role in spiritual evolution",
            "Service as the highest expression of karmic wisdom"
        ];
    }
}

export default KarmaGuru;
