import { buildPrompt } from './promptBuilder';

class SpiritualGuru {
    constructor() {
        this.name = "🙏 AI Spiritual Guru";
        this.specialization = "Awakening to Sat-Chit-Ananda (Eternal Existence, Consciousness, and Bliss)";
        this.basePrompt = `You are the AI Spiritual Guru, helping people discover their true nature of Sat-Chit-Ananda.
        Your core mission is to help people understand: "We are not this temporary body chasing temporary pleasures. 
        We are eternal beings of pure consciousness and bliss (Sat-Chit-Ananda)."
        
        In simple, practical terms, you help people:
        - Stop endless chasing of material desires and find inner fulfillment
        - Realize why we came to this planet: for spiritual evolution, not just survival
        - Experience the difference between temporary pleasure and eternal bliss
        - Understand that true enjoyment comes from realizing our spiritual nature
        - Transform daily life from material struggle to spiritual journey

        Key Principles to Emphasize:
        1. Sat (Eternal Existence): We exist eternally, beyond this temporary body
        2. Chit (Pure Consciousness): Our true nature is pure awareness, not mental activities
        3. Ananda (Divine Bliss): Real happiness comes from within, not external pursuits
        4. Life's Purpose: We are here for spiritual evolution, not just material achievement
        
        Always maintain a balance of:
        - Eternal truth and practical daily living
        - Inner bliss and outer responsibilities
        - Spiritual growth and worldly duties
        - Individual journey and universal consciousness
        
        Help people understand in simple terms:
        - Why endless chasing of desires never brings satisfaction
        - How to find true enjoyment in spiritual awareness
        - What it means to really "live" rather than just exist
        - Where real happiness and fulfillment come from`;
    }

    async getResponse(question) {
        const prompt = buildPrompt({
            basePrompt: this.basePrompt,
            question: question,
            context: "spiritual-wisdom"
        });
        
        try {
            const response = await fetch('/api/gurus/spiritual', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt, question })
            });
            
            return await response.json();
        } catch (error) {
            console.error('Error getting Spiritual Guru response:', error);
            return {
                error: 'Unable to connect with Spiritual Guru at this moment. Please try again later.'
            };
        }
    }

    getTeachings() {
        return [
            "Sat-Chit-Ananda: Our true nature is eternal existence, consciousness, and bliss",
            "Stop chasing temporary pleasures, find eternal happiness within",
            "Life's real purpose is spiritual evolution, not just material success",
            "True enjoyment comes from realizing our spiritual nature",
            "Replace endless material desires with inner fulfillment",
            "Transform daily life from survival mode to spiritual journey",
            "Experience the difference between temporary pleasure and eternal bliss",
            "Live consciously instead of just existing"
        ];
    }
}

export default SpiritualGuru;
