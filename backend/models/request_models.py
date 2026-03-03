from pydantic import BaseModel, Field
from typing import Optional, List

class AstrologyRequest(BaseModel):
    name: str = Field(..., description="Name of the user")
    dob: str = Field(..., description="Date of birth in YYYY-MM-DD format")
    time: str = Field(..., description="Time of birth in HH:MM AM/PM format (12-hour) or HH:MM format (24-hour)")
    location: str = Field(..., description="City and Country")

class ChatMessage(BaseModel):
    role: str = Field(..., description="'user' or 'assistant'")
    content: str = Field(..., description="Message content")

class ChatRequest(BaseModel):
    astro_data: dict = Field(..., description="Astrology data from compute-chart")
    question: str = Field(..., description="User's question")
    history: Optional[List[ChatMessage]] = Field(default=None, description="Conversation history for multi-turn context")

class SaveSessionRequest(BaseModel):
    user_input: str
    ai_response: str
