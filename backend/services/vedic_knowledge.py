"""
vedic_knowledge.py - Comprehensive Vedic Astrology Knowledge Base
Derived from Nakshatra Jyotish and classical Vedic texts.
"""

NAKSHATRAS = {
    "Ashwini": {
        "ruler": "Ketu", "deity": "Ashwini Kumaras (Divine Physicians)",
        "symbol": "Horse's Head", "element": "Earth", "guna": "Rajas",
        "traits": "Swift, healing, pioneering, adventurous, impatient, courageous",
        "career": "Medicine, healing arts, sports, racing, emergency services, entrepreneurship",
        "relationships": "Passionate, quick to fall in love, values freedom, needs an independent partner",
        "health": "Head injuries, migraines, mental stress. Strong vitality but prone to accidents",
        "remedies": "Worship Ashwini Kumaras, chant 'Om Ashwini Kumarabhyam Namah', wear Cat's Eye gemstone",
        "padas": "1-Aries(Mars), 2-Taurus(Venus), 3-Gemini(Mercury), 4-Cancer(Moon)"
    },
    "Bharani": {
        "ruler": "Venus", "deity": "Yama (God of Death/Dharma)",
        "symbol": "Yoni (Female reproductive organ)", "element": "Earth", "guna": "Rajas",
        "traits": "Creative, transformative, intense, nurturing, possessive, determined",
        "career": "Arts, entertainment, judiciary, publishing, fertility specialist, psychology",
        "relationships": "Deeply passionate, possessive in love, loyal, intense emotional bonds",
        "health": "Reproductive issues, diabetes, facial problems. Strong constitution",
        "remedies": "Worship Lord Yama, chant 'Om Yamaya Namah', wear Diamond or White Sapphire",
        "padas": "1-Leo(Sun), 2-Virgo(Mercury), 3-Libra(Venus), 4-Scorpio(Mars)"
    },
    "Krittika": {
        "ruler": "Sun", "deity": "Agni (God of Fire)",
        "symbol": "Razor/Flame", "element": "Fire", "guna": "Rajas",
        "traits": "Sharp, purifying, determined, critical, honest, ambitious, fiery temper",
        "career": "Military, cooking, metalwork, spiritual teaching, surgery, leadership roles",
        "relationships": "Protective, nurturing but critical, needs respect and admiration from partner",
        "health": "Fevers, digestive issues, skin inflammations. Burns and accidents",
        "remedies": "Worship Agni Dev, chant 'Om Agnaye Namah', wear Ruby gemstone",
        "padas": "1-Sagittarius(Jupiter), 2-Capricorn(Saturn), 3-Aquarius(Saturn), 4-Pisces(Jupiter)"
    },
    "Rohini": {
        "ruler": "Moon", "deity": "Brahma (Creator God)",
        "symbol": "Ox Cart/Chariot", "element": "Earth", "guna": "Rajas",
        "traits": "Beautiful, artistic, materialistic, sensual, magnetic, stubborn, creative",
        "career": "Fashion, beauty, agriculture, banking, hospitality, luxury goods, arts",
        "relationships": "Romantic, devoted, attractive, may attract jealousy, values comfort and beauty",
        "health": "Throat problems, cold/cough, blood sugar issues. Generally good health",
        "remedies": "Worship Lord Brahma, chant 'Om Brahmane Namah', wear Pearl or Moonstone",
        "padas": "1-Aries(Mars), 2-Taurus(Venus), 3-Gemini(Mercury), 4-Cancer(Moon)"
    },
    "Mrigashira": {
        "ruler": "Mars", "deity": "Soma (Moon God/Nectar)",
        "symbol": "Deer's Head", "element": "Earth", "guna": "Tamas",
        "traits": "Curious, searching, gentle, restless, intellectual, fickle-minded",
        "career": "Research, writing, travel industry, textiles, music, exploration, teaching",
        "relationships": "Seeks perfect partner, romantic but restless, needs mental stimulation",
        "health": "Nervous disorders, shoulder/arm issues, allergies. Sensitive constitution",
        "remedies": "Worship Soma/Chandra, chant 'Om Somaya Namah', wear Red Coral",
        "padas": "1-Leo(Sun), 2-Virgo(Mercury), 3-Libra(Venus), 4-Scorpio(Mars)"
    },
    "Ardra": {
        "ruler": "Rahu", "deity": "Rudra (Storm God/Shiva)",
        "symbol": "Teardrop/Diamond", "element": "Water", "guna": "Tamas",
        "traits": "Intellectual, destructive-creative, emotional storms, analytical, transformative",
        "career": "Technology, software, research, pharmaceuticals, electrical engineering, politics",
        "relationships": "Intense emotional nature, can be turbulent, deep connections after struggles",
        "health": "Heart problems, nervous system disorders, asthma. Mental health sensitivity",
        "remedies": "Worship Lord Shiva/Rudra, chant 'Om Namah Shivaya', wear Hessonite (Gomed)",
        "padas": "1-Sagittarius(Jupiter), 2-Capricorn(Saturn), 3-Aquarius(Saturn), 4-Pisces(Jupiter)"
    },
    "Punarvasu": {
        "ruler": "Jupiter", "deity": "Aditi (Mother of Gods)",
        "symbol": "Bow and Quiver", "element": "Water", "guna": "Sattva",
        "traits": "Optimistic, philosophical, generous, forgiving, spiritual, restoring",
        "career": "Teaching, counseling, publishing, import-export, hospitality, spiritual work",
        "relationships": "Nurturing, forgiving, attracts good partners, values spiritual connection",
        "health": "Liver issues, respiratory, ear problems. Good recovery from illness",
        "remedies": "Worship Goddess Aditi, chant 'Om Aditaye Namah', wear Yellow Sapphire",
        "padas": "1-Aries(Mars), 2-Taurus(Venus), 3-Gemini(Mercury), 4-Cancer(Moon)"
    },
    "Pushya": {
        "ruler": "Saturn", "deity": "Brihaspati (Jupiter/Guru of Gods)",
        "symbol": "Cow's Udder/Lotus", "element": "Water", "guna": "Sattva",
        "traits": "Nourishing, wise, caring, traditional, conservative, selfless, devoted",
        "career": "Government, dairy, food industry, teaching, real estate, charity, counseling",
        "relationships": "Devoted family person, caring spouse, may sacrifice too much for others",
        "health": "Chest/lung issues, skin diseases, water retention. Moderate constitution",
        "remedies": "Worship Brihaspati/Jupiter, chant 'Om Brihaspataye Namah', wear Blue Sapphire",
        "padas": "1-Leo(Sun), 2-Virgo(Mercury), 3-Libra(Venus), 4-Scorpio(Mars)"
    },
    "Ashlesha": {
        "ruler": "Mercury", "deity": "Naga (Serpent Deities)",
        "symbol": "Coiled Serpent", "element": "Water", "guna": "Sattva",
        "traits": "Mystical, penetrating insight, secretive, manipulative, hypnotic, kundalini energy",
        "career": "Occult sciences, psychology, pharmacy, detective work, politics, astrology",
        "relationships": "Possessive, magnetic attraction, trust issues, deep karmic bonds",
        "health": "Nervous system, poisoning risks, joints, cold constitution. Anxiety prone",
        "remedies": "Worship Naga Devatas, chant 'Om Namo Nagarajaya Namah', wear Emerald",
        "padas": "1-Sagittarius(Jupiter), 2-Capricorn(Saturn), 3-Aquarius(Saturn), 4-Pisces(Jupiter)"
    },
    "Magha": {
        "ruler": "Ketu", "deity": "Pitris (Ancestors)",
        "symbol": "Royal Throne", "element": "Fire", "guna": "Tamas",
        "traits": "Regal, authoritative, traditional, proud, generous, ancestor-connected",
        "career": "Government, administration, management, archaeology, history, politics, leadership",
        "relationships": "Expects respect and devotion, generous partner, values family lineage",
        "health": "Heart issues, eye problems, genetic conditions. Strong but pride affects health",
        "remedies": "Perform Pitru Tarpan, chant 'Om Pitridevabhyo Namah', wear Cat's Eye",
        "padas": "1-Aries(Mars), 2-Taurus(Venus), 3-Gemini(Mercury), 4-Cancer(Moon)"
    },
    "Purva Phalguni": {
        "ruler": "Venus", "deity": "Bhaga (God of Fortune/Pleasure)",
        "symbol": "Front legs of a bed/Hammock", "element": "Fire", "guna": "Tamas",
        "traits": "Creative, luxury-loving, romantic, charismatic, generous, pleasure-seeking",
        "career": "Entertainment, arts, hospitality, wedding planning, cosmetics, music",
        "relationships": "Romantic, sensual, enjoys courtship, needs beauty and comfort in relationships",
        "health": "Heart, lips, reproductive organs. Generally good health, overindulgence risks",
        "remedies": "Worship Bhaga Aditya, chant 'Om Bhagaya Namah', wear Diamond",
        "padas": "1-Leo(Sun), 2-Virgo(Mercury), 3-Libra(Venus), 4-Scorpio(Mars)"
    },
    "Uttara Phalguni": {
        "ruler": "Sun", "deity": "Aryaman (God of Patronage/Contracts)",
        "symbol": "Back legs of a bed", "element": "Fire", "guna": "Tamas",
        "traits": "Helpful, prosperous, reliable, organized, philanthropic, leadership",
        "career": "Social work, UN/NGO, management, administration, law, counseling",
        "relationships": "Reliable, committed, excellent marriage partner, values social standing",
        "health": "Spine issues, stomach, skin. Generally robust health",
        "remedies": "Worship Aryaman, chant 'Om Aryamne Namah', wear Ruby",
        "padas": "1-Sagittarius(Jupiter), 2-Capricorn(Saturn), 3-Aquarius(Saturn), 4-Pisces(Jupiter)"
    },
    "Hasta": {
        "ruler": "Moon", "deity": "Savitar (Sun God of Inspiration)",
        "symbol": "Open Hand/Palm", "element": "Fire", "guna": "Rajas",
        "traits": "Skillful, crafty, humorous, resourceful, healer, light-fingered",
        "career": "Handicrafts, surgery, painting, massage therapy, astrology, stage performance",
        "relationships": "Charming, witty, adaptable partner, can be cunning, values cleverness",
        "health": "Hands, arms, allergies, cold/flu. Nervous energy affects health",
        "remedies": "Worship Savitar/Sun, chant Gayatri Mantra, wear Pearl",
        "padas": "1-Aries(Mars), 2-Taurus(Venus), 3-Gemini(Mercury), 4-Cancer(Moon)"
    },
    "Chitra": {
        "ruler": "Mars", "deity": "Vishvakarma (Divine Architect)",
        "symbol": "Bright Jewel/Pearl", "element": "Fire", "guna": "Rajas",
        "traits": "Attractive, creative, artistic, perfectionist, well-dressed, charismatic",
        "career": "Architecture, interior design, fashion, jewelry, graphic design, photography",
        "relationships": "Attractive, seeks beauty in partner, may be superficial, passionate",
        "health": "Kidney, bladder, forehead, brain. Generally attractive appearance",
        "remedies": "Worship Vishvakarma, chant 'Om Vishvakarmane Namah', wear Red Coral",
        "padas": "1-Leo(Sun), 2-Virgo(Mercury), 3-Libra(Venus), 4-Scorpio(Mars)"
    },
    "Swati": {
        "ruler": "Rahu", "deity": "Vayu (God of Wind)",
        "symbol": "Coral/Young Plant swaying in wind", "element": "Air", "guna": "Rajas",
        "traits": "Independent, flexible, diplomatic, business-minded, freedom-loving, adaptable",
        "career": "Business, trade, law, diplomacy, travel, import-export, stock market",
        "relationships": "Values independence, diplomatic in love, may delay marriage for career",
        "health": "Skin, kidneys, urinary tract, hernia. Wind-related ailments",
        "remedies": "Worship Vayu Dev and Goddess Saraswati, chant 'Om Vayave Namah', wear Hessonite",
        "padas": "1-Sagittarius(Jupiter), 2-Capricorn(Saturn), 3-Aquarius(Saturn), 4-Pisces(Jupiter)"
    },
    "Vishakha": {
        "ruler": "Jupiter", "deity": "Indra-Agni (King of Gods & Fire God)",
        "symbol": "Triumphal Arch/Potter's Wheel", "element": "Air", "guna": "Sattva",
        "traits": "Determined, goal-oriented, ambitious, zealous, jealous, single-minded",
        "career": "Politics, military, religion, research, agriculture, broadcasting",
        "relationships": "Passionate, possessive, intense bonds, may have complicated love life",
        "health": "Kidneys, bladder, hormonal issues. Good stamina",
        "remedies": "Worship Indra and Agni, chant 'Om Indragnibhyam Namah', wear Yellow Sapphire",
        "padas": "1-Aries(Mars), 2-Taurus(Venus), 3-Gemini(Mercury), 4-Cancer(Moon)"
    },
    "Anuradha": {
        "ruler": "Saturn", "deity": "Mitra (God of Friendship)",
        "symbol": "Lotus/Triumphal Archway", "element": "Air", "guna": "Sattva",
        "traits": "Devoted, friendly, spiritual, organized, disciplined, success in foreign lands",
        "career": "Organization, management, occult, mining, diplomacy, international business",
        "relationships": "Devoted, loyal, may face difficulties early, eventual deep partnership",
        "health": "Hips, stomach, bladder, womb. Dental issues possible",
        "remedies": "Worship Lord Vishnu/Mitra, chant 'Om Mitraya Namah', wear Blue Sapphire",
        "padas": "1-Leo(Sun), 2-Virgo(Mercury), 3-Libra(Venus), 4-Scorpio(Mars)"
    },
    "Jyeshtha": {
        "ruler": "Mercury", "deity": "Indra (King of Gods)",
        "symbol": "Circular Amulet/Earring", "element": "Air", "guna": "Sattva",
        "traits": "Protective, senior, authoritative, jealous, secretive, courageous",
        "career": "Military, police, executive roles, occult, administration, detective",
        "relationships": "Protective but controlling, needs to feel superior, intense family bonds",
        "health": "Colon, reproductive organs, neck problems, chronic ailments",
        "remedies": "Worship Lord Indra, chant 'Om Indraya Namah', wear Emerald",
        "padas": "1-Sagittarius(Jupiter), 2-Capricorn(Saturn), 3-Aquarius(Saturn), 4-Pisces(Jupiter)"
    },
    "Mula": {
        "ruler": "Ketu", "deity": "Nirrti (Goddess of Dissolution)",
        "symbol": "Bundle of Roots/Tied bunch", "element": "Air", "guna": "Tamas",
        "traits": "Investigative, destructive-constructive, philosophical, uprooting, intense",
        "career": "Research, medicine (root cause), herbalism, philosophy, astrology, archaeology",
        "relationships": "Karmic relationships, may face early difficulties, spiritual partnerships",
        "health": "Hips, thighs, sciatic nerve, mental instability risk",
        "remedies": "Worship Goddess Kali/Nirrti, chant 'Om Nirrityai Namah', wear Cat's Eye",
        "padas": "1-Aries(Mars), 2-Taurus(Venus), 3-Gemini(Mercury), 4-Cancer(Moon)"
    },
    "Purva Ashadha": {
        "ruler": "Venus", "deity": "Apas (Water Deity)",
        "symbol": "Elephant Tusk/Fan", "element": "Water", "guna": "Tamas",
        "traits": "Invincible, purifying, philosophical, proud, ambitious, persuasive",
        "career": "Shipping, navy, water-related, philosophy, law, media, motivational speaking",
        "relationships": "Attractive, proud, may dominate, needs intellectual equal",
        "health": "Thighs, hips, blood circulation. Kidney/bladder issues",
        "remedies": "Worship Apas/Water deities, chant 'Om Apo Devtabhyo Namah', wear Diamond",
        "padas": "1-Leo(Sun), 2-Virgo(Mercury), 3-Libra(Venus), 4-Scorpio(Mars)"
    },
    "Uttara Ashadha": {
        "ruler": "Sun", "deity": "Vishve Devas (Universal Gods)",
        "symbol": "Elephant Tusk/Small bed", "element": "Water", "guna": "Tamas",
        "traits": "Righteous, victorious, leadership, sincere, law-abiding, pioneering",
        "career": "Government, law, defense, social reform, pioneering ventures, leadership",
        "relationships": "Sincere, committed, may marry late, values integrity in partner",
        "health": "Knees, thighs, skin, bones. Generally strong",
        "remedies": "Worship Vishve Devas/Ganesha, chant 'Om Ganapataye Namah', wear Ruby",
        "padas": "1-Sagittarius(Jupiter), 2-Capricorn(Saturn), 3-Aquarius(Saturn), 4-Pisces(Jupiter)"
    },
    "Shravana": {
        "ruler": "Moon", "deity": "Vishnu (The Preserver)",
        "symbol": "Three Footprints/Ear", "element": "Water", "guna": "Rajas",
        "traits": "Learned, patient, listener, connected, organizational, knowledgeable",
        "career": "Teaching, counseling, media, music, languages, telecommunications",
        "relationships": "Empathetic listener, devoted spouse, values tradition and family",
        "health": "Ears, knees, skin, rheumatism. Walking/mobility issues in old age",
        "remedies": "Worship Lord Vishnu, chant 'Om Namo Narayanaya', wear Pearl",
        "padas": "1-Aries(Mars), 2-Taurus(Venus), 3-Gemini(Mercury), 4-Cancer(Moon)"
    },
    "Dhanishta": {
        "ruler": "Mars", "deity": "Ashta Vasus (Eight Elemental Gods)",
        "symbol": "Drum/Flute", "element": "Ether", "guna": "Rajas",
        "traits": "Wealthy, musical, adventurous, resourceful, ambitious, sometimes hollow",
        "career": "Music, real estate, sports, scientific research, property management",
        "relationships": "May face marital delays, needs compatible temperament, generous partner",
        "health": "Blood disorders, ankles, knees. Anemia risk",
        "remedies": "Worship Ashta Vasus, chant 'Om Vasubhyo Namah', wear Red Coral",
        "padas": "1-Leo(Sun), 2-Virgo(Mercury), 3-Libra(Venus), 4-Scorpio(Mars)"
    },
    "Shatabhisha": {
        "ruler": "Rahu", "deity": "Varuna (God of Cosmic Waters)",
        "symbol": "Empty Circle/100 Stars", "element": "Ether", "guna": "Rajas",
        "traits": "Healing, secretive, independent, philosophical, mysterious, reclusive",
        "career": "Healing, astrology, space science, technology, pharmaceuticals, alternative medicine",
        "relationships": "Independent, secretive, may struggle with intimacy, values personal space",
        "health": "Heart, ankles, jaw, calves. Chronic diseases possible",
        "remedies": "Worship Varuna, chant 'Om Varunaya Namah', wear Hessonite (Gomed)",
        "padas": "1-Sagittarius(Jupiter), 2-Capricorn(Saturn), 3-Aquarius(Saturn), 4-Pisces(Jupiter)"
    },
    "Purva Bhadrapada": {
        "ruler": "Jupiter", "deity": "Aja Ekapada (One-footed Goat/Shiva form)",
        "symbol": "Front of Funeral Cot/Two-faced man", "element": "Ether", "guna": "Sattva",
        "traits": "Intense, transformative, passionate, mystical, dual-natured, fiery idealism",
        "career": "Astrology, occult, research, humanitarian work, philosophy, writing",
        "relationships": "Intense bonds, may be unpredictable, spiritual connection important",
        "health": "Ankles, feet, ribs, liver. Stress-related ailments",
        "remedies": "Worship Aja Ekapada/Shiva, chant 'Om Aja Ekapadaya Namah', wear Yellow Sapphire",
        "padas": "1-Aries(Mars), 2-Taurus(Venus), 3-Gemini(Mercury), 4-Cancer(Moon)"
    },
    "Uttara Bhadrapada": {
        "ruler": "Saturn", "deity": "Ahir Budhnya (Serpent of the Deep)",
        "symbol": "Back of Funeral Cot/Twin", "element": "Ether", "guna": "Sattva",
        "traits": "Wise, deep, compassionate, sacrificing, philosophical, controlled",
        "career": "Charity, non-profit, yoga, meditation teaching, counseling, research",
        "relationships": "Deeply caring, may sacrifice too much, excellent long-term partner",
        "health": "Feet, ankles, sleep disorders. Cold constitution",
        "remedies": "Worship Ahir Budhnya/Shiva, chant 'Om Ahir Budhnyaya Namah', wear Blue Sapphire",
        "padas": "1-Leo(Sun), 2-Virgo(Mercury), 3-Libra(Venus), 4-Scorpio(Mars)"
    },
    "Revati": {
        "ruler": "Mercury", "deity": "Pushan (Nourisher/Protector of Travelers)",
        "symbol": "Fish/Drum", "element": "Ether", "guna": "Sattva",
        "traits": "Nourishing, creative, dreamy, generous, prosperous, imaginative, compassionate",
        "career": "Travel, creative arts, film, spirituality, foster care, long-distance business",
        "relationships": "Romantic dreamer, compassionate lover, may idealize partner",
        "health": "Feet, ankles, lymphatic system. Allergies possible",
        "remedies": "Worship Pushan, chant 'Om Pushne Namah', wear Emerald",
        "padas": "1-Sagittarius(Jupiter), 2-Capricorn(Saturn), 3-Aquarius(Saturn), 4-Pisces(Jupiter)"
    }
}

