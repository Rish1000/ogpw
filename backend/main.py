from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import analyze  # Make sure backend/analyze.py exists and has `router = APIRouter()`

app = FastAPI(
    title="OGPW Packet Analyzer API",
    description="Backend API for analyzing PCAP files and returning structured results.",
    version="1.0.0"
)

# CORS configuration to allow frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace with actual frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route inclusion from analyze.py
app.include_router(analyze.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "OGPW backend is up and running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
