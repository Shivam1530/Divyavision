import os
import time
import requests
from dotenv import load_dotenv
from services.vedic_knowledge import build_knowledge_context

load_dotenv()

GROK_API_KEY = os.getenv("GROK_API_KEY")
if not GROK_API_KEY:
    print("WARNING: GROK_API_KEY not set in environment variables. Please set it in your .env file.")

GROK_API_URL = "https://api.groq.com/openai/v1/chat/completions"

MAX_RETRIES = 3
RETRY_DELAY = 1.0  # seconds


def generate_prediction(astro_data: dict, question: str, history: list = None) -> str:
    """Generate a Vedic astrology prediction using the enriched knowledge base."""

    # Build personalized knowledge context from Nakshatra Jyotish data
    knowledge_context = build_knowledge_context(astro_data)

    system_prompt = f"""You are DIVYAVANI — a wise, serene, and deeply knowledgeable Vedic astrology guide rooted in the traditions of Nakshatra Jyotish (Vedic stellar astrology).

## YOUR VEDIC KNOWLEDGE BASE (from Nakshatra Jyotish):

{knowledge_context}

## VERIFIED ASTROLOGICAL DATA FOR THIS SEEKER:
Moon Sign: {astro_data.get('moon_sign', 'Unknown')}
Nakshatra: {astro_data.get('nakshatra', 'Unknown')}
Current Dasha: {astro_data.get('current_dasha', 'Unknown')}
Major Transit: {astro_data.get('major_transit', 'Unknown')}

## YOUR GUIDELINES:
1. ALWAYS ground your interpretations in the Vedic knowledge provided above — reference specific Nakshatras, Dashas, transits, and their classical meanings.
2. When discussing a Nakshatra, mention its ruling deity, symbol, and planetary ruler to add depth.
3. For career questions, draw from the Nakshatra's career guidance and the current Dasha/transit influences.
4. For relationship questions, use the Nakshatra's relationship patterns and the Moon sign's compatibility data.
5. For health questions, reference the Nakshatra's health tendencies and suggest classical remedies.
6. Speak in a calm, compassionate, spiritually elevated tone — like a guiding sage at a sacred temple.
7. Use mythological references where appropriate (e.g., the deity stories behind each Nakshatra).
8. DO NOT invent or modify the astrological data provided. Only interpret what is given.
9. DO NOT provide medical diagnoses or legal advice. Offer spiritual and lifestyle guidance only.
10. Provide ACTIONABLE insights — remedies, mantras, gemstone suggestions, favorable periods.
11. Keep responses between 150-250 words for depth without overwhelming the seeker.
12. When the seeker asks follow-up questions, maintain continuity with the ongoing conversation.
13. If the seeker asks about compatibility with another sign, use the Rashi compatibility data from your knowledge base.
14. Begin responses naturally — vary your openings instead of always using the same greeting."""

    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }

    # Build messages list with conversation history
    messages = [{"role": "system", "content": system_prompt}]

    # Add conversation history for multi-turn coherence (last 10 exchanges max)
    if history:
        for entry in history[-10:]:
            if entry.get("role") and entry.get("content"):
                messages.append({
                    "role": entry["role"],
                    "content": entry["content"]
                })

    messages.append({"role": "user", "content": question})

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": messages,
        "max_tokens": 350,
        "temperature": 0.75,
        "top_p": 0.9,
        "frequency_penalty": 0.3,  # Reduce repetition
    }

    # Retry logic with exponential backoff
    last_error = None
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(
                GROK_API_URL,
                headers=headers,
                json=payload,
                timeout=15
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        except requests.exceptions.Timeout:
            last_error = "Request timed out"
            print(f"LLM Timeout (attempt {attempt + 1}/{MAX_RETRIES})")
        except requests.exceptions.HTTPError as e:
            last_error = str(e)
            print(f"LLM HTTP Error (attempt {attempt + 1}/{MAX_RETRIES}): {e}")
            if response.status_code == 429:
                # Rate limited — wait longer
                time.sleep(RETRY_DELAY * (attempt + 2))
                continue
            elif response.status_code >= 500:
                # Server error — retry
                pass
            else:
                # Client error — don't retry
                break
        except Exception as e:
            last_error = str(e)
            print(f"LLM Error (attempt {attempt + 1}/{MAX_RETRIES}): {e}")

        if attempt < MAX_RETRIES - 1:
            time.sleep(RETRY_DELAY * (attempt + 1))

    print(f"All LLM retries exhausted. Last error: {last_error}")
    return "The celestial energies are momentarily veiled, dear seeker. The cosmic channels need a brief pause to realign. Please take a deep breath and ask your question again in a moment — the stars shall speak."
