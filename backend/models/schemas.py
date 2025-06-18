from pydantic import BaseModel
from typing import List, Dict, Any

class Anomaly(BaseModel):
    type: str
    severity: str
    explanation: str
    context: Dict[str, Any]
    suggestion: str = None

class AnalysisResult(BaseModel):
    summary: str
    anomalies: List[Anomaly]

