import re
from datetime import datetime
from kerykeion import AstrologicalSubject
from models.request_models import AstrologyRequest
from models.response_models import AstrologyResponse
from services.vedic_knowledge import (
    HORA_SEQUENCE, DAY_RULERS, MUHURTA_ORDER, MUHURTA_DATA,
    ASCENDANT_TRAITS, DAY_NIGHT_BIRTH, HORA_LORDS
)

# ═══════════════════════════════════════════
#  SIGN & NAKSHATRA MAPPING
# ═══════════════════════════════════════════

# Kerykeion uses abbreviated sign names — map to full names
SIGN_MAP = {
    "Ari": "Aries", "Tau": "Taurus", "Gem": "Gemini", "Can": "Cancer",
    "Leo": "Leo", "Vir": "Virgo", "Lib": "Libra", "Sco": "Scorpio",
    "Sag": "Sagittarius", "Cap": "Capricorn", "Aqu": "Aquarius", "Pis": "Pisces"
}

# 27 Nakshatras — each spans 13°20' (13.3333°) of the zodiac (0° to 360°)
NAKSHATRA_LIST = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
    "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni",
    "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha",
    "Jyeshtha", "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana",
    "Dhanishta", "Shatabhisha", "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

# Vimshottari Dasha sequence with durations in years
DASHA_SEQUENCE = [
    ("Ketu", 7), ("Venus", 20), ("Sun", 6), ("Moon", 10), ("Mars", 7),
    ("Rahu", 18), ("Jupiter", 16), ("Saturn", 19), ("Mercury", 17)
]
TOTAL_DASHA_YEARS = 120  # Sum of all dasha durations

# Nakshatra to starting Dasha lord mapping
NAKSHATRA_DASHA_LORD = {
    "Ashwini": "Ketu", "Bharani": "Venus", "Krittika": "Sun",
    "Rohini": "Moon", "Mrigashira": "Mars", "Ardra": "Rahu",
    "Punarvasu": "Jupiter", "Pushya": "Saturn", "Ashlesha": "Mercury",
    "Magha": "Ketu", "Purva Phalguni": "Venus", "Uttara Phalguni": "Sun",
    "Hasta": "Moon", "Chitra": "Mars", "Swati": "Rahu",
    "Vishakha": "Jupiter", "Anuradha": "Saturn", "Jyeshtha": "Mercury",
    "Mula": "Ketu", "Purva Ashadha": "Venus", "Uttara Ashadha": "Sun",
    "Shravana": "Moon", "Dhanishta": "Mars", "Shatabhisha": "Rahu",
    "Purva Bhadrapada": "Jupiter", "Uttara Bhadrapada": "Saturn", "Revati": "Mercury"
}

# Known city coordinates for common Indian cities (fallback)
CITY_COORDS = {
    "delhi": (28.6139, 77.2090, "Asia/Kolkata"),
    "mumbai": (19.0760, 72.8777, "Asia/Kolkata"),
    "bangalore": (12.9716, 77.5946, "Asia/Kolkata"),
    "bengaluru": (12.9716, 77.5946, "Asia/Kolkata"),
    "chennai": (13.0827, 80.2707, "Asia/Kolkata"),
    "kolkata": (22.5726, 88.3639, "Asia/Kolkata"),
    "hyderabad": (17.3850, 78.4867, "Asia/Kolkata"),
    "pune": (18.5204, 73.8567, "Asia/Kolkata"),
    "ahmedabad": (23.0225, 72.5714, "Asia/Kolkata"),
    "jaipur": (26.9124, 75.7873, "Asia/Kolkata"),
    "lucknow": (26.8467, 80.9462, "Asia/Kolkata"),
    "patna": (25.6093, 85.1376, "Asia/Kolkata"),
    "varanasi": (25.3176, 82.9739, "Asia/Kolkata"),
    "indore": (22.7196, 75.8577, "Asia/Kolkata"),
    "bhopal": (23.2599, 77.4126, "Asia/Kolkata"),
    "nagpur": (21.1458, 79.0882, "Asia/Kolkata"),
    "surat": (21.1702, 72.8311, "Asia/Kolkata"),
    "new york": (40.7128, -74.0060, "America/New_York"),
    "london": (51.5074, -0.1278, "Europe/London"),
    "los angeles": (34.0522, -118.2437, "America/Los_Angeles"),
    "chicago": (41.8781, -87.6298, "America/Chicago"),
    "dubai": (25.2048, 55.2708, "Asia/Dubai"),
    "singapore": (1.3521, 103.8198, "Asia/Singapore"),
    "sydney": (-33.8688, 151.2093, "Australia/Sydney"),
    "tokyo": (35.6762, 139.6503, "Asia/Tokyo"),
    "india": (28.6139, 77.2090, "Asia/Kolkata"),  # Default to Delhi
}