RASHIS = {
    "Aries": {"ruler": "Mars", "element": "Fire", "quality": "Cardinal",
              "traits": "Courageous, energetic, pioneering, impulsive, competitive, leadership",
              "compatible": ["Leo", "Sagittarius", "Gemini", "Aquarius"]},
    "Taurus": {"ruler": "Venus", "element": "Earth", "quality": "Fixed",
               "traits": "Stable, sensual, stubborn, loyal, materialistic, artistic",
               "compatible": ["Virgo", "Capricorn", "Cancer", "Pisces"]},
    "Gemini": {"ruler": "Mercury", "element": "Air", "quality": "Mutable",
               "traits": "Curious, communicative, versatile, restless, intellectual, dual-natured",
               "compatible": ["Libra", "Aquarius", "Aries", "Leo"]},
    "Cancer": {"ruler": "Moon", "element": "Water", "quality": "Cardinal",
               "traits": "Nurturing, emotional, protective, intuitive, moody, home-loving",
               "compatible": ["Scorpio", "Pisces", "Taurus", "Virgo"]},
    "Leo": {"ruler": "Sun", "element": "Fire", "quality": "Fixed",
            "traits": "Regal, generous, dramatic, proud, creative, warm-hearted",
            "compatible": ["Aries", "Sagittarius", "Gemini", "Libra"]},
    "Virgo": {"ruler": "Mercury", "element": "Earth", "quality": "Mutable",
              "traits": "Analytical, perfectionist, service-oriented, health-conscious, practical",
              "compatible": ["Taurus", "Capricorn", "Cancer", "Scorpio"]},
    "Libra": {"ruler": "Venus", "element": "Air", "quality": "Cardinal",
              "traits": "Balanced, diplomatic, aesthetic, romantic, indecisive, harmonious",
              "compatible": ["Gemini", "Aquarius", "Leo", "Sagittarius"]},
    "Scorpio": {"ruler": "Mars", "element": "Water", "quality": "Fixed",
                "traits": "Intense, transformative, secretive, passionate, vengeful, magnetic",
                "compatible": ["Cancer", "Pisces", "Virgo", "Capricorn"]},
    "Sagittarius": {"ruler": "Jupiter", "element": "Fire", "quality": "Mutable",
                    "traits": "Philosophical, adventurous, optimistic, blunt, freedom-loving",
                    "compatible": ["Aries", "Leo", "Libra", "Aquarius"]},
    "Capricorn": {"ruler": "Saturn", "element": "Earth", "quality": "Cardinal",
                  "traits": "Ambitious, disciplined, practical, cautious, responsible, patient",
                  "compatible": ["Taurus", "Virgo", "Scorpio", "Pisces"]},
    "Aquarius": {"ruler": "Saturn", "element": "Air", "quality": "Fixed",
                 "traits": "Humanitarian, eccentric, innovative, detached, visionary, rebellious",
                 "compatible": ["Gemini", "Libra", "Aries", "Sagittarius"]},
    "Pisces": {"ruler": "Jupiter", "element": "Water", "quality": "Mutable",
               "traits": "Spiritual, compassionate, dreamy, intuitive, escapist, artistic",
               "compatible": ["Cancer", "Scorpio", "Taurus", "Capricorn"]}
}

