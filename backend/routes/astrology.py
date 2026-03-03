from fastapi import APIRouter, HTTPException
from models.request_models import AstrologyRequest
from models.response_models import AstrologyResponse
from services.astrology_engine import compute_astrology

router = APIRouter()

@router.post("/compute-chart", response_model=AstrologyResponse)
async def compute_chart(request: AstrologyRequest):
    try:
        # Validate inputs roughly
        if not request.name or len(request.name) < 2:
            raise ValueError("Name is too short")
        if not request.dob:
            raise ValueError("Date of birth is required")
            
        result = compute_astrology(request)
        return result
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error while computing astrology")