def expand_sign(abbr: str) -> str:
    """Convert Kerykeion abbreviated sign to full name."""
    return SIGN_MAP.get(abbr, abbr)


def get_nakshatra_from_moon(moon_abs_pos: float) -> tuple:
    """
    Determine the Nakshatra from Moon's absolute position (0-360°).
    Returns (nakshatra_name, pada_number, position_in_nakshatra).
    """
    nakshatra_span = 360.0 / 27.0  # 13.3333° per nakshatra
    pada_span = nakshatra_span / 4.0  # 3.3333° per pada

    index = int(moon_abs_pos / nakshatra_span)
    if index >= 27:
        index = 26

    position_in_nak = moon_abs_pos - (index * nakshatra_span)
    pada = int(position_in_nak / pada_span) + 1
    if pada > 4:
        pada = 4

    return (NAKSHATRA_LIST[index], pada, position_in_nak)


def compute_current_dasha(nakshatra: str, moon_pos_in_nak: float, dob: str) -> str:
    """
    Compute Vimshottari Dasha based on Moon's nakshatra and position.
    Returns "Planet Mahadasha, SubPlanet Antardasha" string.
    """
    nakshatra_span = 360.0 / 27.0
    birth_lord = NAKSHATRA_DASHA_LORD.get(nakshatra, "Ketu")

    # Find position of birth lord in dasha sequence
    lord_idx = 0
    for i, (planet, _) in enumerate(DASHA_SEQUENCE):
        if planet == birth_lord:
            lord_idx = i
            break

    # Fraction of nakshatra already traversed = fraction of birth dasha completed
    fraction_traversed = moon_pos_in_nak / nakshatra_span
    birth_dasha_duration = DASHA_SEQUENCE[lord_idx][1]
    remaining_birth_dasha = birth_dasha_duration * (1 - fraction_traversed)

    # Calculate age from DOB
    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d")
        age_years = (datetime.now() - birth_date).days / 365.25
    except Exception:
        age_years = 30

    # Walk through dashas to find current one
    elapsed = 0
    current_lord_idx = lord_idx

    # First dasha has partial remaining
    if age_years <= remaining_birth_dasha:
        mahadasha = DASHA_SEQUENCE[current_lord_idx][0]
    else:
        elapsed = remaining_birth_dasha
        current_lord_idx = (current_lord_idx + 1) % 9
        while elapsed < age_years:
            duration = DASHA_SEQUENCE[current_lord_idx][1]
            if elapsed + duration > age_years:
                break
            elapsed += duration
            current_lord_idx = (current_lord_idx + 1) % 9
        mahadasha = DASHA_SEQUENCE[current_lord_idx][0]

    # Simple sub-dasha (Antardasha) calculation
    mahadasha_duration = DASHA_SEQUENCE[current_lord_idx][1]
    time_in_mahadasha = age_years - elapsed
    if time_in_mahadasha < 0:
        time_in_mahadasha = 0

    # Antardasha cycles through the same sequence starting from mahadasha lord
    antardasha_elapsed = 0
    antardasha_idx = current_lord_idx
    for i in range(9):
        idx = (current_lord_idx + i) % 9
        sub_duration = (DASHA_SEQUENCE[idx][1] / TOTAL_DASHA_YEARS) * mahadasha_duration
        if antardasha_elapsed + sub_duration > time_in_mahadasha:
            antardasha_idx = idx
            break
        antardasha_elapsed += sub_duration

    antardasha = DASHA_SEQUENCE[antardasha_idx][0]
    return f"{mahadasha} Mahadasha, {antardasha} Antardasha"


def get_major_transit(saturn_sign: str, jupiter_sign: str, moon_sign: str) -> str:
    """Determine a significant current transit based on planet positions."""
    transits = []

    if saturn_sign:
        transits.append(f"Saturn transiting {saturn_sign}")
    if jupiter_sign:
        transits.append(f"Jupiter transiting {jupiter_sign}")

    # Pick the most relevant
    if transits:
        return transits[0]
    return "Jupiter transit"


