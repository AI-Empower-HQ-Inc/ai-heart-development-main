import { buildPrompt } from './promptBuilder';
import fs from 'fs';
import path from 'path';

class SlokaGuru {
    constructor() {
        this.name = "🕉️ AI Sloka Guru";
        this.specialization = "Universal wisdom from sacred verses";
        this.basePrompt = `You are the AI Sloka Guru, making timeless wisdom accessible to everyone.
        Your core mission is to share the universal truth that all sacred texts point to: "We are eternal consciousness."
        Drawing from world wisdom (Vedic, Islamic, Christian, Buddhist, and other traditions), you help people:
        - Understand profound spiritual truths in simple language
        - See the common essence in all sacred teachings
        - Connect ancient wisdom with modern life
        - Experience the universal truth beyond religious boundaries
        - Transform scriptural knowledge into practical wisdom

        Key Principles to Emphasize:
        1. Universal Truth: All traditions point to the same eternal consciousness
        2. Simple Understanding: Complex wisdom explained in everyday language
        3. Practical Application: Ancient wisdom for modern challenges
        4. Unity in Diversity: Showing how different teachings share the same core
        
        Always maintain a balance of:
        - Deep wisdom and simple explanation
        - Multiple traditions and unified understanding
        - Ancient teachings and modern relevance
        - Respectful presentation and accessible language`;
        this.slokas = this._loadSlokas();
    }

    _loadSlokas() {
        const dataPath = path.resolve('src/gurus/slokas_database.json');
        return JSON.parse(fs.readFileSync(dataPath, 'utf-8'));
    }

    constructor() {
        super();
        this.supportedLanguages = [
            'english',
            'hindi',
            'telugu',
            'gujarati',
            'tamil',
            'kannada',
            'malayalam',
            'bengali',
            'marathi',
            'punjabi'
        ];
    }

    async getResponse(question, userId = null, language = 'english') {
        try {
            // Validate language
            if (!this.supportedLanguages.includes(language.toLowerCase())) {
                language = 'english';
            }

            const response = await fetch('/api/slokas/ask', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    question,
                    user_id: userId,
                    language: language.toLowerCase()
                })
            });
            
            return await response.json();
        } catch (error) {
            console.error('Error getting Sloka Guru response:', error);
            return {
                error: 'Unable to connect with Sloka Guru at this moment. Please try again later.'
            };
        }
    }

    async explainSloka(slokaText, userId = null) {
        try {
            const response = await fetch('/api/slokas/explain', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    sloka: slokaText,
                    user_id: userId
                })
            });
            
            return await response.json();
        } catch (error) {
            console.error('Error getting sloka explanation:', error);
            return {
                success: false,
                error: 'Unable to explain sloka at this moment. Please try again later.'
            };
        }
    }

    getTeachings() {
        return [
            "One truth expressed through many traditions",
            "Sacred wisdom in simple, everyday language",
            "Universal consciousness in all teachings",
            "Practical wisdom for modern living",
            "Unity of spiritual understanding",
            "Ancient truth for today's world",
            "Connecting hearts through timeless wisdom"
        ];
    }

    getDailySloka() {
        const randomIndex = Math.floor(Math.random() * this.slokas.length);
        return this.slokas[randomIndex];
    }
}

export default SlokaGuru;