DASHA_INTERPRETATIONS = {
    "Sun": {"duration": "6 years", "theme": "Authority, self-confidence, government connections, father, leadership. May bring fame or ego challenges. Focus on soul purpose and dharma."},
    "Moon": {"duration": "10 years", "theme": "Emotions, mother, public image, travel, mental peace. Heightened sensitivity and intuition. Important for relationships and inner growth."},
    "Mars": {"duration": "7 years", "theme": "Energy, courage, property, siblings, ambition. May bring conflicts or victories. Good for real estate and physical achievements."},
    "Rahu": {"duration": "18 years", "theme": "Worldly desires, foreign connections, unconventional paths, obsessions. Most transformative period. Can bring sudden rise or unexpected challenges."},
    "Jupiter": {"duration": "16 years", "theme": "Wisdom, expansion, children, spirituality, luck. Generally auspicious period. Growth in knowledge, wealth, and spiritual understanding."},
    "Saturn": {"duration": "19 years", "theme": "Discipline, karma, hard work, delays, maturity. Longest dasha teaches patience and responsibility. Rewards come through perseverance."},
    "Mercury": {"duration": "17 years", "theme": "Intelligence, communication, business, education, adaptability. Excellent for learning, writing, and commercial pursuits."},
    "Ketu": {"duration": "7 years", "theme": "Spirituality, detachment, moksha, past-life karma, isolation. Period of inner transformation and letting go of material attachments."},
    "Venus": {"duration": "20 years", "theme": "Love, luxury, arts, marriage, comfort, vehicles. Longest dasha brings romantic fulfillment, creative expression, and material pleasures."}
}

