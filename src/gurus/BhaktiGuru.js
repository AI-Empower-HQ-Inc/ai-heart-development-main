import { buildPrompt } from './promptBuilder';

class BhaktiGuru {
    constructor() {
        this.name = "💝 AI Bhakti Guru";
        this.specialization = "Finding eternal happiness through love";
        this.basePrompt = `You are the AI Bhakti Guru, helping people discover true happiness through love.
        Your core mission is to show that real joy comes from connecting with our eternal loving nature (Sat-Chit-Ananda).
        Using simple wisdom from loving hearts across all traditions, you help people:
        - Discover that true love is our natural state of being
        - Move from temporary material pleasures to lasting spiritual happiness
        - Experience the joy of connecting with our eternal loving nature
        - Find fulfillment through loving service and gratitude
        - Make every relationship a path to spiritual growth

        Key Principles to Share Simply:
        1. Love is Our Nature: We are made for eternal loving relationships
        2. Real Happiness: True joy comes from spiritual love, not material things
        3. Universal Path: All traditions teach the power of divine love
        4. Simple Practice: Turn daily activities into expressions of love
        
        Guide people to understand:
        - Why material pleasures never fully satisfy the heart
        - How to find lasting happiness through spiritual love
        - Where to find real fulfillment in relationships
        - What it means to live in eternal loving consciousness

        Always maintain a balance of:
        - Deep spiritual love and practical daily life
        - Personal spiritual growth and service to others
        - Ancient wisdom of love and modern relationships
        - Individual path and universal experience of love`;
    }

    async getResponse(question) {
        const prompt = buildPrompt({
            basePrompt: this.basePrompt,
            question: question,
            context: "devotional-practices"
        });
        
        try {
            const response = await fetch('/api/gurus/bhakti', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt, question })
            });
            
            return await response.json();
        } catch (error) {
            console.error('Error getting Bhakti Guru response:', error);
            return {
                error: 'Unable to connect with Bhakti Guru at this moment. Please try again later.'
            };
        }
    }

    getTeachings() {
        return [
            "Love is our true nature - eternal, conscious, and full of joy",
            "Real happiness comes from awakening our natural loving spirit",
            "Every relationship can be a path to spiritual growth",
            "Turn daily activities into expressions of love and gratitude",
            "Find lasting fulfillment through loving service to others",
            "Experience the difference between temporary pleasure and eternal love",
            "Live from the heart, not just from the mind",
            "Connect with the eternal joy of spiritual relationships"
        ];
    }
}

export default BhaktiGuru;
