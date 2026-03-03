from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import astrology, chat

app = FastAPI(title="Divyavani Backend", version="1.0.0")

# Setup CORS to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to the specific frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(astrology.router, tags=["Astrology"])
app.include_router(chat.router, tags=["Chat"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Divyavani API. The cosmos is ready."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