TRANSIT_EFFECTS = {
    "Saturn in 8th house": "Period of deep transformation, hidden obstacles, health vigilance needed. Saturn here teaches through intense life experiences. Focus on spiritual growth and insurance matters.",
    "Jupiter in 10th house": "Excellent for career growth, social recognition, professional expansion. Jupiter blesses the house of profession with opportunities, promotions, and public favor.",
    "Rahu in 5th house": "Unconventional creative expression, obsession with romance or children, speculative gains possible. Past-life karmic connections surface through love affairs.",
    "Ketu in 11th house": "Detachment from social circles, spiritual gains through friendships, unexpected income fluctuations. May lose interest in networking but gain spiritual allies.",
    "Mars transit over Natal Moon": "Emotional intensity, courage under pressure, possible conflicts, increased energy. Short but impactful transit bringing action to emotional matters.",
    "Saturn return": "Major life review every 29.5 years. First return (age 28-30): maturity. Second return (age 57-60): wisdom. Restructuring of life foundations.",
    "Jupiter transit": "Expansion and blessings in the house Jupiter transits. Lasts about 1 year per sign. Brings opportunities, growth, and protection.",
    "Rahu-Ketu transit": "Karmic axis shifts every 18 months. Brings fated events, new desires (Rahu) and spiritual release (Ketu) in the transited houses."
}

