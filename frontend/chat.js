/**
 * chat.js - DIVYAVANI Serene Chat Logic
 * Handles STT, TTS, Backend API communication
 */

const BACKEND_URL = 'https://divyavision.onrender.com';

// State
const appState = {
    astroData: null,
    conversation: [],
    chatHistory: [], // {role: 'user'|'assistant', content: string}[]
    isListening: false,
    isSpeaking: false
};

// DOM Elements
const chatContainer = document.getElementById('chat-container');
const chatInput = document.getElementById('chat-input');
const sendBtn = document.getElementById('send-btn');
const micBtn = document.getElementById('mic-btn');
const sttStatus = document.getElementById('stt-status');
const endSessionBtn = document.getElementById('end-session-btn');

// --- Initialization ---

window.addEventListener('DOMContentLoaded', async () => {
    // Attempt to load params passed from the form (index.html -> app.js -> chat.html logic bypass)
    // For MVp, we check sessionStorage
    const storedData = sessionStorage.getItem('astroData');
    if (storedData) {
        appState.astroData = JSON.parse(storedData);
        // Automatically greet the user based on their moon sign
        const greeting = `Greetings. I am observing the current planetary alignment. The moon is in ${appState.astroData.moon_sign}. How may I assist your spiritual journey today?`;
        appendMessage('system', greeting);
        speak(greeting);
    } else {
        // Fallback for direct testing
        const fallbackMsg = "Welcome, Seeker. I am Divyavani. To provide precise cosmic insights, I usually need your birth chart. However, speak your mind, and I shall guide you.";
        appendMessage('system', fallbackMsg);
    }
});

// --- Speech Recognition (STT) ---

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition = null;

if (SpeechRecognition) {
    recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = true;
    recognition.lang = 'en-IN'; // Indian English for better local articulation parsing

    recognition.onstart = () => {
        appState.isListening = true;
        micBtn.classList.add('listening');
        sttStatus.style.display = 'block';
    };

    recognition.onresult = (event) => {
        let interimTranscript = '';
        let finalTranscript = '';

        for (let i = event.resultIndex; i < event.results.length; ++i) {
            if (event.results[i].isFinal) {
                finalTranscript += event.results[i][0].transcript;
            } else {
                interimTranscript += event.results[i][0].transcript;
            }
        }

        // Update input box
        if (finalTranscript) {
            chatInput.value = finalTranscript;
        } else {
            // Optionally show interim somewhere else to not interrupt typing
        }
    };

    recognition.onerror = (event) => {
        console.error("Speech Recognition Error:", event.error);
        stopListening();
    };

    recognition.onend = () => {
        stopListening();
    };
} else {
    micBtn.style.display = 'none'; // Hide mic if not supported
    console.warn("Speech Recognition API not supported in this browser.");
}

function stopListening() {
    if (recognition) recognition.stop();
    appState.isListening = false;
    micBtn.classList.remove('listening');
    sttStatus.style.display = 'none';
}

micBtn.addEventListener('click', () => {
    if (appState.isListening) {
        stopListening();
    } else {
        recognition.start();
    }
});

// --- Text-to-Speech (TTS) ---

const synth = window.speechSynthesis;

function speak(text) {
    if (synth.speaking) {
        synth.cancel(); // Cancel previous speech
    }

    const utterThis = new SpeechSynthesisUtterance(text);

    // Attempt to find a peaceful/calm voice. Female UK or IN usually sounds calmer.
    const voices = synth.getVoices();
    let selectedVoice = voices.find(v => v.name.includes('Google UK English Female'));
    if (!selectedVoice) selectedVoice = voices.find(v => v.lang.includes('en-IN') || v.lang.includes('en-GB'));

    if (selectedVoice) utterThis.voice = selectedVoice;

    utterThis.pitch = 0.9; // Slightly lower pitch for calmness
    utterThis.rate = 0.9;  // Slower rate for serenity

    utterThis.onstart = () => { appState.isSpeaking = true; };
    utterThis.onend = () => { appState.isSpeaking = false; };
    utterThis.onerror = () => { appState.isSpeaking = false; };

    synth.speak(utterThis);
}

