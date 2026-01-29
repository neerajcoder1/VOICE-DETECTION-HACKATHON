"""
pipeline.py
------------
Entry point for Member B audio processing.

Responsibility:
- Accept Base64 audio
- Decode + preprocess
- Extract features
- NEVER crash downstream (return safe fallback if audio is empty)

This file is used by:
- tests
- Member C (model training)
- Member D (API inference)
"""

import numpy as np

from audio_pipeline.preprocessing import base64_to_audio
from audio_pipeline.features import extract_features


FEATURE_DIM = 128  # 🔒 contract with downstream (model + API)


def pipeline_from_base64(b64_audio: str) -> np.ndarray:
    """
    Full audio → feature pipeline.

    Parameters
    ----------
    b64_audio : str
        Base64 encoded audio (MP3/WAV)

    Returns
    -------
    np.ndarray
        1D feature vector (fixed size, non-empty)
    """

    # ---------- STEP 1: Decode ----------
    try:
        audio, sr = base64_to_audio(b64_audio)
    except Exception:
        # Absolute safety: decoding must never crash
        return np.zeros(FEATURE_DIM, dtype=np.float32)

    # ---------- SAFETY GUARD 1 ----------
    if audio is None or not isinstance(audio, np.ndarray) or audio.size == 0:
        return np.zeros(FEATURE_DIM, dtype=np.float32)

    # ---------- STEP 2: Feature extraction ----------
    try:
        features = extract_features(audio, sr)
    except Exception:
        return np.zeros(FEATURE_DIM, dtype=np.float32)

    # ---------- SAFETY GUARD 2 ----------
    if features is None or not isinstance(features, np.ndarray) or features.size == 0:
        return np.zeros(FEATURE_DIM, dtype=np.float32)

    # ---------- SAFETY GUARD 3 (shape contract) ----------
    if features.ndim != 1:
        features = features.flatten()

    if features.shape[0] != FEATURE_DIM:
        fixed = np.zeros(FEATURE_DIM, dtype=np.float32)
        fixed[: min(FEATURE_DIM, features.shape[0])] = features[:FEATURE_DIM]
        return fixed

    return features.astype(np.float32)