HOUSE_MEANINGS = {
    "1st": "Self, personality, physical body, appearance, new beginnings",
    "2nd": "Wealth, family, speech, food habits, values, accumulated resources",
    "3rd": "Siblings, courage, communication, short travels, skills, efforts",
    "4th": "Mother, home, comfort, vehicles, education, emotional foundation",
    "5th": "Children, creativity, romance, intellect, past-life merit, speculation",
    "6th": "Enemies, diseases, debts, service, daily routines, competition",
    "7th": "Marriage, partnerships, business, public dealings, open enemies",
    "8th": "Longevity, transformation, occult, inheritance, sudden events, secrets",
    "9th": "Luck, dharma, father, long journeys, higher education, philosophy",
    "10th": "Career, reputation, authority, public image, life purpose, achievements",
    "11th": "Gains, friendships, social networks, aspirations, elder siblings",
    "12th": "Loss, moksha, foreign lands, expenses, isolation, spiritual liberation"
}

# ═══════════════════════════════════════════
#  TIME-BASED VEDIC KNOWLEDGE
# ═══════════════════════════════════════════

HORA_LORDS = {
    "Sun": {
        "quality": "Auspicious for authority, government work, leadership tasks",
        "energy": "Royal, commanding, vital energy. Excellent for starting important ventures.",
        "health": "Strong vitality period. Good for health-related decisions.",
        "advice": "Ideal time for meeting authority figures, signing contracts, and initiating bold actions."
    },
    "Moon": {
        "quality": "Auspicious for travel, emotions, creativity, public dealings",
        "energy": "Receptive, nurturing, intuitive energy. Good for emotional matters.",
        "health": "Fluid energy period. Pay attention to hydration and emotional well-being.",
        "advice": "Best for starting journeys, creative work, dealing with the public, and nurturing relationships."
    },
    "Mars": {
        "quality": "Good for courage, property, surgery, competitive endeavors",
        "energy": "Aggressive, fiery, action-oriented energy. Period of high motivation.",
        "health": "High energy but accident-prone. Be cautious with sharp objects and fire.",
        "advice": "Ideal for physical activities, property deals, and matters requiring courage. Avoid arguments."
    },
    "Mercury": {
        "quality": "Excellent for intellect, communication, business, education",
        "energy": "Quick, analytical, communicative energy. Perfect for mental tasks.",
        "health": "Nervous energy period. Good for medical consultations and learning.",
        "advice": "Best for writing, studying, commerce, accounting, and signing documents."
    },
    "Jupiter": {
        "quality": "Most auspicious for spiritual work, teaching, ceremonies, blessings",
        "energy": "Expansive, wise, benevolent energy. The most favorable hora overall.",
        "health": "Healing and protective energy. Excellent for starting treatments.",
        "advice": "Ideal for religious ceremonies, teaching, marriage, and important life decisions."
    },
    "Venus": {
        "quality": "Excellent for love, arts, luxury purchases, beauty treatments",
        "energy": "Harmonious, artistic, romantic energy. Period of pleasure and creativity.",
        "health": "Relaxing energy. Good for beauty treatments and rest.",
        "advice": "Best for romantic meetings, purchasing jewelry/clothes, artistic pursuits, and celebrations."
    },
    "Saturn": {
        "quality": "Good for discipline, long-term planning, ancestral work, meditation",
        "energy": "Structured, karmic, introspective energy. Period of serious reflection.",
        "health": "Low energy period. Rest and conserve energy. Avoid starting new health regimens.",
        "advice": "Ideal for meditation, long-term planning, charity, and dealing with legal matters."
    }
}

