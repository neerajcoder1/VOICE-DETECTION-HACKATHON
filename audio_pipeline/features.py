"""
features.py
------------
Feature extraction logic (Member B).

Features used:
- MFCCs (robust, fast)
- Reduced to fixed-size vector

Design rules:
- No empty outputs
- Stable shape
- Model-safe
"""

import numpy as np
import librosa


def extract_features(audio: np.ndarray, sr: int) -> np.ndarray:
    """
    Extract fixed-length feature vector from audio.

    Parameters
    ----------
    audio : np.ndarray
        Mono audio signal
    sr : int
        Sample rate

    Returns
    -------
    np.ndarray
        1D feature vector (size = 128)
    """

    # ---------- SAFETY GUARD ----------
    if audio is None or len(audio) == 0:
        return np.zeros(128, dtype=np.float32)

    try:
        # Compute MFCCs
        mfcc = librosa.feature.mfcc(
            y=audio,
            sr=sr,
            n_mfcc=20
        )

        # mfcc shape: (n_mfcc, time)
        if mfcc.size == 0:
            return np.zeros(128, dtype=np.float32)

        # Statistical pooling (time axis)
        mfcc_mean = np.mean(mfcc, axis=1)
        mfcc_std = np.std(mfcc, axis=1)

        # Concatenate
        features = np.concatenate([mfcc_mean, mfcc_std])

        # Pad or trim to fixed size (128)
        if features.shape[0] < 128:
            features = np.pad(
                features,
                (0, 128 - features.shape[0]),
                mode="constant"
            )
        else:
            features = features[:128]

        return features.astype(np.float32)

    except Exception:
        # Absolute last-resort fallback
        return np.zeros(128, dtype=np.float32)
