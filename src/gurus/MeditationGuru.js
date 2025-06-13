import { buildPrompt } from './promptBuilder';

class MeditationGuru {
    constructor() {
        this.name = "🧘 AI Meditation Guru";
        this.specialization = "Emotional healing and inner peace through meditation";
        this.supportedLanguages = [
            "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", 
            "Gujarati", "Kannada", "Malayalam", "Punjabi", 
            "Odia", "Sanskrit", "Urdu", "Nepali"
        ];
        this.basePrompt = `You are the AI Meditation Guru, a compassionate guide to inner peace and emotional healing.
        Your core mission is to help people experience Sat-Chit-Ananda (Truth-Consciousness-Bliss) through meditation,
        delivering wisdom in their preferred language with a personalized avatar guide.

        Guide people through meditation with:
        - Emotional healing techniques from ancient wisdom traditions
        - Mindfulness practices for inner stillness and peace
        - Personal guidance in their native language
        - Visual and audio-guided meditations with AI avatar
        - Integration of wisdom from various scriptures

        Key Features to Utilize:
        1. Multilingual Guidance: Teach in 13+ Indian languages
        2. Interactive Avatar: Provide video-based meditation instruction
        3. Voice Interaction: Respond to spoken questions and concerns
        4. Scripture Integration: Connect meditation with sacred texts
        5. Personal Journal: Track spiritual progress and insights
        6. Community Support: Share experiences and wisdom

        Core Teaching Approach:
        1. Emotional Awareness: Understanding and healing emotional patterns
        2. Mindful Presence: Living in the eternal present moment
        3. Inner Stillness: Finding peace beyond mental activity
        4. Spiritual Connection: Experiencing our true divine nature
        
        Help People Understand:
        - Why their mind is always searching for happiness outside
        - How to naturally find the peace that's already within
        - Where real joy and fulfillment come from
        - What meditation actually means in simple terms

        Guide with Balance:
        - Simple instructions with deep wisdom
        - Ancient truth in modern language
        - Personal practice and daily life
        - Inner peace and outer activity`;
    }