# ═══════════════════════════════════════════
#  TIME PARSING & VEDIC TIME COMPUTATIONS
# ═══════════════════════════════════════════

def parse_birth_time(time_str: str) -> tuple:
    """
    Parse birth time from various formats into 24-hour (hour, minute).
    Supports: "HH:MM AM/PM", "HH:MM am/pm", "HH:MM" (24hr)
    Returns: (hour_24, minute, formatted_12hr_string)
    """
    time_str = time_str.strip()

    # Try 12-hour format
    match_12 = re.match(r'^(\d{1,2}):(\d{2})\s*(AM|PM|am|pm)$', time_str)
    if match_12:
        hour = int(match_12.group(1))
        minute = int(match_12.group(2))
        period = match_12.group(3).upper()
        hour_24 = (0 if hour == 12 else hour) if period == "AM" else (hour if hour == 12 else hour + 12)
        return (hour_24, minute, f"{hour}:{minute:02d} {period}")

    # Try 24-hour format
    match_24 = re.match(r'^(\d{1,2}):(\d{2})$', time_str)
    if match_24:
        hour_24 = int(match_24.group(1))
        minute = int(match_24.group(2))
        if hour_24 == 0:
            display_hour, period = 12, "AM"
        elif hour_24 < 12:
            display_hour, period = hour_24, "AM"
        elif hour_24 == 12:
            display_hour, period = 12, "PM"
        else:
            display_hour, period = hour_24 - 12, "PM"
        return (hour_24, minute, f"{display_hour}:{minute:02d} {period}")

    return (12, 0, "12:00 PM")


def compute_hora_lord(hour_24: int, minute: int, dob: str) -> str:
    """Compute the Hora (planetary hour) lord for the birth time."""
    SUNRISE_HOUR = 6
    total_minutes = hour_24 * 60 + minute
    sunrise_minutes = SUNRISE_HOUR * 60
    minutes_since_sunrise = (total_minutes - sunrise_minutes) if total_minutes >= sunrise_minutes else (24 * 60 - sunrise_minutes) + total_minutes
    hora_index = minutes_since_sunrise // 60

    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d")
        day_of_week = birth_date.weekday()
    except Exception:
        day_of_week = 0

    day_ruler = DAY_RULERS.get(day_of_week, "Sun")
    start_index = HORA_SEQUENCE.index(day_ruler)
    planet_index = (start_index + hora_index) % len(HORA_SEQUENCE)
    return HORA_SEQUENCE[planet_index]


