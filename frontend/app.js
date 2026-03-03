/**
 * DIVYAVANI — Unified App v12.0
 * Single-page: Entry → Choose Path → Chat / Report
 * Includes: Numerology Engine, Backend API, STT, TTS
 */

const BACKEND_URL = 'https://divyavision.onrender.com';

// ═══════════════════════════════════════════
//  PYTHAGOREAN LETTER MAP & DATA
// ═══════════════════════════════════════════

const LETTER_MAP = {
    A: 1, B: 2, C: 3, D: 4, E: 5, F: 6, G: 7, H: 8, I: 9,
    J: 1, K: 2, L: 3, M: 4, N: 5, O: 6, P: 7, Q: 8, R: 9,
    S: 1, T: 2, U: 3, V: 4, W: 5, X: 6, Y: 7, Z: 8
};
const VOWELS = new Set(['A', 'E', 'I', 'O', 'U']);

const NUMEROLOGY_DATA = {
    1: { title: "The Leader & Innovator", planet: "Sun", element: "Fire", keywords: ["Pioneer", "Independent", "Driven", "Original"], nature: "You are fiercely independent, original, and driven. You prefer to carve your own path rather than follow the crowd and possess a strong, pioneering spirit.", strengths: "Courage, originality, unwavering determination, self-reliance, and an innate capacity for leadership.", challenges: "Arrogance, stubbornness, impatience, and a tendency to become domineering or struggle with teamwork.", lucky_color: "Red", lucky_day: "Sunday", lucky_gemstone: "Ruby", career: "Entrepreneurship, management, inventing, or freelance work. You thrive when you can be the boss and execute your own vision.", relationships: "You are passionate and protective but absolutely require a partner who respects your fundamental need for independence.", compatible_numbers: [3, 5, 9], famous_people: ["Steve Jobs", "Martin Luther King Jr.", "Lady Gaga"], destiny_description: "Your Destiny Number {n} (Sun) reveals a purpose built on leadership, innovation, and blazing trails that others will follow." },
    2: { title: "The Peacemaker & Diplomat", planet: "Moon", element: "Water", keywords: ["Diplomat", "Empathetic", "Cooperative", "Intuitive"], nature: "You are highly sensitive, empathetic, and cooperative. You thrive in partnerships and seek to create harmony and balance in every environment you enter.", strengths: "Diplomacy, profound intuition, patience, emotional intelligence, and a calming presence.", challenges: "Over-sensitivity, indecisiveness, avoiding necessary conflict, and losing your personal identity in relationships.", lucky_color: "Orange", lucky_day: "Monday", lucky_gemstone: "Moonstone", career: "Counseling, mediation, human resources, teaching, or the arts.", relationships: "Deeply devoted and loving. You crave a profound emotional connection and need a gentle, communicative partner.", compatible_numbers: [4, 6, 8], famous_people: ["Barack Obama", "Madonna", "Emma Watson"], destiny_description: "Your Destiny Number {n} (Moon) reveals a purpose built on harmony, partnership, and being the compassionate glue." },
    3: { title: "The Communicator & Creative", planet: "Jupiter", element: "Air", keywords: ["Creative", "Expressive", "Joyful", "Charismatic"], nature: "You are the life of the party—expressive, charismatic, and endlessly creative. You process the world through self-expression.", strengths: "Brilliant communication skills, boundless artistic talent, optimism, and the ability to inspire others.", challenges: "Scattering your energy, superficiality, lack of focus, and struggling with routine or discipline.", lucky_color: "Yellow", lucky_day: "Thursday", lucky_gemstone: "Yellow Sapphire", career: "Entertainment, writing, public relations, design, broadcasting, or performing arts.", relationships: "You bring fun and spontaneity to love. You need a partner who appreciates your humor and grand gestures.", compatible_numbers: [1, 5, 7], famous_people: ["Albert Einstein", "Christina Aguilera", "Swami Vivekananda"], destiny_description: "Your Destiny Number {n} (Jupiter) reveals a purpose built on creative expression and joyful communication." },
    4: { title: "The Builder & Practical Mind", planet: "Uranus", element: "Earth", keywords: ["Builder", "Practical", "Grounded", "Reliable"], nature: "You are the rock. Grounded, methodical, and incredibly hardworking, you value stability, order, and building foundations that last.", strengths: "Unwavering loyalty, dedication, impeccable organization, practicality, and trustworthiness.", challenges: "Rigidity, stubbornness, missing the bigger picture by focusing on details, and becoming a workaholic.", lucky_color: "Green", lucky_day: "Tuesday", lucky_gemstone: "Emerald", career: "Architecture, engineering, finance, law, project management, or agriculture.", relationships: "Steady, loyal, and protective. You show love through acts of service and providing security.", compatible_numbers: [2, 6, 8], famous_people: ["Bill Gates", "Oprah Winfrey", "Elton John"], destiny_description: "Your Destiny Number {n} (Uranus) reveals a purpose built on creating lasting structures and reliable systems." },
    5: { title: "The Explorer & Free Spirit", planet: "Mercury", element: "Air", keywords: ["Explorer", "Adaptable", "Dynamic", "Fearless"], nature: "You crave freedom, adventure, and variety. Highly adaptable and curious about the world, you are a dynamic force.", strengths: "Adaptability, resourcefulness, progressive thinking, charisma, and a fearless approach to life.", challenges: "Restlessness, inconsistency, impatience, and a deep-seated fear of commitment or being tied down.", lucky_color: "Blue", lucky_day: "Wednesday", lucky_gemstone: "Turquoise", career: "Travel, journalism, sales, marketing, or aviation.", relationships: "You require a dynamic, adventurous partner. You cannot tolerate boredom or routine in love.", compatible_numbers: [1, 3, 7], famous_people: ["Angelina Jolie", "Abraham Lincoln", "Mick Jagger"], destiny_description: "Your Destiny Number {n} (Mercury) reveals a purpose built on exploration and bringing the energy of change." },
    6: { title: "The Nurturer & Caregiver", planet: "Venus", element: "Earth", keywords: ["Nurturer", "Responsible", "Harmonious", "Loving"], nature: "You are the caretaker of the numbers. Loving and responsible, you have a deep sense of justice and beauty.", strengths: "Profound compassion, protectiveness, a strong aesthetic sense, deep empathy, and loyalty.", challenges: "Self-righteousness, interference, anxiety, and a tendency to become overly possessive or smothering.", lucky_color: "Pink", lucky_day: "Friday", lucky_gemstone: "Diamond", career: "Healthcare, teaching, interior design, social work, culinary arts, or therapy.", relationships: "The most romantic and devoted partner. Family is everything to you.", compatible_numbers: [2, 4, 8], famous_people: ["Mother Teresa", "John Lennon", "Sachin Tendulkar"], destiny_description: "Your Destiny Number {n} (Venus) reveals a purpose built on nurturing, healing, and weaving beauty into life." },
    7: { title: "The Seeker & Intellectual", planet: "Neptune", element: "Water", keywords: ["Seeker", "Analytical", "Mystical", "Observant"], nature: "You are analytical, observant, and deeply spiritual. You seek the hidden truth beneath the surface of reality.", strengths: "A brilliant analytical mind, deep intuition, spiritual refinement, and excellent problem-solving skills.", challenges: "Aloofness, cynicism, over-thinking, isolating yourself, and potential social awkwardness.", lucky_color: "Purple", lucky_day: "Monday", lucky_gemstone: "Amethyst", career: "Scientific research, psychology, investigative journalism, academia, or esoteric studies.", relationships: "You require an intellectual and spiritual connection above all else.", compatible_numbers: [3, 5, 9], famous_people: ["Princess Diana", "Leonardo DiCaprio", "Marilyn Monroe"], destiny_description: "Your Destiny Number {n} (Neptune) reveals a purpose built on uncovering hidden truths and bridging worlds." },
    8: { title: "The Powerhouse & Achiever", planet: "Saturn", element: "Earth", keywords: ["Powerhouse", "Ambitious", "Authoritative", "Driven"], nature: "You are ambitious, authoritative, and focused on the material world. You understand how to manage resources and leave a legacy.", strengths: "Executive leadership, financial acumen, incredible resilience, confidence, and determination.", challenges: "Materialism, ruthlessness, controlling behavior, and sacrificing personal life for ambition.", lucky_color: "Black", lucky_day: "Saturday", lucky_gemstone: "Onyx", career: "Corporate leadership, real estate, investment banking, law, or running enterprises.", relationships: "You treat relationships as serious partnerships. You show love by providing rock-solid security.", compatible_numbers: [2, 4, 6], famous_people: ["Nelson Mandela", "Pablo Picasso", "Muhammad Ali"], destiny_description: "Your Destiny Number {n} (Saturn) reveals a purpose built on discipline, material mastery, and sustained effort." },
    9: { title: "The Humanitarian & Old Soul", planet: "Mars", element: "Fire", keywords: ["Humanitarian", "Compassionate", "Idealistic", "Wise"], nature: "You are an old soul—compassionate, idealistic, and deeply concerned with the state of the world.", strengths: "Universal love, boundless generosity, profound wisdom, broad-mindedness, and forgiveness.", challenges: "Disappointment when reality falls short of ideals, emotional volatility, and self-sacrifice.", lucky_color: "Gold", lucky_day: "Tuesday", lucky_gemstone: "Bloodstone", career: "Philanthropy, environmentalism, global politics, human rights advocacy, or healing arts.", relationships: "You love deeply but are often focused on humanity. You need a partner who shares your vision.", compatible_numbers: [1, 3, 7], famous_people: ["Mahatma Gandhi", "Bob Marley", "Jim Carrey"], destiny_description: "Your Destiny Number {n} (Mars) reveals a purpose built on compassion, completion, and selflessly elevating humanity." }
};