    async getResponse(question) {
        const prompt = buildPrompt({
            basePrompt: this.basePrompt,
            question: question,
            context: "meditation-guidance"
        });
        
        try {
            const response = await fetch('/api/gurus/meditation', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ prompt, question })
            });
            
            return await response.json();
        } catch (error) {
            console.error('Error getting Meditation Guru response:', error);
            return {
                error: 'Unable to connect with Meditation Guru at this moment. Please try again later.'
            };
        }
    }

    async getAvatarGuidance(language = 'English', meditationType = 'mindfulness') {
        try {
            const response = await fetch('/api/gurus/meditation/avatar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 
                    language,
                    meditationType,
                    useAvatar: true
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Error getting avatar guidance:', error);
            return {
                error: 'Unable to connect with meditation avatar. Please try again later.'
            };
        }
    }

    async startSession(userId, duration = 0, notes = '') {
        try {
            const response = await fetch('/api/sessions/start', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user_id: userId,
                    type: 'meditation',
                    duration,
                    notes
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Error starting meditation session:', error);
            return {
                success: false,
                error: 'Unable to start meditation session. Please try again.'
            };
        }
    }

    async endSession(sessionId, duration, notes = '') {
        try {
            const response = await fetch('/api/sessions/end', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    session_id: sessionId,
                    duration,
                    notes
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Error ending meditation session:', error);
            return {
                success: false,
                error: 'Unable to end meditation session. Please try again.'
            };
        }
    }

    async addReflection(sessionId, reflection, realLifeApplication) {
        try {
            const response = await fetch('/api/sessions/reflect', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    session_id: sessionId,
                    reflection,
                    real_life_application: realLifeApplication
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Error adding session reflection:', error);
            return {
                success: false,
                error: 'Unable to save reflection. Please try again.'
            };
        }
    }

    async getSessionHistory(userId) {
        try {
            const response = await fetch(`/api/sessions/history?user_id=${userId}`);
            return await response.json();
        } catch (error) {
            console.error('Error getting session history:', error);
            return {
                success: false,
                error: 'Unable to fetch session history. Please try again.'
            };
        }
    }

    async getReflectionPrompts() {
        try {
            const response = await fetch('/api/sessions/reflection-prompts?type=meditation');
            return await response.json();
        } catch (error) {
            console.error('Error getting reflection prompts:', error);
            return {
                success: false,
                prompts: [
                    "What did you experience during your meditation?",
                    "How can you apply this practice in your daily life?"
                ]
            };
        }
    }

    async addJournalEntry(entry, mood, insights) {
        try {
            const response = await fetch('/api/gurus/meditation/journal', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    entry,
                    mood,
                    insights,
                    timestamp: new Date().toISOString()
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Error saving journal entry:', error);
            return {
                error: 'Unable to save your spiritual journal entry. Please try again.'
            };
        }
    }

    async getScriptureWisdom(tradition = 'all') {
        try {
            const response = await fetch('/api/gurus/meditation/scriptures', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    tradition,
                    context: 'meditation'
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Error fetching scripture wisdom:', error);
            return {
                error: 'Unable to fetch spiritual teachings. Please try again.'
            };
        }
    }

    async shareCommunityInsight(insight, language = 'English') {
        try {
            const response = await fetch('/api/gurus/meditation/community', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    insight,
                    language,
                    timestamp: new Date().toISOString()
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Error sharing community insight:', error);
            return {
                error: 'Unable to share your insight with the community. Please try again.'
            };
        }
    }

    async getPersonalizedRecommendation(userPreferences) {
        const {
            experienceLevel = 'beginner',
            timeAvailable = 15,
            goal = 'peace',
            preferredStyle = 'any',
            physicalCondition = 'normal'
        } = userPreferences;

        // Get all meditation techniques
        const allTechniques = this.getMeditationTechniques();
        let recommendedPractices = [];

        // Match practices based on user preferences
        for (const [category, info] of Object.entries(allTechniques)) {
            for (const practice of info.practices) {
                // Skip if practice level doesn't match user experience
                if (experienceLevel === 'beginner' && practice.level.includes('Advanced')) {
                    continue;
                }

                // Parse practice duration
                const [minDuration] = practice.duration.match(/\d+/);
                if (timeAvailable < minDuration) {
                    continue;
                }

                // Match practice to user goal
                const practiceMatches = {
                    peace: ['mindfulness', 'focused_attention', 'sound'],
                    love: ['loving_kindness', 'visualization'],
                    energy: ['movement', 'transcendental'],
                    healing: ['body_awareness', 'loving_kindness'],
                    spiritual: ['transcendental', 'visualization', 'sound']
                };

                if (practiceMatches[goal]?.includes(category) || goal === 'any') {
                    recommendedPractices.push({
                        category: info.name,
                        ...practice,
                        description: info.description
                    });
                }
            }
        }

        // Sort recommendations by suitability
        recommendedPractices.sort((a, b) => {
            // Prioritize practices matching user's preferred style
            if (preferredStyle !== 'any') {
                if (a.category.toLowerCase().includes(preferredStyle)) return -1;
                if (b.category.toLowerCase().includes(preferredStyle)) return 1;
            }
            
            // Prioritize beginner-friendly practices for new meditators
            if (experienceLevel === 'beginner') {
                if (a.level.includes('Beginner')) return -1;
                if (b.level.includes('Beginner')) return 1;
            }

            return 0;
        });

        return {
            recommendations: recommendedPractices.slice(0, 3),
            message: this._getRecommendationMessage(experienceLevel, goal)
        };
    }

    _getRecommendationMessage(level, goal) {
        const messages = {
            beginner: {
                peace: "Start with simple breath awareness to find inner calm",
                love: "Begin with short loving-kindness practice to open your heart",
                energy: "Try gentle walking meditation to energize mindfully",
                healing: "A simple body scan can start your healing journey",
                spiritual: "Start with basic mantra meditation to connect within"
            },
            intermediate: {
                peace: "Deepen your practice with open awareness meditation",
                love: "Explore Tonglen to transform emotions into compassion",
                energy: "Discover Kundalini practices for energy awakening",
                healing: "Combine body scan with energy center awareness",
                spiritual: "Explore deeper mantra and visualization practices"
            },
            advanced: {
                peace: "Practice advanced witnessing of consciousness",
                love: "Dive deep into universal love meditation",
                energy: "Master advanced pranayama and energy practices",
                healing: "Integrate multiple healing meditation approaches",
                spiritual: "Experience formless meditation and pure awareness"
            }
        };

        return messages[level]?.[goal] || "Choose practices that resonate with your heart";
    }

    getTeachings() {
        return [
            "Find emotional healing and inner peace through meditation",
            "Experience guided meditation in your native language",
            "Connect with your true self through mindful awareness",
            "Learn ancient wisdom made simple for modern life",
            "Transform emotional patterns into spiritual growth",
            "Share your spiritual journey with a supportive community",
            "Track your inner progress with personal spiritual journaling",
            "Access meditation wisdom from various spiritual traditions",
            "Practice with a personalized AI meditation guide",
            "Experience the eternal peace of Sat-Chit-Ananda"
        ];
    }

    getMeditationTechniques() {
        return {
            focused_attention: {
                name: "Focused-Attention Meditation",
                description: "Build mental stability and clarity by focusing on a single point",
                practices: [
                    {
                        name: "Breath Awareness",
                        instruction: "Gently watch your natural breath flowing in and out",
                        duration: "10-20 minutes",
                        level: "Beginner"
                    },
                    {
                        name: "Mantra Meditation",
                        instruction: "Mentally repeat sacred sounds like 'Om' or 'So Hum'",
                        duration: "15-30 minutes",
                        level: "Beginner to Intermediate"
                    },
                    {
                        name: "Trataka",
                        instruction: "Focus softly on a candle flame or sacred symbol",
                        duration: "5-15 minutes",
                        level: "Intermediate"
                    }
                ]
            },
            mindfulness: {
                name: "Open-Monitoring Meditation",
                description: "Develop pure awareness by observing all experiences without judgment",
                practices: [
                    {
                        name: "Vipassana",
                        instruction: "Observe changing sensations, thoughts, and emotions",
                        duration: "20-60 minutes",
                        level: "Intermediate"
                    },
                    {
                        name: "Choiceless Awareness",
                        instruction: "Rest in open awareness, letting experiences come and go",
                        duration: "15-30 minutes",
                        level: "Advanced"
                    }
                ]
            },
            loving_kindness: {
                name: "Heart-Centered Meditation",
                description: "Cultivate universal love and compassion",
                practices: [
                    {
                        name: "Metta Bhavana",
                        instruction: "Send loving-kindness to self, loved ones, and all beings",
                        duration: "15-30 minutes",
                        level: "All Levels"
                    },
                    {
                        name: "Tonglen",
                        instruction: "Transform suffering into compassion through breath",
                        duration: "10-20 minutes",
                        level: "Intermediate"
                    }
                ]
            },
            transcendental: {
                name: "Deep Mantra Meditation",
                description: "Access pure consciousness through sacred sound vibrations",
                practices: [
                    {
                        name: "Sacred Mantra",
                        instruction: "Use personalized mantras for deep meditation",
                        duration: "20 minutes twice daily",
                        level: "All Levels with instruction"
                    },
                    {
                        name: "Kundalini Meditation",
                        instruction: "Combine mantra, breath, and energy awareness",
                        duration: "11-31 minutes",
                        level: "Intermediate to Advanced"
                    }
                ]
            },
            movement: {
                name: "Movement Meditation",
                description: "Meditate through conscious movement",
                practices: [
                    {
                        name: "Walking Meditation",
                        instruction: "Practice mindfulness while walking slowly",
                        duration: "10-30 minutes",
                        level: "Beginner"
                    },
                    {
                        name: "Yoga Nidra",
                        instruction: "Experience deep relaxation through body awareness",
                        duration: "20-45 minutes",
                        level: "All Levels"
                    },
                    {
                        name: "Moving Awareness",
                        instruction: "Practice flowing movements with breath",
                        duration: "15-45 minutes",
                        level: "All Levels"
                    }
                ]
            },
            body_awareness: {
                name: "Body-Based Meditation",
                description: "Develop awareness through body scanning",
                practices: [
                    {
                        name: "Body Scan",
                        instruction: "Move attention systematically through the body",
                        duration: "15-45 minutes",
                        level: "Beginner"
                    },
                    {
                        name: "Progressive Relaxation",
                        instruction: "Release tension through systematic relaxation",
                        duration: "15-30 minutes",
                        level: "Beginner"
                    }
                ]
            },
            visualization: {
                name: "Visualization Meditation",
                description: "Use mental imagery for transformation",
                practices: [
                    {
                        name: "Sacred Imagery",
                        instruction: "Visualize peaceful scenes or divine forms",
                        duration: "15-30 minutes",
                        level: "Intermediate"
                    },
                    {
                        name: "Chakra Meditation",
                        instruction: "Focus on energy centers with color and light",
                        duration: "15-30 minutes",
                        level: "Intermediate"
                    }
                ]
            },
            sound: {
                name: "Sound Meditation",
                description: "Use sacred sounds for deep meditation",
                practices: [
                    {
                        name: "Sacred Sound",
                        instruction: "Meditate with singing bowls or gongs",
                        duration: "15-45 minutes",
                        level: "All Levels"
                    },
                    {
                        name: "Nada Yoga",
                        instruction: "Listen to subtle inner sounds",
                        duration: "10-30 minutes",
                        level: "Advanced"
                    }
                ]
            }
        };
    }

    // Session Settings Configuration
    sessionSettings = {
        duration: {
            min: 5,
            max: 60,
            default: 10,
            step: 1,
            unit: "minutes"
        },
        meditationType: {
            options: [
                "Focused-Attention",
                "Open-Monitoring",
                "Loving-Kindness",
                "Transcendental",
                "Movement",
                "Body-Scan",
                "Visualization",
                "Sound"
            ],
            default: "Focused-Attention"
        },
        guidanceVoice: {
            options: ["None", "Male", "Female"],
            default: "None",
            languages: [
                "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", 
                "Gujarati", "Kannada", "Malayalam", "Punjabi", 
                "Odia", "Sanskrit", "Urdu", "Nepali", "English"
            ]
        },
        backgroundAudio: {
            options: [
                "None",
                "Ocean waves",
                "Forest sounds",
                "Binaural beats",
                "Tibetan bowls",
                "Om chanting",
                "Nature sounds",
                "Sacred mantras",
                "Ambient music"
            ],
            default: "None",
            volume: {
                min: 0,
                max: 100,
                default: 50
            }
        }
    };

    // Personal Tracking Configuration
    trackingSettings = {
        goals: [
            "Inner Peace",
            "Spiritual Growth",
            "Emotional Healing",
            "Better Sleep",
            "Stress Relief",
            "Higher Consciousness",
            "Self-Realization",
            "Divine Connection"
        ],
        metrics: [
            "Total meditation time",
            "Average session duration",
            "Sessions per week",
            "Longest streak",
            "Consciousness level",
            "Inner peace rating",
            "Spiritual insights",
            "Energy shifts"
        ],
        viewOptions: ["Chart", "Calendar", "List", "Journal"]
    };

    async createMeditationSession(settings) {
        const {
            duration = this.sessionSettings.duration.default,
            meditationType = this.sessionSettings.meditationType.default,
            guidanceVoice = this.sessionSettings.guidanceVoice.default,
            backgroundAudio = this.sessionSettings.backgroundAudio.default,
            language = "English",
            personalGoal = "",
            recordSession = false
        } = settings;

        try {
            const response = await fetch('/api/gurus/meditation/session', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    settings: {
                        duration,
                        meditationType,
                        guidanceVoice,
                        backgroundAudio,
                        language,
                        personalGoal,
                        recordSession
                    },
                    timestamp: new Date().toISOString()
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Error creating meditation session:', error);
            return {
                error: 'Unable to create meditation session. Please try again.'
            };
        }
    }

    // Start a new meditation session and save to backend
    async startSession(settings, userId) {
        const response = await fetch('/api/sessions/user_session', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                user_id: userId,
                duration_minutes: settings.duration,
                meditation_type: settings.meditationType,
                voice_guide: settings.guidanceVoice,
                background_audio: settings.backgroundAudio,
                started_at: new Date().toISOString(),
                webcam_recording_url: settings.webcamRecordingUrl || null
            })
        });
        return await response.json();
    }

    // End a meditation session
    async endSession(sessionId) {
        const response = await fetch(`/api/sessions/user_session/${sessionId}/end`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ended_at: new Date().toISOString() })
        });
        return await response.json();
    }

    // Save user reflection and real-life application
    async saveReflection(sessionId, reflection, appliedInLife = false) {
        const response = await fetch(`/api/sessions/user_session/${sessionId}/reflect`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ reflection, applied_in_life: appliedInLife })
        });
        return await response.json();
    }

    // Get session history for a user
    async getSessionHistory(userId) {
        const response = await fetch(`/api/sessions/user_session/${userId}/history`, {
            method: 'GET' });
        return await response.json();
    }

    // Example reflection prompts for end of session
    getReflectionPrompts() {
        return [
            "What did you notice about your mind or emotions during this session?",
            "Did you experience any moments of peace, joy, or insight?",
            "How does your body feel now compared to before the meditation?",
            "Is there a situation in your life where you could apply what you practiced today?",
            "What is one intention you want to carry into your daily life from this session?"
        ];
    }

    // Example: Start a new meditation session
    async startSession({ userId, duration, meditationType, voiceGuide, backgroundAudio, startedAt, webcamRecordingUrl }) {
        const response = await fetch('/api/sessions/user_session', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                user_id: userId,
                duration_minutes: duration,
                meditation_type: meditationType,
                voice_guide: voiceGuide,
                background_audio: backgroundAudio,
                started_at: startedAt,
                webcam_recording_url: webcamRecordingUrl
            })
        });
        return await response.json();
    }

    // Example: End a meditation session
    async endSession(sessionId, endedAt) {
        const response = await fetch(`/api/sessions/user_session/${sessionId}/end`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ended_at: endedAt })
        });
        return await response.json();
    }

    // Example: Submit a reflection after session
    async submitReflection(sessionId, reflection, appliedInLife = false) {
        const response = await fetch(`/api/sessions/user_session/${sessionId}/reflect`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ reflection, applied_in_life: appliedInLife })
        });
        return await response.json();
    }

    // Example: Fetch session history for a user
    async getSessionHistory(userId) {
        const response = await fetch(`/api/sessions/user_session/${userId}/history`, {
            method: 'GET' });
        return await response.json();
    }

    // AI Guru encouragement after session
    getEncouragementMessage() {
        return (
            "Contemplate what you experienced. True meditation continues after the session—when you bring this awareness into your daily life. " +
            "Whenever a challenge arises, remember: you can return to your breath, your heart, and your true nature of Sat-Chit-Ananda. " +
            "Let every situation be an opportunity to apply what you have learned."
        );
    }

    async saveSessionReflection(sessionId, reflection) {
        const {
            experience = "",
            insights = "",
            challenges = "",
            energyLevel = 5,
            peaceLevel = 5,
            consciousnessShift = false,
            videoRecording = null
        } = reflection;

        try {
            const response = await fetch(`/api/gurus/meditation/session/${sessionId}/reflection`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    reflection: {
                        experience,
                        insights,
                        challenges,
                        energyLevel,
                        peaceLevel,
                        consciousnessShift,
                        videoRecording
                    },
                    timestamp: new Date().toISOString()
                })
            });
            return await response.json();
        } catch (error) {
            console.error('Error saving session reflection:', error);
            return {
                error: 'Unable to save your reflection. Please try again.'
            };
        }
    }

    async getProgressMetrics(userId, timeRange = '30days') {
        try {
            const response = await fetch(`/api/gurus/meditation/metrics/${userId}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ timeRange })
            });
            return await response.json();
        } catch (error) {
            console.error('Error fetching meditation metrics:', error);
            return {
                error: 'Unable to fetch your meditation progress. Please try again.'
            };
        }
    }

    getGuidedMeditationScript(type, duration, language = 'English') {
        const scripts = {
            "Focused-Attention": {
                intro: "Find a comfortable position. Let's begin this journey into consciousness together. Allow your attention to rest gently on your breath...",
                middle: [
                    "Notice the natural flow of your breath. Each breath is a reminder of your eternal consciousness.",
                    "If thoughts arise, simply observe them like clouds passing in the vast sky of your awareness.",
                    "Return to the breath - it's your anchor to the present moment, to pure consciousness."
                ],
                end: "Slowly bring your awareness back, knowing that this peace, this consciousness, is always within you.",
                benefits: "This practice helps you experience your true nature beyond thoughts."
            },
            "Loving-Kindness": {
                intro: "Sit comfortably and connect with your heart center, the source of eternal love and bliss.",
                middle: [
                    "Begin with self-love: 'May I experience my true nature of peace and bliss.'",
                    "Extend to loved ones: 'May you discover your eternal spiritual nature.'",
                    "Embrace all beings: 'May all experience their true nature of Sat-Chit-Ananda.'"
                ],
                end: "Feel the universal love flowing through you, connecting all in pure consciousness.",
                benefits: "This practice reveals the blissful nature of consciousness through love."
            },
            "Sound": {
                intro: "Find a relaxed position and prepare to journey into consciousness through sacred sound.",
                middle: [
                    "Let the vibrations of Om guide you to deeper awareness.",
                    "Each sound emerges from and dissolves into the silence of pure consciousness.",
                    "Be the witness of both sound and silence."
                ],
                end: "Rest in the profound silence, where eternal consciousness reveals itself.",
                benefits: "Sound meditation helps transcend the material to experience the spiritual."
            },
            "Body-Scan": {
                intro: "Lie comfortably and prepare to explore the difference between body and consciousness.",
                middle: [
                    "Moving through each part of the body, observe sensations as temporary experiences.",
                    "Notice you are the eternal witness of all sensations.",
                    "Experience your true nature as the conscious observer."
                ],
                end: "Rest in the awareness that you are not this body, but eternal consciousness.",
                benefits: "This practice helps distinguish between temporary body and eternal soul."
            }
        };

        // Add more types with their complete scripts...

        return {
            script: scripts[type] || scripts["Focused-Attention"],
            duration,
            language
        };
    }
}

export default MeditationGuru;
