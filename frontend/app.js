/**
 * DIVYAVANI — Numerology Engine (Pure Frontend)
 * v10.0 — No Backend Required. All calculations & data are local.
 * v11.0 — Instant Display & Full Insights (Redesigned)
 */

// ═══════════════════════════════════════════
//  PYTHAGOREAN LETTER MAP
// ═══════════════════════════════════════════

const LETTER_MAP = {
    A: 1, B: 2, C: 3, D: 4, E: 5, F: 6, G: 7, H: 8, I: 9,
    J: 1, K: 2, L: 3, M: 4, N: 5, O: 6, P: 7, Q: 8, R: 9,
    S: 1, T: 2, U: 3, V: 4, W: 5, X: 6, Y: 7, Z: 8
};
const VOWELS = new Set(['A', 'E', 'I', 'O', 'U']);

// ═══════════════════════════════════════════
//  NUMEROLOGY TRAIT DATA
// ═══════════════════════════════════════════

const NUMEROLOGY_DATA = {
    1: {
        title: "The Leader & Innovator",
        planet: "Sun",
        element: "Fire",
        keywords: ["Pioneer", "Independent", "Driven", "Original"],
        nature: "You are fiercely independent, original, and driven. You prefer to carve your own path rather than follow the crowd and possess a strong, pioneering spirit. As a natural-born leader, you process the world through action and self-discovery.",
        strengths: "Courage, originality, unwavering determination, self-reliance, and an innate capacity for leadership.",
        challenges: "Arrogance, stubbornness, impatience, and a tendency to become domineering or struggle with teamwork.",
        lucky_color: "Red",
        lucky_day: "Sunday",
        lucky_gemstone: "Ruby",
        career: "Entrepreneurship, management, inventing, or freelance work. You thrive when you can be the boss and execute your own vision.",
        relationships: "You are passionate and protective but absolutely require a partner who respects your fundamental need for independence. You cannot be smothered.",
        compatible_numbers: [3, 5, 9],
        famous_people: ["Steve Jobs", "Martin Luther King Jr.", "Lady Gaga"],
        destiny_description: "Your Destiny Number {n} (Sun) reveals a purpose built on leadership, innovation, and blazing trails that others will follow."
    },
    2: {
        title: "The Peacemaker & Diplomat",
        planet: "Moon",
        element: "Water",
        keywords: ["Diplomat", "Empathetic", "Cooperative", "Intuitive"],
        nature: "You are highly sensitive, empathetic, and cooperative. You thrive in partnerships and seek to create harmony and balance in every environment you enter. You are the ultimate team player.",
        strengths: "Diplomacy, profound intuition, patience, emotional intelligence, and a calming presence.",
        challenges: "Over-sensitivity, indecisiveness, avoiding necessary conflict, and losing your personal identity in relationships.",
        lucky_color: "Orange",
        lucky_day: "Monday",
        lucky_gemstone: "Moonstone",
        career: "Counseling, mediation, human resources, teaching, or the arts. You excel in supportive roles that require emotional intelligence.",
        relationships: "Deeply devoted and loving. You crave a profound emotional connection and need a gentle, communicative partner who makes you feel secure.",
        compatible_numbers: [4, 6, 8],
        famous_people: ["Barack Obama", "Madonna", "Emma Watson"],
        destiny_description: "Your Destiny Number {n} (Moon) reveals a purpose built on harmony, partnership, and being the compassionate glue that holds others together."
    },
    3: {
        title: "The Communicator & Creative",
        planet: "Jupiter",
        element: "Air",
        keywords: ["Creative", "Expressive", "Joyful", "Charismatic"],
        nature: "You are the life of the party—expressive, charismatic, and endlessly creative. You process the world through self-expression and bring joy, optimism, and humor to those around you.",
        strengths: "Brilliant communication skills, boundless artistic talent, optimism, and the ability to inspire others.",
        challenges: "Scattering your energy, superficiality, lack of focus, and struggling with routine or discipline.",
        lucky_color: "Yellow",
        lucky_day: "Thursday",
        lucky_gemstone: "Yellow Sapphire",
        career: "Entertainment, writing, public relations, design, broadcasting, or performing arts. You belong in the spotlight.",
        relationships: "You bring fun and spontaneity to love. You need a partner who appreciates your humor and grand gestures, but who also gives you the freedom to socialize.",
        compatible_numbers: [1, 5, 7],
        famous_people: ["Albert Einstein", "Christina Aguilera", "Swami Vivekananda"],
        destiny_description: "Your Destiny Number {n} (Jupiter) reveals a purpose built on creative expression, joyful communication, and inspiring others through art and word."
    },
    4: {
        title: "The Builder & Practical Mind",
        planet: "Uranus",
        element: "Earth",
        keywords: ["Builder", "Practical", "Grounded", "Reliable"],
        nature: "You are the rock. Grounded, methodical, and incredibly hardworking, you value stability, order, and building foundations that stand the test of time.",
        strengths: "Unwavering loyalty, dedication, impeccable organization, practicality, and trustworthiness.",
        challenges: "Rigidity, stubbornness, missing the bigger picture by focusing on details, and becoming a workaholic.",
        lucky_color: "Green",
        lucky_day: "Tuesday",
        lucky_gemstone: "Emerald",
        career: "Architecture, engineering, finance, law, project management, or agriculture. You excel where structure is required.",
        relationships: "Steady, loyal, and protective. You show love through acts of service and providing security rather than grand emotional displays.",
        compatible_numbers: [2, 6, 8],
        famous_people: ["Bill Gates", "Oprah Winfrey", "Elton John"],
        destiny_description: "Your Destiny Number {n} (Uranus) reveals a purpose built on creating lasting structures, reliable systems, and the solid foundations civilization depends on."
    },
    5: {
        title: "The Explorer & Free Spirit",
        planet: "Mercury",
        element: "Air",
        keywords: ["Explorer", "Adaptable", "Dynamic", "Fearless"],
        nature: "You crave freedom, adventure, and variety. Highly adaptable and curious about the world, you are a dynamic force constantly seeking new experiences and knowledge.",
        strengths: "Adaptability, resourcefulness, progressive thinking, charisma, and a fearless approach to life.",
        challenges: "Restlessness, inconsistency, impatience, and a deep-seated fear of commitment or being tied down.",
        lucky_color: "Blue",
        lucky_day: "Wednesday",
        lucky_gemstone: "Turquoise",
        career: "Travel, journalism, sales, marketing, or aviation. You need a career that avoids a repetitive 9-to-5 desk routine.",
        relationships: "You require a dynamic, adventurous partner. You cannot tolerate boredom or routine in love; your partner must be your fellow explorer.",
        compatible_numbers: [1, 3, 7],
        famous_people: ["Angelina Jolie", "Abraham Lincoln", "Mick Jagger"],
        destiny_description: "Your Destiny Number {n} (Mercury) reveals a purpose built on exploration, communication, and bringing the energy of change and progress to the world."
    },
    6: {
        title: "The Nurturer & Caregiver",
        planet: "Venus",
        element: "Earth",
        keywords: ["Nurturer", "Responsible", "Harmonious", "Loving"],
        nature: "You are the caretaker of the numbers. Loving and responsible, you have a deep sense of justice and beauty, creating warmth, harmony, and healing wherever you go.",
        strengths: "Profound compassion, protectiveness, a strong aesthetic sense, deep empathy, and loyalty.",
        challenges: "Self-righteousness, interference, anxiety, and a tendency to become overly possessive or smothering.",
        lucky_color: "Pink",
        lucky_day: "Friday",
        lucky_gemstone: "Diamond",
        career: "Healthcare, teaching, interior design, social work, culinary arts, or therapy.",
        relationships: "The most romantic and devoted partner. Family is everything to you. You create a beautiful home and need a partner who values deep, unconditional love.",
        compatible_numbers: [2, 4, 8],
        famous_people: ["Mother Teresa", "John Lennon", "Sachin Tendulkar"],
        destiny_description: "Your Destiny Number {n} (Venus) reveals a purpose built on nurturing, healing, and weaving beauty and love into the fabric of everyday life."
    },
    7: {
        title: "The Seeker & Intellectual",
        planet: "Neptune",
        element: "Water",
        keywords: ["Seeker", "Analytical", "Mystical", "Observant"],
        nature: "You are analytical, observant, and deeply spiritual. You seek the hidden truth beneath the surface of reality and require plenty of solitude to recharge your mind.",
        strengths: "A brilliant analytical mind, deep intuition, spiritual refinement, and excellent problem-solving skills.",
        challenges: "Aloofness, cynicism, over-thinking, isolating yourself, and potential social awkwardness.",
        lucky_color: "Purple",
        lucky_day: "Monday",
        lucky_gemstone: "Amethyst",
        career: "Scientific research, psychology, investigative journalism, academia, or esoteric and occult studies.",
        relationships: "You require an intellectual and spiritual connection above all else. You can seem distant, so you need a secure partner who understands your need for space.",
        compatible_numbers: [3, 5, 9],
        famous_people: ["Princess Diana", "Leonardo DiCaprio", "Marilyn Monroe"],
        destiny_description: "Your Destiny Number {n} (Neptune) reveals a purpose built on uncovering hidden truths, bridging the spiritual and material worlds through wisdom and analysis."
    },
    8: {
        title: "The Powerhouse & Achiever",
        planet: "Saturn",
        element: "Earth",
        keywords: ["Powerhouse", "Ambitious", "Authoritative", "Driven"],
        nature: "You are ambitious, authoritative, and focused on the material world. You understand how to manage resources and are driven by goals, tangible success, and leaving a legacy.",
        strengths: "Executive leadership, financial acumen, incredible resilience, confidence, and determination.",
        challenges: "Materialism, ruthlessness, controlling behavior, and sacrificing personal life for ambition.",
        lucky_color: "Black",
        lucky_day: "Saturday",
        lucky_gemstone: "Onyx",
        career: "Corporate leadership, real estate, investment banking, law, or running large-scale enterprises.",
        relationships: "You treat relationships as serious partnerships. You show love by providing rock-solid security and need a strong, equally driven partner to build an empire with.",
        compatible_numbers: [2, 4, 6],
        famous_people: ["Nelson Mandela", "Pablo Picasso", "Muhammad Ali"],
        destiny_description: "Your Destiny Number {n} (Saturn) reveals a purpose built on discipline, material mastery, and demonstrating that sustained effort can achieve anything."
    },
    9: {
        title: "The Humanitarian & Old Soul",
        planet: "Mars",
        element: "Fire",
        keywords: ["Humanitarian", "Compassionate", "Idealistic", "Wise"],
        nature: "You are an old soul—compassionate, idealistic, and deeply concerned with the state of the world. Representing completion, you are wise and driven by a need to give back to society.",
        strengths: "Universal love, boundless generosity, profound wisdom, broad-mindedness, and forgiveness.",
        challenges: "Disappointment when reality falls short of ideals, emotional volatility, holding onto the past, and self-sacrifice.",
        lucky_color: "Gold",
        lucky_day: "Tuesday",
        lucky_gemstone: "Bloodstone",
        career: "Philanthropy, environmentalism, global politics, human rights advocacy, or the healing arts.",
        relationships: "You love deeply but are often focused on the bigger picture of humanity. You need a partner who shares your idealistic vision and supports your humanitarian goals.",
        compatible_numbers: [1, 3, 7],
        famous_people: ["Mahatma Gandhi", "Bob Marley", "Jim Carrey"],
        destiny_description: "Your Destiny Number {n} (Mars) reveals a purpose built on compassion, completion, and selflessly elevating humanity as a whole."
    }
};