// ═══════════════════════════════════════════
//  CALCULATION ENGINE
// ═══════════════════════════════════════════

function reduceToSingleDigit(n) { while (n > 9) { n = String(n).split('').reduce((s, d) => s + parseInt(d), 0); } return n; }
function calcLifePath(dob) { try { const d = dob.split('-')[2]; return reduceToSingleDigit(d.split('').reduce((s, c) => s + parseInt(c), 0)); } catch { return 1; } }
function calcDestiny(name) { try { const c = name.toUpperCase().replace(/[^A-Z]/g, ''); return reduceToSingleDigit(c.split('').reduce((s, ch) => s + (LETTER_MAP[ch] || 0), 0)) || 1; } catch { return 1; } }
function calcSoulUrge(name) { try { const c = name.toUpperCase().replace(/[^A-Z]/g, ''); return reduceToSingleDigit(c.split('').filter(ch => VOWELS.has(ch)).reduce((s, ch) => s + (LETTER_MAP[ch] || 0), 0)) || 1; } catch { return 1; } }
function calcPersonality(name) { try { const c = name.toUpperCase().replace(/[^A-Z]/g, ''); return reduceToSingleDigit(c.split('').filter(ch => !VOWELS.has(ch)).reduce((s, ch) => s + (LETTER_MAP[ch] || 0), 0)) || 1; } catch { return 1; } }