# Planetary hour sequence (Chaldean order)
HORA_SEQUENCE = ["Sun", "Venus", "Mercury", "Moon", "Saturn", "Jupiter", "Mars"]

# Day rulers for hora starting point
DAY_RULERS = {
    0: "Moon",      # Monday
    1: "Mars",      # Tuesday
    2: "Mercury",   # Wednesday
    3: "Jupiter",   # Thursday
    4: "Venus",     # Friday
    5: "Saturn",    # Saturday
    6: "Sun"        # Sunday
}

MUHURTA_DATA = {
    "Rudra": {"quality": "Inauspicious", "deity": "Rudra (Shiva)", "description": "Period of destruction and transformation. Avoid new beginnings. Good for meditation on impermanence."},
    "Ahi": {"quality": "Inauspicious", "deity": "Serpent", "description": "Serpent energy period. Avoid travel and new ventures. Good for introspection and healing past wounds."},
    "Mitra": {"quality": "Auspicious", "deity": "Mitra (Friend)", "description": "Period of friendship and alliance. Excellent for making new friends, partnerships, and social gatherings."},
    "Pitri": {"quality": "Neutral", "deity": "Ancestors", "description": "Ancestral energy period. Good for honoring ancestors, performing rituals, and connecting with family roots."},
    "Vasu": {"quality": "Auspicious", "deity": "Vasus (Elemental Gods)", "description": "Period of wealth and prosperity. Excellent for financial decisions, business deals, and material pursuits."},
    "Varah": {"quality": "Auspicious", "deity": "Vishnu (Varaha)", "description": "Period of protection and upliftment. Great for beginning new projects and seeking divine blessings."},
    "Vishvedeva": {"quality": "Auspicious", "deity": "Universal Gods", "description": "Period of universal harmony. Excellent for all auspicious activities, ceremonies, and celebrations."},
    "Vidhi": {"quality": "Auspicious", "deity": "Brahma (Creator)", "description": "Period of creation and learning. Ideal for education, creative arts, and starting new creative ventures."},
    "Satamukhi": {"quality": "Auspicious", "deity": "Multi-faced One", "description": "Period of versatility and adaptability. Good for multitasking and handling complex situations."},
    "Puruhuta": {"quality": "Auspicious", "deity": "Indra", "description": "Period of leadership and victory. Excellent for competitive endeavors and asserting authority."},
    "Vahini": {"quality": "Inauspicious", "deity": "Fire", "description": "Intense fire energy. Avoid hasty decisions. Channel this energy into focused, passionate work."},
    "Naktanakara": {"quality": "Inauspicious", "deity": "Moon/Night", "description": "Lunar energy period. Good for rest, reflection, and dream work. Avoid strenuous activities."},
    "Varuna": {"quality": "Auspicious", "deity": "Varuna (Water God)", "description": "Period of cosmic order and justice. Excellent for legal matters, oaths, and seeking truth."},
    "Aryaman": {"quality": "Auspicious", "deity": "Aryaman (Nobility)", "description": "Period of patronage and contracts. Ideal for marriage proposals, agreements, and social contracts."},
    "Bhaga": {"quality": "Auspicious", "deity": "Bhaga (Fortune)", "description": "Period of good fortune and prosperity. Excellent for lottery, investments, and taking calculated risks."},
    "Girisha": {"quality": "Inauspicious", "deity": "Shiva (Mountain Lord)", "description": "Period of solitude and asceticism. Best for meditation, spiritual practices, and inner work."},
    "Ajapada": {"quality": "Inauspicious", "deity": "Aja Ekapada", "description": "Period of instability. Avoid travel and major decisions. Use for spiritual contemplation."},
    "Ahirbudhnya": {"quality": "Auspicious", "deity": "Serpent of the Deep", "description": "Period of deep wisdom and kundalini energy. Good for yoga, tantra, and esoteric studies."},
    "Pushan": {"quality": "Auspicious", "deity": "Pushan (Nourisher)", "description": "Period of nourishment and journey. Excellent for travel, animal care, and providing guidance."},
    "Ashwini": {"quality": "Auspicious", "deity": "Ashwini Kumaras", "description": "Period of healing and swift action. Ideal for medical treatments, quick tasks, and emergency responses."},
    "Yama": {"quality": "Inauspicious", "deity": "Yama (Death/Dharma)", "description": "Period of karmic reckoning. Avoid risky activities. Good for settling debts and ethical reflection."},
    "Agni": {"quality": "Auspicious", "deity": "Agni (Fire God)", "description": "Period of sacred fire and purification. Excellent for homas, cooking, and transformative work."},
    "Vidhata": {"quality": "Auspicious", "deity": "Creator/Destiny", "description": "Period of destiny and divine plan. Good for meditation on life purpose and accepting divine will."},
    "Kanda": {"quality": "Neutral", "deity": "Root/Stem", "description": "Period of foundation building. Suitable for planting seeds—both literal and metaphorical."},
    "Aditi": {"quality": "Auspicious", "deity": "Aditi (Mother of Gods)", "description": "Period of boundless nurturing. Excellent for motherly duties, hospitality, and unconditional love."},
    "Jiva": {"quality": "Auspicious", "deity": "Jupiter/Life Force", "description": "Period of vitality and teaching. Ideal for education, spiritual guidance, and life-affirming activities."},
    "Vishnu": {"quality": "Auspicious", "deity": "Vishnu (Preserver)", "description": "Period of preservation and protection. Excellent for all auspicious beginnings and maintenance work."},
    "Dyumadgadyuti": {"quality": "Auspicious", "deity": "Radiant Light", "description": "Period of divine radiance and illumination. Perfect for gaining clarity and making enlightened decisions."},
    "Brahma": {"quality": "Auspicious", "deity": "Brahma (Supreme Creator)", "description": "Period of supreme creation. Most auspicious for beginning monumental ventures and creative masterworks."},
    "Samudram": {"quality": "Neutral", "deity": "Ocean", "description": "Period of vastness and depth. Good for deep thinking, research, and exploring the unknown."}
}

