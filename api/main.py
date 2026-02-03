# api/main.py

import os
import base64
import uuid
import requests
from typing import Optional

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

from audio_pipeline.pipeline import pipeline_from_base64
from model.predictor import predict_explain

app = FastAPI(title="AI vs Human Voice Detection API")

# API key (Render will set this)
API_KEY = os.getenv("API_KEY", "DEV_KEY")

TEMP_DIR = "temp_audio"
os.makedirs(TEMP_DIR, exist_ok=True)


# -------- Request Schema (Tester-Compatible) --------
class PredictRequest(BaseModel):
    audio_base64: str

    # Tester metadata (ignored safely)
    language: Optional[str] = None
    audio_format: Optional[str] = None
    audio_base64_format: Optional[str] = None


# -------- Helpers --------
def base64_to_temp_wav(b64_audio: str) -> str:
    try:
        audio_bytes = base64.b64decode(b64_audio)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Base64 audio")

    file_id = str(uuid.uuid4())
    wav_path = os.path.join(TEMP_DIR, f"{file_id}.wav")

    with open(wav_path, "wb") as f:
        f.write(audio_bytes)

    return wav_path


# -------- Endpoint --------
@app.post("/predict")
def predict(
    request: PredictRequest,
    x_api_key: str = Header(None),
):
    # ---- AUTH (Tester uses x-api-key) ----
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    wav_path = None
    try:
        # ---- Team B preprocessing (Base64 → features, safety check) ----
        _ = pipeline_from_base64(request.audio_base64)

        # ---- Convert Base64 → WAV for Team C ----
        wav_path = base64_to_temp_wav(request.audio_base64)

        # ---- Team C inference ----
        result = predict_explain(wav_path)

        classification = "AI" if result["classification"] == "fake" else "Human"
        confidence = round(float(result["confidence"]), 3)
        explanation = result["explanation"]

        return {
            "classification": classification,
            "confidence": confidence,
            "explanation": explanation,
        }

    except HTTPException:
        raise

    except Exception:
        # Absolute safety fallback
        return {
            "classification": "Unknown",
            "confidence": 0.0,
            "explanation": "Invalid or corrupted audio input.",
        }

    finally:
        if wav_path and os.path.exists(wav_path):
            os.remove(wav_path)