function computeNumerology(name, dob) {
    const lp = calcLifePath(dob), destiny = calcDestiny(name), soulUrge = calcSoulUrge(name), personality = calcPersonality(name);
    const t = NUMEROLOGY_DATA[lp] || NUMEROLOGY_DATA[1];
    return { life_path_number: lp, destiny_number: destiny, soul_urge_number: soulUrge, personality_number: personality, ...t, destiny_description: (t.destiny_description || '').replace('{n}', destiny) };
}

// ═══════════════════════════════════════════
//  STATE
// ═══════════════════════════════════════════

const appState = {
    astroData: null,       // Backend computed chart
    numerologyData: null,  // Frontend computed report
    conversation: [],
    isListening: false,
    isSpeaking: false,
    isMuted: false,
    userName: '',
    userDob: ''
};

// ═══════════════════════════════════════════
//  DOM REFERENCES
// ═══════════════════════════════════════════

const views = {
    entry: document.getElementById('view-entry'),
    choose: document.getElementById('view-choose'),
    chat: document.getElementById('view-chat'),
    report: document.getElementById('view-report')
};

const sidebar = document.getElementById('chat-sidebar');
const mainContent = document.getElementById('main-content');
const chatGuideHeader = document.getElementById('chat-guide-header');
const defaultHeaderLogo = document.getElementById('default-header-logo');

