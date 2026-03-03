from pydantic import BaseModel
from typing import Optional

class AstrologyResponse(BaseModel):
    moon_sign: str
    nakshatra: str
    current_dasha: str
    major_transit: str
    # Time analysis fields
    birth_time_formatted: str = ""
    hora_lord: str = ""
    birth_quality: str = ""
    muhurta: str = ""
    ascending_influence: str = ""
    time_analysis_summary: str = ""

class ChatResponse(BaseModel):
    reply: str
