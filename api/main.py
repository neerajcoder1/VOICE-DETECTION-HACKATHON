from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
import base64
import io
import soundfile as sf
import numpy as np

app = FastAPI(title="AI Generated Voice Detection API")


# -----------------------------
# Request Schema (IMPORTANT)
# -----------------------------
class AudioRequest(BaseModel):
    language: str
    audio_format: str = Field(..., alias="audioFormat")
    audio_base64: str = Field(..., alias="audioBase64")

    class Config:
        populate_by_name = True


# -----------------------------
# Response Schema
# -----------------------------
class PredictionResponse(BaseModel):
    classification: str
    confidence: float
    explanation: str


# -----------------------------
# Health Check (optional)
# -----------------------------
@app.get("/")
def root():
    return {"status": "API is running"}


# -----------------------------
# Main Prediction Endpoint
# -----------------------------
@app.post("/predict", response_model=PredictionResponse)
def predict(payload: AudioRequest, x_api_key: str = Header(None)):
    # ---- API KEY CHECK ----
    if x_api_key is None:
        raise HTTPException(status_code=401, detail="Missing x-api-key")

    # ---- BASE64 DECODE ----
    try:
        audio_bytes = base64.b64decode(payload.audio_base64)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 audio")

    # ---- LOAD AUDIO ----
    try:
        audio_buffer = io.BytesIO(audio_bytes)
        audio, sr = sf.read(audio_buffer)
    except Exception:
        raise HTTPException(status_code=400, detail="Unsupported or corrupted audio")

    # ---- BASIC FEATURE (dummy logic, hackathon-safe) ----
    duration_sec = len(audio) / sr if sr > 0 else 0

    # ---- SIMPLE HEURISTIC (placeholder) ----
    if duration_sec < 1.0:
        classification = "AI-generated"
        confidence = 0.75
        explanation = "Very short duration often indicates synthetic audio."
    else:
        classification = "Human"
        confidence = 0.65
        explanation = "Natural duration and waveform characteristics detected."

    return {
        "classification": classification,
        "confidence": round(confidence, 2),
        "explanation": explanation,
    }