# Ordered list of 30 muhurtas in a day (sunrise to sunrise)
MUHURTA_ORDER = [
    "Rudra", "Ahi", "Mitra", "Pitri", "Vasu", "Varah", "Vishvedeva", "Vidhi",
    "Satamukhi", "Puruhuta", "Vahini", "Naktanakara", "Varuna", "Aryaman", "Bhaga",
    "Girisha", "Ajapada", "Ahirbudhnya", "Pushan", "Ashwini", "Yama", "Agni",
    "Vidhata", "Kanda", "Aditi", "Jiva", "Vishnu", "Dyumadgadyuti", "Brahma", "Samudram"
]

ASCENDANT_TRAITS = {
    "Aries": {"quality": "Dynamic, assertive, pioneering personality", "appearance": "Athletic build, sharp features, energetic demeanor", "life_theme": "Self-discovery and initiative. Born to lead and take bold action."},
    "Taurus": {"quality": "Steady, sensual, reliable personality", "appearance": "Sturdy build, pleasant features, calm presence", "life_theme": "Material security and comfort. Born to build lasting value and beauty."},
    "Gemini": {"quality": "Curious, communicative, versatile personality", "appearance": "Youthful look, expressive eyes, animated gestures", "life_theme": "Communication and learning. Born to connect ideas and people."},
    "Cancer": {"quality": "Nurturing, intuitive, protective personality", "appearance": "Round face, caring eyes, gentle manner", "life_theme": "Emotional security and family. Born to nurture and protect loved ones."},
    "Leo": {"quality": "Regal, confident, dramatic personality", "appearance": "Commanding presence, thick hair, warm smile", "life_theme": "Creative self-expression and leadership. Born to shine and inspire."},
    "Virgo": {"quality": "Analytical, modest, service-oriented personality", "appearance": "Refined features, neat appearance, observant eyes", "life_theme": "Service and perfection. Born to heal, analyze, and improve."},
    "Libra": {"quality": "Charming, diplomatic, aesthetic personality", "appearance": "Symmetrical features, graceful movement, pleasant voice", "life_theme": "Balance and partnership. Born to create harmony and beauty."},
    "Scorpio": {"quality": "Intense, magnetic, transformative personality", "appearance": "Penetrating eyes, magnetic aura, powerful presence", "life_theme": "Transformation and depth. Born to probe mysteries and regenerate."},
    "Sagittarius": {"quality": "Optimistic, philosophical, adventurous personality", "appearance": "Tall stature, open face, jovial expression", "life_theme": "Wisdom and expansion. Born to explore truth and share knowledge."},
    "Capricorn": {"quality": "Ambitious, disciplined, practical personality", "appearance": "Bony structure, serious expression, mature look", "life_theme": "Achievement and responsibility. Born to build structures that endure."},
    "Aquarius": {"quality": "Independent, humanitarian, eccentric personality", "appearance": "Unique features, distant gaze, unconventional style", "life_theme": "Innovation and collective welfare. Born to revolutionize and serve humanity."},
    "Pisces": {"quality": "Compassionate, dreamy, spiritual personality", "appearance": "Soft features, dreamy eyes, ethereal quality", "life_theme": "Spiritual transcendence and compassion. Born to dissolve boundaries and heal."}
}