// ═══════════════════════════════════════════
//  CALCULATION ENGINE
// ═══════════════════════════════════════════

function reduceToSingleDigit(n) {
    while (n > 9) {
        n = String(n).split('').reduce((sum, d) => sum + parseInt(d), 0);
    }
    return n;
}

function calcLifePath(dob) {
    try {
        const day = dob.split('-')[2];
        const total = day.split('').reduce((sum, d) => sum + parseInt(d), 0);
        return reduceToSingleDigit(total);
    } catch { return 1; }
}

function calcDestiny(name) {
    try {
        const clean = name.toUpperCase().replace(/[^A-Z]/g, '');
        const total = clean.split('').reduce((sum, ch) => sum + (LETTER_MAP[ch] || 0), 0);
        return reduceToSingleDigit(total) || 1;
    } catch { return 1; }
}

function calcSoulUrge(name) {
    try {
        const clean = name.toUpperCase().replace(/[^A-Z]/g, '');
        const total = clean.split('').filter(ch => VOWELS.has(ch)).reduce((sum, ch) => sum + (LETTER_MAP[ch] || 0), 0);
        return reduceToSingleDigit(total) || 1;
    } catch { return 1; }
}

function calcPersonality(name) {
    try {
        const clean = name.toUpperCase().replace(/[^A-Z]/g, '');
        const total = clean.split('').filter(ch => !VOWELS.has(ch)).reduce((sum, ch) => sum + (LETTER_MAP[ch] || 0), 0);
        return reduceToSingleDigit(total) || 1;
    } catch { return 1; }
}

