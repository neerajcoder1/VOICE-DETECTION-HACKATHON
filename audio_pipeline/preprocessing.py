"""
preprocessing.py
----------------
Audio decoding and normalization utilities.

Responsibilities:
- Base64 → audio
- MP3/WAV handling via ffmpeg
- Return numpy waveform + sample rate
"""

import base64
import io
import numpy as np
import librosa


def base64_to_audio(b64_audio: str, target_sr: int = 16000):
    """
    Decode base64 audio to mono waveform.

    Parameters
    ----------
    b64_audio : str
        Base64 encoded audio
    target_sr : int
        Target sample rate

    Returns
    -------
    audio : np.ndarray
        Mono audio waveform
    sr : int
        Sample rate
    """

    try:
        audio_bytes = base64.b64decode(b64_audio)
        audio_buffer = io.BytesIO(audio_bytes)

        audio, sr = librosa.load(
            audio_buffer,
            sr=target_sr,
            mono=True
        )

        if audio is None or len(audio) == 0:
            return np.array([]), target_sr

        return audio, sr

    except Exception:
        # Defensive fallback
        return np.array([]), target_sr
