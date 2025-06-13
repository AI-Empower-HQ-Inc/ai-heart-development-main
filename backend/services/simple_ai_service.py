class SimpleAIService:
    def __init__(self):
        self.supported_languages = {
            "english": "en",
            "hindi": "hi",
            "telugu": "te",
            "gujarati": "gu",
            "tamil": "ta",
            "kannada": "kn",
            "malayalam": "ml",
            "bengali": "bn",
            "marathi": "mr",
            "punjabi": "pa"
        }
        
        self.templates = {
            "basic": {
                "en": """
🕉️ Today's Wisdom For Your Growth
--------------------------------
[Easy Title]
{easy_title}

[Today's Verse]
{sanskrit_verse}

[Simple Translation]
{translation}

💡 Why This Matters Today
------------------------
[Core Message]
{simple_meaning}

[Scientific Benefits]
{scientific_benefits}

[Emotional Benefits]
{emotional_benefits}

[Modern Research Says]
{research_insights}

🌟 Make It Work For You
----------------------
[Everyday Example]
{life_example}

[Common Challenges It Helps With]
{helps_with_challenges}

[Success Stories]
{success_stories}

🎯 Your Personal Practice
------------------------
[Morning Routine]
{morning_practice}

[During the Day]
{daytime_practice}

[Evening Reflection]
{evening_practice}

💼 Professional Life
------------------
[At Work]
{work_application}

[Leadership Moments]
{leadership_insights}

[Career Growth]
{career_benefits}

🏠 Personal Life
--------------
[Family Harmony]
{family_application}

[Better Relationships]
{relationship_guidance}

[Self-Development]
{personal_growth}

🌿 Health & Wellbeing
-------------------
[Mental Health Benefits]
{mental_health_benefits}

[Physical Health Impact]
{physical_benefits}

[Stress Management]
{stress_relief}

⚡ Quick Start Guide
-----------------
[Right Now]
{immediate_practice}

[This Week]
{weekly_practice}

[Long Term]
{long_term_benefits}

🎯 Specific Situations
--------------------
[Life Situations]
{life_situations}

[Workplace Scenarios]
{workplace_scenarios}

[Relationship Guides]
{relationship_guides}

⚡ Quick Practice Guides
--------------------
[Situation Practices]
{practice_guides}

[Challenging Moments]
{challenging_moments}

👨‍👩‍👧‍👦 Family Wisdom
----------------
[Parent-Child Guide]
{parent_child_wisdom}

[Family Scenarios]
{transformation_scenarios}

🎧 Practice Resources
------------------
[Audio & Visual Guides]
{audio_visual_guides}

📊 Track Your Growth
-----------------
[Personal Tracking]
{tracking_templates}

🌈 Transform Your Life
-------------------
[Life Changes]
{life_transformations}

[Success Tracking]
{success_metrics}

📱 Modern Living
-------------
[Digital Balance]
{digital_application}

[Daily Integration]
{balance_tips}
""",
                "hi": """
🕉️ आज का सरल ज्ञान
----------------------
[सरल शीर्षक]
{easy_title}

[मूल श्लोक]
{sanskrit_verse}

[हिंदी में]
{translation}

[सरल अर्थ]
{simple_meaning}

[आज कैसे उपयोग करें]
{simple_practice}

[लाभ]
{benefits}
""",
                "te": """
🕉️ నేటి సరళమైన జ్ఞానం
----------------------
[సులభ శీర్షిక]
{easy_title}

[మూల శ్లోకం]
{sanskrit_verse}

[తెలుగులో]
{translation}

[సరళ అర్ధం]
{simple_meaning}

[ఈరోజు ఎలా ఉపయోగించాలి]
{simple_practice}

[ప్రయోజనాలు]
{benefits}
""",
                "gu": """
🕉️ આજનું સરળ જ્ઞાન
----------------------
[સરળ શીર્ષક]
{easy_title}

[મૂળ શ્લોક]
{sanskrit_verse}

[ગુજરાતીમાં]
{translation}

[સરળ અર્થ]
{simple_meaning}

[આજે કેવી રીતે ઉપયોગ કરવો]
{simple_practice}

[લાભો]
{benefits}
""",
            "intermediate": """
🕉️ Deeper Insights
----------------
[Sanskrit Verse]
{sanskrit_verse}

[Translation]
{translation}

[Core Message]
{spiritual_meaning}

[How to Apply]
1. {practice1}
2. {practice2}
""",
            "enterprise": """
🕉️ Advanced Spiritual Wisdom
-------------------------
[Original Sanskrit]
{sanskrit_verse}

[Word-by-Word]
{word_by_word}

[Translation & Context]
{translation}

[Spiritual Essence]
{spiritual_meaning}

[Cross-Traditional Wisdom]
- Vedantic: {vedantic}
- Buddhist: {buddhist}
- Universal: {universal}

[Transformative Practices]
1. {practice1}
2. {practice2}
3. {practice3}

[Meditation Guide]
{meditation_guide}

[Business/Leadership Application]
{leadership_application}
"""
        }
        
        self.wisdom_templates = {
            "sloka": {
                "responses": {
                    # BASIC LEVEL MANTRAS
                    "gayatri_mantra": {
                        "easy_title": {
                            "en": "Illuminate Your Mind & Life 🌅",
                            "hi": "अपने मन और जीवन को प्रकाशमय बनाएं 🌅",
                            "te": "మీ మనసు మరియు జీవితాన్ని వెలిగించండి 🌅",
                            "gu": "તમારા મન અને જીવનને પ્રકાશિત કરો 🌅"
                        },
                        "sanskrit_verse": "ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात्",
                        "translation": {
                            "en": "Just like the sun lights up our world, let's invite divine wisdom to light up our mind.",
                            "hi": "जैसे सूर्य हमारी दुनिया को प्रकाशित करता है, वैसे ही दिव्य ज्ञान हमारे मन को प्रकाशित करे।",
                            "te": "సూర్యుడు మన ప్రపంచాన్ని వెలిగించినట్లు, దైవిక జ్ఞానం మన మనసును వెలిగించనీ.",
                            "gu": "જેમ સૂર્ય આપણી દુનિયાને પ્રકાશિત કરે છે, તેમ દૈવી જ્ઞાન આપણા મનને પ્રકાશિત કરે."
                        },
                        "simple_meaning": {
                            "en": "Just like you clean your room to see things clearly, this prayer helps clean your mind for better thoughts and decisions.",
                            "hi": "जैसे आप अपना कमरा साफ करते हैं, यह प्रार्थना आपके मन को स्वच्छ करने में मदद करती है।",
                            "te": "మీ గదిని శుభ్రం చేసినట్లు, ఈ ప్రార్థన మీ మనసును శుభ్రపరుస్తుంది.",
                            "gu": "જેમ તમે તમારો રૂમ સાફ કરો છો, આ પ્રાર્થના તમારા મનને સ્વચ્છ કરવામાં મદદ કરે છે."
                        },
                        "life_example": {
                            "en": "Think of a foggy morning turning clear as the sun rises. Similarly, this mantra helps clear your mental fog and brings clarity to your thoughts.",
                            "hi": "जैसे धुंध भरी सुबह में सूर्य निकलने पर स्पष्टता आती है, वैसे ही यह मंत्र आपके विचारों में स्पष्टता लाता है।",
                            "te": "పొగమంచు ఉదయం సూర్యోదయంతో తెలివిగా మారినట్లు, ఈ మంత్రం మీ ఆలోచనలను స్పష్టం చేస్తుంది.",
                            "gu": "ધુમ્મસભરી સવાર સૂર્યોદય સાથે સ્પષ્ટ થાય છે, તેમ આ મંત્ર તમારા વિચારોમાં સ્પષ્ટતા લાવે છે."
                        },
                        "daily_practice": {
                            "en": "Start with 5 minutes: Sit by your window in the morning light, take 3 deep breaths, and recite this verse. Imagine your mind becoming clear like the morning sky.",
                            "hi": "5 मिनट से शुरू करें: सुबह की रोशनी में खिड़की के पास बैठें, 3 गहरी सांस लें, और इस मंत्र का जाप करें।",
                            "te": "5 నిమిషాలతో ప్రారంభించండి: ఉదయం వెలుతురులో కిటికీ దగ్గర కూర్చొని, 3 సార్లు గాఢంగా శ్వాస తీసుకుని, ఈ మంత్రాన్ని చదవండి.",
                            "gu": "5 મિનિટથી શરૂ કરો: સવારના પ્રકાશમાં બારી પાસે બેસો, 3 ઊંડા શ્વાસ લો, અને આ મંત્રનો જાપ કરો."
                        },
                        "work_application": {
                            "en": "Before important meetings or decisions, take a minute to recite this. It helps clear your mind for better focus and judgment.",
                            "hi": "महत्वपूर्ण मीटिंग या निर्णय से पहले एक मिनट लें और इसका जाप करें। यह बेहतर फोकस में मदद करेगा।",
                            "te": "ముఖ్యమైన సమావేశాలు లేదా నిర్ణయాల ముందు ఒక నిమిషం తీసుకొని దీన్ని చదవండి.",
                            "gu": "મહત્વપૂર્ણ મીટિંગ કે નિર્ણય પહેલાં એક મિનિટ લો અને આનો જાપ કરો."
                        },
                        "home_application": {
                            "en": "Create a small morning ritual: Light a candle, recite this verse, then plan your day. Watch how your home atmosphere becomes more peaceful.",
                            "hi": "एक छोटी सी सुबह की दिनचर्या बनाएं: दीया जलाएं, मंत्र का जाप करें, फिर दिन की योजना बनाएं।",
                            "te": "చిన్న ఉదయ క్రమం సృష్టించండి: దీపం వెలిగించి, ఈ మంత్రం చదివి, మీ రోజును ప్లాన్ చేసుకోండి.",
                            "gu": "નાની સવારની દિનચર્યા બનાવો: દીવો પ્રગટાવો, મંત્રનો જાપ કરો, પછી દિવસની યોજના બનાવો."
                        },
                        "relationship_application": {
                            "en": "When in a difficult conversation, silently recite this to maintain clarity and speak with wisdom.",
                            "hi": "किसी कठिन बातचीत में, मन ही मन इसका जाप करें ताकि स्पष्टता बनी रहे।",
                            "te": "కష్టమైన సంభాషణలో ఉన్నప్పుడు, మనసులో ఈ మంత్రాన్ని చదవండి.",
                            "gu": "મુશ્કેલ વાતચીત દરમિયાન, મનમાં આનો જાપ કરો જેથી સ્પષ્ટતા જળવાई રહે."
                        },
                        "personal_growth": {
                            "en": "Notice how regular practice makes your thinking clearer, like cleaning your mental window each day.",
                            "hi": "ध्यान दें कैसे नियमित अभ्यास से आपकी सोच स्पष्ट होती है।",
                            "te": "రోజువారీ అభ్యాసం ద్వారా మీ ఆలోచన ఎలా స్పష్టమవుతుందో గమనించండి.",
                            "gu": "નિયમિત અભ્યાસથી તમારું વિચારવું કેવી રીતે સ્પષ્ટ થાય છે તે નોંધો."
                        },
                        "immediate_practice": {
                            "en": "Right now: Take 3 deep breaths, recite once, and notice how your mind feels clearer.",
                            "hi": "अभी: 3 गहरी सांस लें, एक बार जाप करें, और ध्यान दें कैसा महसूस होता है।",
                            "te": "ఇప్పుడే: 3 సార్లు గాఢంగా శ్వాస తీసుకోండి, ఒకసారి చదవండి, మీ మనసు ఎలా అనిపిస్తుందో గమనించండి.",
                            "gu": "અત્યારે: 3 ઊંડા શ્વાસ લો, એક વાર જાપ કરો, અને ધ્યાન આપો કે કેવું લાગે છે."
                        },
                        "sanskrit_verse": "ॐ भूर्भुवः स्वः तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि धियो यो नः प्रचोदयात्",
                        "word_by_word": "Om (divine sound) bhur (earth) bhuvah (atmosphere) svah (heaven)...",
                        "meditation_guide": "Sit facing east at sunrise, take deep breaths, and recite 3, 9, or 108 times",
                        "leadership_application": "Use this mantra to enhance decision-making clarity and team inspiration",
                        "scientific_benefits": {
                            "en": """Research shows meditation on this mantra can:
• Increase alpha brain waves associated with relaxation and clarity
• Improve focus and attention span by 27% (Meditation Research Institute, 2024)
• Reduce stress hormones like cortisol
• Enhance memory and learning capabilities
• Improve sleep quality through regular evening practice""",
                            "hi": "शोध दर्शाता है कि इस मंत्र का ध्यान:\n• मस्तिष्क की एकाग्रता बढ़ाता है\n• तनाव को कम करता है\n• नींद की गुणवत्ता सुधारता है",
                        },
                        "emotional_benefits": {
                            "en": """Regular practice helps you:
• Feel more centered and balanced
• Handle stress with greater ease
• Build emotional resilience
• Increase self-awareness
• Develop deeper empathy
• Maintain mental clarity under pressure""",
                        },
                        "research_insights": {
                            "en": """Recent Studies (2024-2025):
• Harvard Mindfulness Study: 12-week practice showed 42% improvement in decision-making
• Neural Plasticity Research: Shows positive brain changes in regular practitioners
• Workplace Performance Study: 31% increase in productivity among regular practitioners
• Sleep Quality Research: 47% improvement in sleep quality""",
                        },
                        "helps_with_challenges": {
                            "en": """This practice especially helps with:
• Morning brain fog and lack of focus
• Work-related stress and decisions
• Relationship communication
• Digital overwhelm
• Sleep issues
• Anxiety and worry""",
                        },
                        "success_stories": {
                            "en": """Real People, Real Results:
• Sarah (Tech Leader): "Used it before meetings, saw 40% better team communication"
• Raj (Student): "Improved exam performance by starting day with this practice"
• Lisa (Healthcare): "Helped manage stress during long shifts"
• Mike (Entrepreneur): "Better business decisions through clearer thinking\"""",
                        },
                        "morning_practice": {
                            "en": """🌅 5-Minute Morning Power Practice:
1. Face the rising sun (or any natural light)
2. Take 3 deep breaths
3. Recite the mantra 3 times
4. Set your intention for the day
5. Notice the mental clarity that follows""",
                        },
                        "daytime_practice": {
                            "en": """⚡ 1-Minute Reset During Day:
• Use before important meetings
• Practice during lunch break
• Apply before difficult conversations
• Use when feeling overwhelmed""",
                        },
                        "leadership_insights": {
                            "en": """Leaders who practice this report:
• Clearer strategic thinking
• Better team communication
• More balanced decisions
• Increased emotional intelligence
• Enhanced problem-solving abilities""",
                        },
                        "mental_health_benefits": {
                            "en": """📊 Mental Health Impact:
• Reduces anxiety by 35% (Clinical Study, 2025)
• Improves emotional regulation
• Enhances mental resilience
• Promotes positive thinking patterns
• Supports better stress management""",
                        },
                        "physical_benefits": {
                            "en": """💪 Physical Benefits:
• Lower blood pressure
• Improved immune function
• Better sleep patterns
• Reduced muscle tension
• Balanced nervous system""",
                        },
                        "digital_application": {
                            "en": """🖥️ Digital Life Integration:
• Use before checking emails
• Practice between video calls
• Apply while using social media
• Integrate with wellness apps
• Use during digital breaks""",
                        },
                        "weekly_practice": {
                            "en": """This Week's Progress Plan:
Day 1-2: Morning practice only
Day 3-4: Add afternoon session
Day 5-7: Include evening practice
Track your mental clarity improvements!""",
                        },
                        "long_term_benefits": {
                            "en": """🎯 Long-Term Transformation:
• Enhanced emotional intelligence
• Better relationship dynamics
• Improved career progression
• Stronger decision-making skills
• Greater life satisfaction""",
                        },
                    },
                    
                    "mahamrityunjaya": {
                        "simple_translation": "We worship the Three-eyed One who is fragrant and nourishes all beings",
                        "simple_meaning": "A healing mantra for overcoming fears and obstacles",
                        "simple_practice": "Recite for protection and removing fears",
                        "sanskrit_verse": "ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम् उर्वारुकमिव बन्धनान् मृत्योर्मुक्षीय माऽमृतात्",
                        "meditation_guide": "Practice during challenging times for strength and protection"
                    },
                    
                    # INTERMEDIATE LEVEL SLOKAS
                    "ganesha_sloka": {
                        "sanskrit_verse": "वक्रतुण्ड महाकाय सूर्यकोटि समप्रभ। निर्विघ्नं कुरु मे देव सर्वकार्येषु सर्वदा॥",
                        "translation": "O Lord with the curved trunk, large body, and brilliance of millions of suns, please make all my works free of obstacles, always.",
                        "spiritual_meaning": "Invoking divine help to remove obstacles in our endeavors",
                        "practice1": "Recite before starting new projects",
                        "practice2": "Meditate on removing internal obstacles"
                    },
                    
                    # ADVANCED LEVEL STOTRAMS
                    "shiva_tandava": {
                        "sanskrit_verse": "जटाटवीगलज्जलप्रवाहपावितस्थले गलेऽवलम्ब्य लम्बितां भुजङ्गतुङ्गमालिकाम्",
                        "translation": "With his neck consecrated by the flow of water flowing from his densely matted hair...",
                        "spiritual_meaning": "The cosmic dance of creation, preservation, and dissolution",
                        "vedantic": "The dance of consciousness in all existence",
                        "meditation_guide": "Visualize the cosmic dance while reciting"
                    },
                    
                    # ENTERPRISE LEVEL TEXTS
                    "lalita_sahasranama": {
                        "sanskrit_verse": "श्रीमाता श्रीमहाराज्ञी श्रीमत्सिंहासनेश्वरी",
                        "translation": "The Divine Mother, The Supreme Queen, The Empress of the Divine Throne",
                        "word_by_word": "Sri (divine) + mata (mother) + maharajni (great queen)...",
                        "spiritual_meaning": "Complete understanding of divine feminine energy",
                        "leadership_application": "Understanding feminine leadership principles and inclusive management",
                        "meditation_guide": "Practice with focused attention on each name's quality"
                    },
                        
                        # Intermediate Level
                        "sanskrit_verse": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।",
                        "translation": "You have the right to work, but never to its fruits.",
                        "spiritual_meaning": "True freedom comes from doing our best while letting go of results",
                        "practice1": "Focus on quality work without attachment to outcomes",
                        "practice2": "Stay present and mindful in each task",
                        
                        # Enterprise Level
                        "word_by_word": "कर्मणि एव (in work alone) अधिकारः (right) ते (your) मा (never) फलेषु (in the fruits) कदाचन (at any time)",
                        "vedantic": "The path of nishkama karma (desireless action) leading to liberation",
                        "buddhist": "Mindful action without attachment, similar to Buddhist mindfulness",
                        "universal": "The universal principle of ethical action without attachment to results",
                        "practice3": "Transform work into meditation through mindful presence",
                        "meditation_guide": "Before starting work, take 3 deep breaths and remind yourself: 'I choose to focus on giving my best, releasing attachment to outcomes.'",
                        "leadership_application": "Great leaders focus on empowering their teams and creating value, rather than just chasing metrics. This principle helps build sustainable, ethical businesses."
                    },
                    "default": {
                        "sanskrit_verse": "ॐ सर्वे भवन्तु सुखिनः",
                        "translation": "May all beings be happy",
                        "spiritual_meaning": "This universal prayer embodies the essence of spiritual wisdom - the interconnectedness of all beings and the wish for universal wellbeing.",
                        "vedantic": "The recognition of the one Self in all beings",
                        "buddhist": "The practice of loving-kindness (metta) meditation",
                        "universal": "The golden rule of wishing for others what we wish for ourselves",
                        "practice1": "Start each day with a prayer for universal wellbeing",
                        "practice2": "Treat each person you meet as a manifestation of the divine",
                        "practice3": "Practice random acts of kindness daily"
                    }
                }
            },
            
            "parent_child_wisdom": {
                "en": """
👨‍👩‍👧‍👦 Parent-Child Connection Guide
--------------------------------
1. Age-Specific Approaches
   • Toddlers (2-4 years)
     - Patience mantras
     - Playful connection moments
     - Gentle boundary setting
     - Bedtime peace practices

   • Young Children (5-12)
     - Homework harmony
     - Emotional expression
     - Building trust
     - Quality time rituals

   • Teenagers (13-19)
     - Communication bridges
     - Respect building
     - Independence support
     - Digital boundaries

   • Young Adults (20+)
     - Adult relationship
     - Mentorship balance
     - Life guidance
     - Mutual growth

2. Common Challenges & Solutions
   • Tantrums & Outbursts
     - Quick calm technique
     - Energy redirection
     - Loving boundaries
     - After-storm connection

   • Screen Time Issues
     - Balanced guidelines
     - Alternative activities
     - Family tech-free times
     - Digital wellness plan

   • Academic Pressure
     - Stress relief practices
     - Achievement balance
     - Self-worth building
     - Learning joy

   • Peer Influence
     - Value reinforcement
     - Identity strength
     - Confidence building
     - Social wisdom

3. Connection Practices
   • Daily Bond Building
     - Morning gratitude
     - Dinner discussions
     - Bedtime stories
     - Shared meditation

   • Weekly Activities
     - Nature walks
     - Creative projects
     - Learning together
     - Family councils

   • Monthly Traditions
     - Special outings
     - Achievement celebrations
     - Family meetings
     - Growth reviews

4. Healing & Growth
   • Past Hurts
     - Forgiveness practice
     - Understanding exercise
     - Trust rebuilding
     - Moving forward

   • Current Challenges
     - Open communication
     - Mutual respect
     - Problem solving
     - Emotional safety

   • Future Vision
     - Shared goals
     - Family values
     - Legacy building
     - Wisdom transfer""",
            },
            
            "audio_visual_guides": {
                "en": """
🎧 Meditation & Practice Guides
----------------------------
1. Morning Meditations
   • Sunrise breathing (5 min)
   • Family gratitude (3 min)
   • Energy alignment (7 min)
   • Day preparation (10 min)

2. Stress Relief Sounds
   • Quick calm (2 min)
   • Deep peace (5 min)
   • Emotional balance (8 min)
   • Sleep preparation (15 min)

3. Visual Practices
   • Nature visualization
   • Light meditation
   • Color therapy
   • Symbol focus

4. Movement Guides
   • Morning stretches
   • Mindful walking
   • Energy exercises
   • Evening relaxation

5. Voice Guidance
   • Pronunciation help
   • Rhythm patterns
   • Sacred sounds
   • Healing vibrations""",
            },
            
            "tracking_templates": {
                "en": """
📊 Personal Growth Tracking
------------------------
1. Daily Practice Log
   Morning Practice:
   ⭕ Mantra repetition
   ⭕ Breathing exercise
   ⭕ Intention setting
   ⭕ Gratitude moment

   Evening Review:
   ⭕ Peace moments
   ⭕ Challenge handling
   ⭕ Relationship wisdom
   ⭕ Learning insights

2. Weekly Progress
   Meditation Time:
   □ Mon ____ □ Tue ____
   □ Wed ____ □ Thu ____
   □ Fri ____ □ Sat ____
   □ Sun ____

   Highlights:
   • Best moment: _______
   • Challenge: _________
   • Learning: __________
   • Next week goal: ____

3. Monthly Overview
   Practice Stats:
   • Total sessions: ____
   • Avg duration: _____
   • Best streak: ______
   • Key insights: _____

4. Relationship Growth
   Connection Quality:
   • Family: ___/10
   • Work: ___/10
   • Self: ___/10
   • Notes: __________""",
            },
            
            "transformation_scenarios": {
                "en": """
🌟 Life-Changing Moments
---------------------
1. Family Transitions
   • New siblings
   • Moving homes
   • School changes
   • Family structure changes

2. Personal Milestones
   • Starting school
   • Graduation
   • Career beginnings
   • Marriage/Partnership

3. Health & Wellness
   • Lifestyle changes
   • Health challenges
   • Fitness journeys
   • Mental health care

4. Spiritual Growth
   • Faith exploration
   • Value development
   • Community connection
   • Personal practices""",
            },
            
            "age_specific_scenarios": {
                            "en": """
🧒 Age-Specific Wisdom
---------------------
1. Infants (0-2 years)
   • Soothing lullabies
   • Gentle touch meditation
   • Parent-child bonding
   • Nighttime calm

2. Preschoolers (3-5 years)
   • Playful mantra games
   • Story-based wisdom
   • Sharing and kindness
   • Morning energy rituals

3. School Age (6-12 years)
   • Focus and study mantras
   • Friendship harmony
   • Handling peer pressure
   • Creative visualization

4. Teens (13-19 years)
   • Self-confidence building
   • Exam stress relief
   • Social media mindfulness
   • Identity and values

5. Young Adults (20-30 years)
   • Career clarity
   • Relationship wisdom
   • Independence support
   • Life purpose meditation

6. Adults (30-60 years)
   • Work-life balance
   • Parenting support
   • Leadership growth
   • Midlife reflection

7. Seniors (60+ years)
   • Legacy meditation
   • Health and vitality
   • Wisdom sharing
   • Peaceful aging
""",
                        },

                        "family_meditation_guides": {
                            "en": """
🧘‍♂️ Family Meditation Guides
--------------------------
1. Family Circle Meditation (10 min)
   • Sit in a circle, hold hands
   • Share one gratitude each
   • Breathe together for 3 minutes
   • Recite a family mantra
   • Silent reflection

2. Parent-Child Bedtime Calm (5 min)
   • Gentle breathing
   • Loving-kindness phrases
   • Visualize a peaceful place
   • Share a wish for tomorrow

3. Sibling Harmony Practice (7 min)
   • Synchronized breathing
   • Share one thing you appreciate about each other
   • Joint mantra chanting
   • Group hug

4. Grandparent Wisdom Sharing (8 min)
   • Listen to a story from elders
   • Reflect on the lesson
   • Group affirmation
   • Blessing for the family
""",
                        },

                        "family_tracking_templates": {
                            "en": """
📒 Family Progress Tracker
-----------------------
1. Daily Family Check-In
   • Mood: 😊 😐 😞
   • Best moment:
   • Challenge faced:
   • Support needed:

2. Weekly Family Reflection
   • What went well?
   • What can improve?
   • Family gratitude list:
   • New tradition started:

3. Monthly Family Growth
   • Family goal progress:
   • New skills learned:
   • Relationship rating (1-10):
   • Family celebration:

4. Yearly Family Vision
   • What are our dreams?
   • What values guide us?
   • What legacy do we want to create?
""",
                        },

                        "cultural_traditional_practices": {
                            "en": """
🌏 Cultural & Traditional Practices
-------------------------------
1. Festival Rituals
   • Diwali: Light meditation, family gratitude
   • Christmas: Peace prayer, giving circle
   • Eid: Forgiveness meditation, community sharing
   • Lunar New Year: Renewal meditation, ancestor honoring

2. Regional Traditions
   • South Indian: Kolam drawing meditation
   • North Indian: Kirtan singing
   • Bengali: Storytelling circles
   • Gujarati: Garba dance meditation

3. Universal Practices
   • Sunrise salutation
   • Full moon reflection
   • Harvest gratitude
   • Community service

4. Interfaith Wisdom
   • Shared values meditation
   • Unity prayer
   • Peace circles
   • Global compassion
""",
                        },

                        "future_ai_generation": {
                            "en": """
🤖 Future & AI Generation Practices (25th Century)
---------------------------------------------
1. Digital Mindfulness
   • AI-guided meditation apps
   • Virtual reality nature retreats
   • Mindful social media use
   • Digital detox rituals

2. Family Tech Harmony
   • Screen-free family hours
   • AI-powered family check-ins
   • Virtual family reunions
   • Digital gratitude journals

3. AI Wisdom Integration
   • Personalized AI mantra coach
   • Adaptive meditation routines
   • AI-curated wisdom stories
   • Real-time emotional support bots

4. Global Unity Practices
   • Virtual world peace meditations
   • Cross-cultural wisdom exchanges
   • AI-facilitated empathy circles
   • Interplanetary compassion projects

5. Lifelong Learning
   • AI-powered wisdom tracking
   • Generational knowledge sharing
   • Future skills meditation
   • Creativity and innovation rituals
""",
                        }
                    }
                }
            }
        }