DAY_NIGHT_BIRTH = {
    "day": {
        "quality": "Solar Birth — Extroverted, Visible, Action-Oriented",
        "description": "Born during daylight hours, you carry the Sun's energy prominently. You are naturally inclined toward public life, leadership, and visible achievements. Your soul purpose tends to manifest through external actions and worldly contributions.",
        "strengths": "Confidence, clarity of purpose, natural authority, and ability to inspire others",
        "spiritual": "Your spiritual path is through Karma Yoga — selfless action in the world"
    },
    "night": {
        "quality": "Lunar Birth — Introverted, Intuitive, Reflective",
        "description": "Born during nighttime hours, you carry the Moon's energy prominently. You are naturally inclined toward inner work, intuition, and subtle influence. Your soul purpose tends to manifest through reflection, creativity, and emotional depth.",
        "strengths": "Deep intuition, emotional intelligence, creative imagination, and psychic sensitivity",
        "spiritual": "Your spiritual path is through Bhakti Yoga — devotion and emotional surrender"
    },
    "twilight": {
        "quality": "Sandhya Birth — Balanced, Transitional, Mystical",
        "description": "Born during the sacred twilight (Sandhya Kaal), you carry a unique blend of solar and lunar energies. This is considered a spiritually potent time in Vedic tradition. You possess qualities of both day and night births.",
        "strengths": "Spiritual sensitivity, balance between action and reflection, strong meditation abilities",
        "spiritual": "Your spiritual path is through Dhyana Yoga — meditation and inner stillness"
    }
}


def get_nakshatra_info(nakshatra_name: str) -> dict:
    """Get detailed information about a specific Nakshatra."""
    return NAKSHATRAS.get(nakshatra_name, {})


def get_rashi_info(rashi_name: str) -> dict:
    """Get detailed information about a specific Rashi (Moon Sign)."""
    return RASHIS.get(rashi_name, {})


def get_dasha_info(planet: str) -> dict:
    """Get interpretation for a planetary Dasha period."""
    return DASHA_INTERPRETATIONS.get(planet, {})


def get_hora_info(planet: str) -> dict:
    """Get interpretation for a planetary Hora."""
    return HORA_LORDS.get(planet, {})


def get_muhurta_info(muhurta_name: str) -> dict:
    """Get interpretation for a specific Muhurta."""
    return MUHURTA_DATA.get(muhurta_name, {})


def get_ascendant_info(sign: str) -> dict:
    """Get Lagna/Ascendant traits for a sign."""
    return ASCENDANT_TRAITS.get(sign, {})


def build_knowledge_context(astro_data: dict) -> str:
    """Build a rich knowledge context string based on the user's astrological data."""
    context_parts = []

    moon_sign = astro_data.get("moon_sign", "")
    nakshatra = astro_data.get("nakshatra", "")
    current_dasha = astro_data.get("current_dasha", "")
    major_transit = astro_data.get("major_transit", "")

    # Moon Sign knowledge
    if moon_sign and moon_sign in RASHIS:
        rashi = RASHIS[moon_sign]
        context_parts.append(f"""MOON SIGN - {moon_sign}:
Ruler: {rashi['ruler']} | Element: {rashi['element']} | Quality: {rashi['quality']}
Key Traits: {rashi['traits']}
Compatible Signs: {', '.join(rashi['compatible'])}""")

    # Nakshatra knowledge
    if nakshatra and nakshatra in NAKSHATRAS:
        nak = NAKSHATRAS[nakshatra]
        context_parts.append(f"""NAKSHATRA - {nakshatra}:
Ruling Planet: {nak['ruler']} | Deity: {nak['deity']} | Symbol: {nak['symbol']}
Core Traits: {nak['traits']}
Career Guidance: {nak['career']}
Relationship Pattern: {nak['relationships']}
Health Tendencies: {nak['health']}
Remedies: {nak['remedies']}""")

    # Dasha knowledge
    if current_dasha:
        for planet_name, dasha_info in DASHA_INTERPRETATIONS.items():
            if planet_name in current_dasha:
                context_parts.append(f"""DASHA - {planet_name} ({dasha_info['duration']}):
{dasha_info['theme']}""")

    # Transit knowledge
    if major_transit and major_transit in TRANSIT_EFFECTS:
        context_parts.append(f"""CURRENT TRANSIT - {major_transit}:
{TRANSIT_EFFECTS[major_transit]}""")

    # Time-based knowledge
    hora_lord = astro_data.get("hora_lord", "")
    if hora_lord and hora_lord in HORA_LORDS:
        hora = HORA_LORDS[hora_lord]
        context_parts.append(f"""HORA LORD (Birth Hour Ruler) - {hora_lord}:
Quality: {hora['quality']}
Energy: {hora['energy']}
Advice: {hora['advice']}""")

    muhurta = astro_data.get("muhurta", "")
    if muhurta and muhurta in MUHURTA_DATA:
        m = MUHURTA_DATA[muhurta]
        context_parts.append(f"""BIRTH MUHURTA - {muhurta} ({m['quality']}):
Deity: {m['deity']}
{m['description']}""")

    ascending = astro_data.get("ascending_influence", "")
    for sign in ASCENDANT_TRAITS:
        if sign in ascending:
            asc = ASCENDANT_TRAITS[sign]
            context_parts.append(f"""ASCENDING SIGN (LAGNA) - {sign}:
Personality: {asc['quality']}
Appearance: {asc['appearance']}
Life Theme: {asc['life_theme']}""")
            break

    birth_quality = astro_data.get("birth_quality", "")
    for time_type, info in DAY_NIGHT_BIRTH.items():
        if info['quality'] in birth_quality:
            context_parts.append(f"""BIRTH TIME QUALITY - {info['quality']}:
{info['description']}
Strengths: {info['strengths']}
Spiritual Path: {info['spiritual']}""")
            break

    return "\n\n".join(context_parts)

