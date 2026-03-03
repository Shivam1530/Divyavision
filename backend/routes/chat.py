from fastapi import APIRouter, HTTPException
from models.request_models import ChatRequest, SaveSessionRequest
from models.response_models import ChatResponse
from services.llm_service import generate_prediction
import json
import os

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        # Convert history to list of dicts for the LLM service
        history = None
        if request.history:
            history = [{"role": msg.role, "content": msg.content} for msg in request.history]
        
        reply = generate_prediction(request.astro_data, request.question, history=history)
        return ChatResponse(reply=reply)
    except Exception as e:
        print(f"Chat endpoint error: {e}")
        raise HTTPException(status_code=500, detail="Error generating insight")

@router.post("/save-session")
async def save_session(request: SaveSessionRequest):
    try:
        # Simple file-based storage for MVP
        session_file = "sessions.json"
        
        # In a real app, use a DB
        sessions = []
        if os.path.exists(session_file):
            try:
                with open(session_file, "r") as f:
                    sessions = json.load(f)
            except:
                sessions = []
                
        sessions.append({
            "question": request.user_input,
            "response": request.ai_response,
            "timestamp": "now" # Simplified for MVP
        })
        
        with open(session_file, "w") as f:
            json.dump(sessions, f)
            
        return {"status": "success"}
    except Exception as e:
        print(f"Failed to save session: {e}")
        return {"status": "error"}