function computeNumerology(name, dob) {
    const lifePath = calcLifePath(dob);
    const destiny = calcDestiny(name);
    const soulUrge = calcSoulUrge(name);
    const personality = calcPersonality(name);

    const traits = NUMEROLOGY_DATA[lifePath] || NUMEROLOGY_DATA[1];
    const destinyTraits = NUMEROLOGY_DATA[destiny] || NUMEROLOGY_DATA[1];
    const soulTraits = NUMEROLOGY_DATA[soulUrge] || NUMEROLOGY_DATA[1];

    const destinyDesc = (traits.destiny_description || '').replace('{n}', destiny);

    return {
        life_path_number: lifePath,
        destiny_number: destiny,
        soul_urge_number: soulUrge,
        personality_number: personality,
        title: traits.title,
        ruling_planet: traits.planet,
        element: traits.element,
        keywords: traits.keywords,
        nature: traits.nature,
        strengths: traits.strengths,
        challenges: traits.challenges,
        lucky_color: traits.lucky_color,
        lucky_day: traits.lucky_day,
        lucky_gemstone: traits.lucky_gemstone,
        career: traits.career,
        relationships: traits.relationships,
        compatible_numbers: traits.compatible_numbers,
        famous_people: traits.famous_people,
        destiny_description: destinyDesc,
        soul_urge_description: `Your Soul Urge Number ${soulUrge} (${soulTraits.planet}) reflects your inner desire to ${soulTraits.nature.split('.')[0].toLowerCase()}.`,
    };
}