const birthForm = document.getElementById('birth-form');
const btnBack = document.getElementById('btn-back');
const btnChatBack = document.getElementById('btn-chat-back');
const btnMute = document.getElementById('btn-mute');
const muteIcon = document.getElementById('mute-icon');
const btnGoChat = document.getElementById('btn-go-chat');
const btnGoReport = document.getElementById('btn-go-report');
const btnNewReading = document.getElementById('btn-new-reading');
const chooseSummary = document.getElementById('choose-summary');

// Chat DOM
const chatContainer = document.getElementById('chat-container');
const chatInput = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');
const micBtn = document.getElementById('mic-btn');
const sttStatus = document.getElementById('stt-status');

// ═══════════════════════════════════════════
//  VIEW MANAGEMENT
// ═══════════════════════════════════════════

let currentView = 'entry';
let viewHistory = [];

function showView(viewName) {
    viewHistory.push(currentView);
    Object.values(views).forEach(v => v.classList.remove('active'));
    views[viewName].classList.add('active');
    currentView = viewName;

    // Toggle sidebar
    if (viewName === 'chat') {
        sidebar.classList.add('active');
        chatGuideHeader.style.display = 'block';
        defaultHeaderLogo.style.display = 'none';
        mainContent.classList.add('with-sidebar');
        // Show chat-specific back & mute buttons
        btnChatBack.style.display = 'flex';
        btnMute.style.display = 'flex';
    } else {
        sidebar.classList.remove('active');
        chatGuideHeader.style.display = 'none';
        defaultHeaderLogo.style.display = 'flex';
        mainContent.classList.remove('with-sidebar');
        // Hide chat-specific buttons
        btnChatBack.style.display = 'none';
        btnMute.style.display = 'none';
    }

    // Toggle back button (for choose/report views)
    btnBack.style.display = (viewName === 'entry' || viewName === 'chat') ? 'none' : 'flex';

    // Allow scroll on report
    if (viewName === 'report') {
        document.body.style.overflow = 'auto';
        mainContent.style.overflow = 'auto';
        mainContent.style.height = 'auto';
    } else {
        document.body.style.overflow = 'hidden';
        mainContent.style.overflow = 'hidden';
        mainContent.style.height = '100%';
    }
}

btnNewReading.addEventListener('click', () => {
    // Reset app state
    chatInitialized = false;
    // Clear only messages, keep the welcome card
    const messages = chatContainer.querySelectorAll('.msg-wrapper');
    messages.forEach(m => m.remove());

    // Re-show welcome card
    const welcome = chatContainer.querySelector('.welcome-seeker-card');
    if (welcome) welcome.style.display = 'block';

    showView('entry');
});

btnBack.addEventListener('click', () => {
    if (currentView === 'chat' || currentView === 'report') {
        showView('choose');
    } else if (currentView === 'choose') {
        showView('entry');
    }
});

// Chat-specific back button
btnChatBack.addEventListener('click', () => {
    showView('choose');
});

