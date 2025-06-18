from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from typing import List
import tempfile
import os

from backend.utils.anomalies import detect_anomalies  # You must create this
from backend.models.schemas import AnalysisResult     # You must create this

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResult)
async def analyze_pcap(file: UploadFile = File(...)):
    if not file.filename.endswith(".pcap"):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload a .pcap file.")

    try:
        # Save uploaded file to a temp location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pcap") as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name

        # Process with your anomaly detection logic
        results = await detect_anomalies(tmp_path)

        # Clean up temp file
        os.remove(tmp_path)

        return JSONResponse(content=results)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