// ═══════════════════════════════════════════
//  DOM ELEMENTS
// ═══════════════════════════════════════════

const stepInputContainer = document.getElementById('step-input');
const resultContainer = document.getElementById('numerology-result');
const numerologyForm = document.getElementById('numerology-form');
const btnReveal = document.getElementById('btn-reveal');
const btnReset = document.getElementById('btn-reset');

// Result Elements
const resultNumber = document.getElementById('result-number');
const resultPlanet = document.getElementById('result-planet');
const resultElement = document.getElementById('result-element');
const resultKeywords = document.getElementById('result-keywords');
const resultNature = document.getElementById('result-nature');
const resultStrengths = document.getElementById('result-strengths');
const resultChallenges = document.getElementById('result-challenges');
const resultDestinyNumber = document.getElementById('result-destiny-number');
const resultSoulNumber = document.getElementById('result-soul-number');
const resultPersonalityNumber = document.getElementById('result-personality-number');
const resultDestinyDesc = document.getElementById('result-destiny-desc');
const resultCareer = document.getElementById('result-career');
const resultRelationships = document.getElementById('result-relationships');
const resultLuckyColor = document.getElementById('result-lucky-color');
const resultLuckyDay = document.getElementById('result-lucky-day');
const resultLuckyGem = document.getElementById('result-lucky-gem');
const resultCompatibility = document.getElementById('result-compatibility');
const resultFamous = document.getElementById('result-famous');