// Mute/Unmute toggle
btnMute.addEventListener('click', () => {
    appState.isMuted = !appState.isMuted;
    if (appState.isMuted) {
        muteIcon.textContent = 'volume_off';
        btnMute.classList.add('muted');
        btnMute.title = 'Unmute Voice';
        // Stop any current speech
        if (synth.speaking) synth.cancel();
    } else {
        muteIcon.textContent = 'volume_up';
        btnMute.classList.remove('muted');
        btnMute.title = 'Mute Voice';
    }
});

// ═══════════════════════════════════════════
//  FORM SUBMISSION → CHOOSE PATH
// ═══════════════════════════════════════════

birthForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const name = document.getElementById('inp-name').value.trim();
    const dob = document.getElementById('inp-dob').value;
    const hour = document.getElementById('inp-hour').value;
    const minute = document.getElementById('inp-minute').value;
    const ampm = document.getElementById('inp-ampm').value;
    const time = `${hour}:${minute} ${ampm}`;
    const location = document.getElementById('inp-location').value || 'India';

    if (!name || !dob) return;

    appState.userName = name;
    appState.userDob = dob;

    // 1. Compute local numerology for report
    appState.numerologyData = computeNumerology(name, dob);

    // 2. Call backend for astro chart (used for chat)
    try {
        const res = await fetch(`${BACKEND_URL}/compute-chart`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, dob, time, location })
        });
        if (res.ok) {
            appState.astroData = await res.json();
        } else {
            // Fallback: use local data as mock astro
            appState.astroData = { moon_sign: appState.numerologyData.planet, nakshatra: "Rohini", current_dasha: "Sun Mahadasha", major_transit: "Jupiter transit", birth_time_formatted: time, hora_lord: "", birth_quality: "", muhurta: "", ascending_influence: "", time_analysis_summary: "" };
        }
    } catch {
        appState.astroData = { moon_sign: appState.numerologyData.planet, nakshatra: "Rohini", current_dasha: "Sun Mahadasha", major_transit: "Jupiter transit", birth_time_formatted: time, hora_lord: "", birth_quality: "", muhurta: "", ascending_influence: "", time_analysis_summary: "" };
    }

    // 3. Update choose screen summary
    const timeDisplay = appState.astroData.birth_time_formatted || time;
    chooseSummary.textContent = `Welcome, ${name}. Born at ${timeDisplay}. Life Path Number ${appState.numerologyData.life_path_number} — ${appState.numerologyData.title}. Choose how you'd like to explore.`;

    // 4. Show choose path view
    showView('choose');
});

// ═══════════════════════════════════════════
//  CHOOSE PATH → CHAT or REPORT
// ═══════════════════════════════════════════

btnGoChat.addEventListener('click', () => {
    showView('chat');
    initChat();
});

btnGoReport.addEventListener('click', () => {
    renderReport(appState.numerologyData);
    showView('report');
});

// ═══════════════════════════════════════════
//  REPORT RENDERING
// ═══════════════════════════════════════════

