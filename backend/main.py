from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import analyze  # Make sure analyze.py has `router = APIRouter()`

app = FastAPI(
    title="OGPW Packet Analyzer API",
    description="Backend API for analyzing PCAP files and returning structured results.",
    version="1.0.0"
)

# Allow frontend (e.g., Streamlit) to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, set this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes from analyze.py
app.include_router(analyze.router, prefix="/api")

# Optional: a health check route
@app.get("/")
def root():
    return {"message": "OGPW backend is up and running!"}

# Optional: enable direct running
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