// Make sure voices are loaded (Chrome quirk)
if (speechSynthesis.onvoiceschanged !== undefined) {
    speechSynthesis.onvoiceschanged = synth.getVoices;
}

// --- Chat Logic ---

function appendMessage(role, text) {
    const wrapper = document.createElement('div');
    wrapper.className = `msg-wrapper ${role} fade-in`;

    const bubble = document.createElement('div');
    bubble.className = 'msg-bubble';
    bubble.textContent = text;

    const meta = document.createElement('div');
    meta.className = 'msg-meta';

    const timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    if (role === 'system') {
        meta.innerHTML = `<span class="material-symbols-outlined" style="font-size:12px;">spa</span> ${timeStr} · WISDOM CHANNELED`;
    } else {
        meta.textContent = timeStr;
    }

    bubble.appendChild(meta);
    wrapper.appendChild(bubble);
    chatContainer.appendChild(wrapper);

    // Remove intro if it exists and this is the first real message
    const intro = document.querySelector('.chat-intro');
    if (intro && role === 'user') {
        intro.style.display = 'none';
    }

    scrollToBottom();
}

function showTyping() {
    const wrapper = document.createElement('div');
    wrapper.className = 'msg-wrapper system typing-wrap';
    wrapper.id = 'typing-indicator';

    const typing = document.createElement('div');
    typing.className = 'typing-indicator';
    typing.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';

    wrapper.appendChild(typing);
    chatContainer.appendChild(wrapper);
    scrollToBottom();
}

function removeTyping() {
    const ind = document.getElementById('typing-indicator');
    if (ind) ind.remove();
}

function scrollToBottom() {
    // Smooth scroll down
    chatContainer.scrollTo({
        top: chatContainer.scrollHeight,
        behavior: 'smooth'
    });
}

async function handleSend() {
    const text = chatInput.value.trim();
    if (!text) return;

    // 1. Show user message
    appendMessage('user', text);
    chatInput.value = '';

    // If listening, stop it
    if (appState.isListening) stopListening();
    if (appState.isSpeaking) synth.cancel();

    // 2. Show typing indicator
    showTyping();

    // 3. Call Backend
    try {
        const payload = {
            astro_data: appState.astroData || { status: "No chart provided. General query." },
            question: text,
            history: appState.chatHistory.length > 0 ? appState.chatHistory : null
        };

        const response = await fetch(`${BACKEND_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) throw new Error("Cosmic connection interrupted.");

        const data = await response.json();

        removeTyping();
        appendMessage('system', data.reply);
        speak(data.reply);

        // Track conversation history for multi-turn context
        appState.chatHistory.push({ role: 'user', content: text });
        appState.chatHistory.push({ role: 'assistant', content: data.reply });

        // Keep only last 10 exchanges (20 messages) to avoid payload bloat
        if (appState.chatHistory.length > 20) {
            appState.chatHistory = appState.chatHistory.slice(-20);
        }

        // Optional save session (fire and forget)
        fetch(`${BACKEND_URL}/save-session`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: text, ai_response: data.reply })
        }).catch(e => console.log("Session not saved:", e));

    } catch (error) {
        removeTyping();
        const errMsg = "I sense a disturbance in the cosmic connection right now. Please allow the energy to settle and try asking your question again.";
        appendMessage('system', errMsg);
        speak(errMsg);
    }
}

// --- Event Listeners ---

sendBtn.addEventListener('click', handleSend);
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        handleSend();
    }
});

endSessionBtn.addEventListener('click', () => {
    if (confirm("Are you sure you want to end this cosmic session?")) {
        sessionStorage.removeItem('astroData');
        window.location.href = 'index.html';
    }
});