function renderReport(d) {
    document.getElementById('r-lp-num').textContent = d.life_path_number;
    document.getElementById('r-planet').textContent = d.planet;
    document.getElementById('r-element').textContent = d.element;
    document.getElementById('r-destiny-num').textContent = d.destiny_number;
    document.getElementById('r-soul-num').textContent = d.soul_urge_number;
    document.getElementById('r-personality-num').textContent = d.personality_number;

    const kw = document.getElementById('r-keywords');
    kw.innerHTML = '';
    d.keywords.forEach(k => { const s = document.createElement('span'); s.className = 'kw-chip'; s.textContent = k; kw.appendChild(s); });

    document.getElementById('r-color').textContent = d.lucky_color;
    document.getElementById('r-day').textContent = d.lucky_day;
    document.getElementById('r-gem').textContent = d.lucky_gemstone;
    document.getElementById('r-strengths').textContent = d.strengths;
    document.getElementById('r-challenges').textContent = d.challenges;
    document.getElementById('r-nature').textContent = d.nature;
    document.getElementById('r-destiny-desc').textContent = d.destiny_description;
    document.getElementById('r-career').textContent = d.career;
    document.getElementById('r-relationships').textContent = d.relationships;

    const compat = document.getElementById('r-compat');
    compat.innerHTML = '';
    d.compatible_numbers.forEach(n => { const b = document.createElement('div'); b.className = 'compat-badge'; b.textContent = n; compat.appendChild(b); });

    const famous = document.getElementById('r-famous');
    famous.innerHTML = '';
    d.famous_people.forEach(p => { const c = document.createElement('span'); c.className = 'famous-chip'; c.textContent = p; famous.appendChild(c); });

    // Time Analysis section
    if (appState.astroData) {
        const a = appState.astroData;
        document.getElementById('r-birth-time').textContent = a.birth_time_formatted || '—';
        document.getElementById('r-hora-lord').textContent = a.hora_lord || '—';
        document.getElementById('r-muhurta').textContent = a.muhurta || '—';
        document.getElementById('r-ascending').textContent = a.ascending_influence || '—';
        document.getElementById('r-birth-quality').textContent = a.birth_quality || '—';
    }
}

// ═══════════════════════════════════════════
//  CHAT LOGIC
// ═══════════════════════════════════════════

let chatInitialized = false;

function initChat() {
    if (chatInitialized) return;
    chatInitialized = true;

    let greeting;
    if (appState.astroData) {
        const d = appState.astroData;
        let timePart = '';
        if (d.birth_time_formatted) timePart += ` Born at ${d.birth_time_formatted}.`;
        if (d.hora_lord) timePart += ` Your birth hour is ruled by ${d.hora_lord}.`;
        if (d.birth_quality) timePart += ` ${d.birth_quality}.`;
        greeting = `Greetings, ${appState.userName}.${timePart} The moon is in ${d.moon_sign}, and you are under ${d.current_dasha}. How may I assist your spiritual journey today?`;
    } else {
        greeting = `Welcome, ${appState.userName}. Speak your mind, and I shall guide you.`;
    }

    appendMessage('system', greeting);
    speak(greeting);
}

function appendMessage(role, text) {
    const wrapper = document.createElement('div');
    const isAi = (role === 'system' || role === 'ai');
    wrapper.className = `msg-wrapper ${isAi ? 'ai' : 'user'} fade-up`;

    // Avatar/Icon
    const avatar = document.createElement('div');
    if (isAi) {
        avatar.className = 'ai-avatar-icon';
        avatar.innerHTML = '<span class="material-symbols-outlined" style="font-size:16px;">om</span>';
    } else {
        avatar.className = 'user-avatar-icon';
        avatar.innerHTML = '<span class="material-symbols-outlined">person</span>';
    }
    wrapper.appendChild(avatar);

    const bubble = document.createElement('div');
    bubble.className = 'msg-bubble';
    bubble.textContent = text;

    const meta = document.createElement('div');
    meta.className = 'msg-meta';
    const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    if (isAi) {
        meta.textContent = `${timeStr} · WISDOM CHANNELED`;
    } else {
        meta.textContent = timeStr;
    }

    bubble.appendChild(meta);

    // If AI and certain patterns matched, add action buttons
    if (isAi && text.toLowerCase().includes('report')) {
        const actions = document.createElement('div');
        actions.className = 'chat-actions-row';
        actions.innerHTML = `
            <button class="action-btn-pill btn-gold-fill"><span class="material-symbols-outlined" style="font-size:14px;">lock</span> UNLOCK FULL REPORT</button>
            <button class="action-btn-pill btn-outline"><span class="material-symbols-outlined" style="font-size:14px;">calendar_month</span> BOOK A SESSION</button>
        `;
        bubble.appendChild(actions);
    }

    wrapper.appendChild(bubble);
    chatContainer.appendChild(wrapper);

    // Hide welcome card if present AND this is a user message
    const welcome = document.querySelector('.welcome-seeker-card');
    if (welcome && !isAi) welcome.style.display = 'none';

    scrollToBottom();
}