// State
let currentReportData = { name: '', dob: '' };

// ═══════════════════════════════════════════
//  FUNCTIONS
// ═══════════════════════════════════════════

async function revealAndRender(name, dob) {
    try {
        const result = computeNumerology(name, dob);
        currentReportData = { name, dob };
        renderReport(result);
        showResult();
        window.history.replaceState({}, '', `?name=${encodeURIComponent(name)}&dob=${encodeURIComponent(dob)}`);
    } catch (error) {
        console.error("Calculation Error:", error);
        alert(`Something went wrong: ${error.message}`);
    }
}

function showResult() {
    stepInputContainer.style.display = 'none';
    resultContainer.style.display = 'flex';
}

function renderReport(data) {
    if (resultNumber) resultNumber.textContent = data.life_path_number;
    if (resultPlanet) resultPlanet.textContent = data.ruling_planet;
    if (resultElement) resultElement.textContent = data.element;
    if (resultDestinyNumber) resultDestinyNumber.textContent = data.destiny_number;
    if (resultSoulNumber) resultSoulNumber.textContent = data.soul_urge_number;
    if (resultPersonalityNumber) resultPersonalityNumber.textContent = data.personality_number;

    if (resultKeywords) {
        resultKeywords.innerHTML = '';
        data.keywords.forEach(keyword => {
            const chip = document.createElement('span');
            chip.className = 'kw-chip';
            chip.textContent = keyword;
            resultKeywords.appendChild(chip);
        });
    }

    if (resultLuckyColor) resultLuckyColor.textContent = data.lucky_color;
    if (resultLuckyDay) resultLuckyDay.textContent = data.lucky_day;
    if (resultLuckyGem) resultLuckyGem.textContent = data.lucky_gemstone;
    if (resultStrengths) resultStrengths.textContent = data.strengths;
    if (resultChallenges) resultChallenges.textContent = data.challenges;
    if (resultNature) resultNature.textContent = data.nature;
    if (resultDestinyDesc) resultDestinyDesc.textContent = data.destiny_description;
    if (resultCareer) resultCareer.textContent = data.career;
    if (resultRelationships) resultRelationships.textContent = data.relationships;

    if (resultCompatibility) {
        resultCompatibility.innerHTML = '';
        data.compatible_numbers.forEach(num => {
            const badge = document.createElement('div');
            badge.className = 'compat-badge';
            badge.textContent = num;
            resultCompatibility.appendChild(badge);
        });
    }

    if (resultFamous) {
        resultFamous.innerHTML = '';
        data.famous_people.forEach(person => {
            const chip = document.createElement('span');
            chip.className = 'famous-chip';
            chip.textContent = person;
            resultFamous.appendChild(chip);
        });
    }
}

// ═══════════════════════════════════════════
//  EVENTS
// ═══════════════════════════════════════════

numerologyForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const dob = document.getElementById('dob').value;
    if (name && dob) revealAndRender(name, dob);
});

if (btnReset) {
    btnReset.addEventListener('click', () => {
        resultContainer.style.display = 'none';
        stepInputContainer.style.display = 'flex';
        numerologyForm.reset();
        window.history.replaceState({}, '', window.location.pathname);
    });
}

window.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    const name = params.get('name');
    const dob = params.get('dob');
    if (name && dob) revealAndRender(name, dob);
});

console.log("DIVYAVANI v11.0 Ready.");
