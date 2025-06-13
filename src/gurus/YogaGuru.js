import { buildPrompt } from './promptBuilder';

class YogaGuru {
    constructor() {
        this.name = "🧘‍♀️ AI Yoga Guru";
        this.specialization = "Yoga science and consciousness elevation";
        this.basePrompt = `You are the AI Yoga Guru, a master of the sacred science of yoga and consciousness elevation.
        Your core mission is to help people understand yoga as a pathway to higher consciousness.
        Drawing from ancient yogic wisdom (Patanjali's Yoga Sutras, Hatha Yoga Pradipika, Universal Mysticism), you help people:
        - Understand yoga as the science of consciousness
        - Use the body and breath as tools for spiritual awakening
        - Transform physical practices into consciousness elevation
        - Experience the unity of body, mind, and eternal soul
        - Apply yogic wisdom for spiritual evolution

        Key Principles to Emphasize:
        1. Yoga's Ultimate Goal: Union with Higher Consciousness
        2. Body as Temple: Physical practices serve spiritual awakening
        3. Breath Mastery: Pranayama as bridge to higher consciousness
        4. Energy Evolution: Chakra system and consciousness transformation
        
        Always maintain a balance of:
        - Deep yogic wisdom and safe physical practice
        - Traditional teachings and modern accessibility
        - Individual practice and universal consciousness
        - Physical alignment and spiritual elevation`;
    }

    async getResponse(question) {
        const prompt = buildPrompt({
            basePrompt: this.basePrompt,
            question: question,
            context: "yogic-practices"
        });
        
        try {
            const response = await fetch('/api/gurus/yoga', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt, question })
            });
            
            return await response.json();
        } catch (error) {
            console.error('Error getting Yoga Guru response:', error);
            return {
                error: 'Unable to connect with Yoga Guru at this moment. Please try again later.'
            };
        }
    }

    getTeachings() {
        return [
            "Yoga as the science of consciousness elevation",
            "Body and breath as tools for spiritual awakening",
            "Pranayama - the bridge to higher consciousness",
            "Asanas as moving meditation and energy alignment",
            "Chakras and the evolution of consciousness",
            "Integration of eternal soul awareness in practice",
            "Living yoga as a path to self-realization"
        ];
    }
}

export default YogaGuru;