function showTyping() {
    const w = document.createElement('div');
    w.className = 'msg-wrapper system'; w.id = 'typing-indicator';
    w.innerHTML = '<div class="typing-indicator"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>';
    chatContainer.appendChild(w);
    scrollToBottom();
}

function removeTyping() { const el = document.getElementById('typing-indicator'); if (el) el.remove(); }
function scrollToBottom() { chatContainer.scrollTo({ top: chatContainer.scrollHeight, behavior: 'smooth' }); }

async function handleSend() {
    const text = chatInput.value.trim();
    if (!text) return;

    appendMessage('user', text);
    chatInput.value = '';
    if (appState.isListening) stopListening();
    if (appState.isSpeaking) synth.cancel();

    showTyping();

    try {
        const payload = {
            astro_data: appState.astroData || { status: "No chart" },
            question: text
        };
        const res = await fetch(`${BACKEND_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        if (!res.ok) throw new Error("Connection interrupted");
        const data = await res.json();
        removeTyping();
        appendMessage('system', data.reply);
        speak(data.reply);

        // Fire-and-forget save
        fetch(`${BACKEND_URL}/save-session`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: text, ai_response: data.reply })
        }).catch(() => { });
    } catch {
        removeTyping();
        const err = "I sense a disturbance in the cosmic connection. Please try again in a moment.";
        appendMessage('system', err);
        speak(err);
    }
}

sendBtn.addEventListener('click', handleSend);
chatInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') { e.preventDefault(); handleSend(); } });

// ═══════════════════════════════════════════
//  SPEECH-TO-TEXT (STT)
// ═══════════════════════════════════════════

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition = null;

if (SpeechRecognition) {
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = true;
    recognition.lang = 'en-IN';

    recognition.onstart = () => { appState.isListening = true; micBtn.classList.add('listening'); sttStatus.style.display = 'block'; };
    recognition.onresult = (event) => {
        let finalT = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) finalT += event.results[i][0].transcript;
        }
        if (finalT) chatInput.value = finalT;
    };
    recognition.onerror = () => stopListening();
    recognition.onend = () => stopListening();
} else {
    micBtn.style.display = 'none';
}

function stopListening() { if (recognition) recognition.stop(); appState.isListening = false; micBtn.classList.remove('listening'); sttStatus.style.display = 'none'; }

micBtn.addEventListener('click', () => {
    if (appState.isListening) { stopListening(); } else { recognition.start(); }
});

// ═══════════════════════════════════════════
//  TEXT-TO-SPEECH (TTS)
// ═══════════════════════════════════════════

const synth = window.speechSynthesis;

function speak(text) {
    if (appState.isMuted) return; // Respect mute setting
    if (synth.speaking) synth.cancel();
    const utt = new SpeechSynthesisUtterance(text);
    const voices = synth.getVoices();
    let voice = voices.find(v => v.name.includes('Google UK English Female'));
    if (!voice) voice = voices.find(v => v.lang.includes('en-IN') || v.lang.includes('en-GB'));
    if (voice) utt.voice = voice;
    utt.pitch = 0.9; utt.rate = 0.9;
    utt.onstart = () => { appState.isSpeaking = true; };
    utt.onend = () => { appState.isSpeaking = false; };
    utt.onerror = () => { appState.isSpeaking = false; };
    synth.speak(utt);
}

if (speechSynthesis.onvoiceschanged !== undefined) { speechSynthesis.onvoiceschanged = synth.getVoices; }

// ═══════════════════════════════════════════
//  INIT
// ═══════════════════════════════════════════

console.log("DIVYAVANI v12.0 — Unified SPA Ready.");
