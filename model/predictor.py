from transformers import pipeline

voice_authenticator = None  # lazy-loaded


def load_model():
    global voice_authenticator
    if voice_authenticator is None:
        voice_authenticator = pipeline(
            "audio-classification", model="MelodyMachine/Deepfake-audio-detection-V2"
        )


def predict_explain(audio_path: str) -> dict:

    load_model()

    """
    Detect whether a voice sample is AI-generated or human.

    Args:
        audio_path (str): Path to preprocessed WAV audio file (16kHz, mono)

    Returns:
        dict: {
            "classification": "fake" | "real",
            "confidence": float,
            "explanation": str
        }
    """
    outputs = voice_authenticator(audio_path)
    top = max(outputs, key=lambda x: x["score"])

    label = top["label"]
    score = float(top["score"])

    if label == "fake":
        if score > 0.9:
            explanation = "High confidence synthetic (AI-generated) voice."
        elif score > 0.6:
            explanation = "Moderate likelihood of AI-generated voice."
        else:
            explanation = "Weak synthetic signal detected."
    else:
        if score > 0.9:
            explanation = "High confidence natural human voice."
        elif score > 0.6:
            explanation = "Likely a real human voice."
        else:
            explanation = "Uncertain, but leans toward human voice."

    return {"classification": label, "confidence": score, "explanation": explanation}