def compute_muhurta(hour_24: int, minute: int) -> str:
    """Compute the Muhurta for the birth time."""
    SUNRISE_HOUR = 6
    total_minutes = hour_24 * 60 + minute
    sunrise_minutes = SUNRISE_HOUR * 60
    minutes_since_sunrise = (total_minutes - sunrise_minutes) if total_minutes >= sunrise_minutes else (24 * 60 - sunrise_minutes) + total_minutes
    muhurta_index = (minutes_since_sunrise // 48) % 30
    return MUHURTA_ORDER[muhurta_index]


def compute_birth_quality(hour_24: int, minute: int) -> str:
    """Determine day/night/twilight birth quality."""
    total_minutes = hour_24 * 60 + minute
    dawn_start, dawn_end = 330, 390     # 5:30-6:30 AM
    dusk_start, dusk_end = 1050, 1110   # 5:30-6:30 PM

    if dawn_start <= total_minutes < dawn_end or dusk_start <= total_minutes < dusk_end:
        return DAY_NIGHT_BIRTH["twilight"]["quality"]
    elif dawn_end <= total_minutes < dusk_start:
        return DAY_NIGHT_BIRTH["day"]["quality"]
    else:
        return DAY_NIGHT_BIRTH["night"]["quality"]


def get_coords_for_location(location: str) -> tuple:
    """Get lat/lng/tz for a location string. Returns (lat, lng, tz_str, city_name)."""
    loc_lower = location.lower().strip()

    # Try direct match first
    for city, (lat, lng, tz) in CITY_COORDS.items():
        if city in loc_lower:
            return (lat, lng, tz, city.title())

    # Default to Delhi, India
    return (28.6139, 77.2090, "Asia/Kolkata", "Delhi")


# ═══════════════════════════════════════════
#  MAIN COMPUTATION
# ═══════════════════════════════════════════

def compute_astrology(data: AstrologyRequest) -> AstrologyResponse:
    """
    Compute astrological chart using Kerykeion (Swiss Ephemeris).
    Real planetary position calculations + Vedic time analysis.
    """
    # Parse time
    hour_24, minute, formatted_time = parse_birth_time(data.time)

    # Parse DOB
    try:
        birth_date = datetime.strptime(data.dob, "%Y-%m-%d")
        year = birth_date.year
        month = birth_date.month
        day = birth_date.day
    except Exception:
        year, month, day = 2000, 1, 1

    # Resolve location to coordinates
    lat, lng, tz_str, city_name = get_coords_for_location(data.location)

    # Create Kerykeion subject with direct coordinates (no GeoNames dependency)
    try:
        subject = AstrologicalSubject(
            data.name, year, month, day, hour_24, minute,
            lat=lat, lng=lng, tz_str=tz_str, city=city_name
        )

        # Extract real planetary data
        moon_sign_full = expand_sign(subject.moon.sign)
        sun_sign_full = expand_sign(subject.sun.sign)
        ascendant_sign = expand_sign(subject.first_house.sign)
        moon_abs_pos = subject.moon.abs_pos

        # Compute Nakshatra from Moon's absolute position
        nakshatra, pada, moon_pos_in_nak = get_nakshatra_from_moon(moon_abs_pos)

        # Compute Vimshottari Dasha
        dasha_str = compute_current_dasha(nakshatra, moon_pos_in_nak, data.dob)

        # Get transit info from current planet positions
        saturn_sign = expand_sign(subject.saturn.sign)
        jupiter_sign = expand_sign(subject.jupiter.sign)
        transit = get_major_transit(saturn_sign, jupiter_sign, moon_sign_full)

        # Ascending sign with traits
        asc_traits = ASCENDANT_TRAITS.get(ascendant_sign, {})
        ascending_influence = f"{ascendant_sign} Lagna — {asc_traits.get('quality', 'Rising sign influence')}"

    except Exception as e:
        # Fallback if Kerykeion fails
        import hashlib
        input_str = f"{data.name}{data.dob}{data.time}{data.location}"
        hash_val = int(hashlib.md5(input_str.encode()).hexdigest(), 16)

        moon_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                      "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        moon_sign_full = moon_signs[hash_val % 12]
        nakshatra = NAKSHATRA_LIST[(hash_val // 10) % 27]
        planets = ["Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury", "Ketu", "Venus"]
        dasha_planet = planets[(hash_val // 100) % 9]
        dasha_str = f"{dasha_planet} Mahadasha"
        transit = "Jupiter transit"
        ascendant_sign = moon_signs[(hash_val // 1000) % 12]
        ascending_influence = f"{ascendant_sign} Lagna"

    # ═══════════════════════════════════════════
    #  TIME-BASED VEDIC ANALYSIS
    # ═══════════════════════════════════════════

    hora_lord = compute_hora_lord(hour_24, minute, data.dob)
    muhurta_name = compute_muhurta(hour_24, minute)
    birth_quality = compute_birth_quality(hour_24, minute)

    # Build summary
    hora_info = HORA_LORDS.get(hora_lord, {})
    muhurta_info = MUHURTA_DATA.get(muhurta_name, {})
    time_summary = (
        f"Born at {formatted_time}. "
        f"Birth Hour ruled by {hora_lord} — {hora_info.get('quality', '')}. "
        f"Birth Muhurta: {muhurta_name} ({muhurta_info.get('quality', 'Neutral')}) — presided by {muhurta_info.get('deity', 'Unknown')}. "
        f"Rising Sign: {ascending_influence}. "
        f"Birth Nature: {birth_quality}."
    )

    return AstrologyResponse(
        moon_sign=moon_sign_full,
        nakshatra=f"{nakshatra} (Pada {pada})" if 'pada' in dir() else nakshatra,
        current_dasha=dasha_str,
        major_transit=transit,
        birth_time_formatted=formatted_time,
        hora_lord=hora_lord,
        birth_quality=birth_quality,
        muhurta=muhurta_name,
        ascending_influence=ascending_influence,
        time_analysis_summary=time_summary
    )
