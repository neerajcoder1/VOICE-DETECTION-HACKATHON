# Voice Detection Dataset – Team A

## Contributor
**Prince Dubey**  
Role: Data Collection & Labeling

---

## Overview
This contribution provides the **dataset preparation layer** for a Human vs AI voice detection system.  
Raw audio files are **not stored in this repository** to follow GitHub best practices.

The repo contains:
- Dataset metadata
- Preprocessing scripts for feature extraction

---

## Dataset Summary
**Classes:** Human, AI  
**Languages:** English, Hindi, Tamil, Telugu, Malayalam  
**Audio type:** Short speech clips (WAV / MP3)

---

## Metadata
File: `metadata.csv`

Contains:
- `filename`
- `language`
- `label` (human / ai)
- `source`

This file is used as input for preprocessing and training.

---

## Preprocessing Scripts
- `scripts/generate_metadata.py`  
  → Generates `metadata.csv` from dataset folders

- `scripts/extract_features.py`  
  → Extracts MFCC features and produces:
  - `X_mfcc.npy`
  - `y_labels.npy`

---

## Dataset Access
📥 **Download full dataset here:**  
👉 **[https://drive.google.com/drive/folders/1Gs9y63qPlBd93RyMEpj7V3F50bKmC7b3?usp=sharing]**

After download, place the extracted folder as:



## Model & Inference (Member C)

This module implements the core AI logic for detecting whether a voice sample is human-generated or AI-generated.

### Responsibilities
- Load a pretrained deepfake voice detection model
- Perform inference on preprocessed audio (16 kHz, mono WAV)
- Return structured results with:
  - classification (real / fake)
  - confidence score
  - human-readable explanation

### Interface
The model exposes a single function: predict_explain(audio_path: str) -> dict


Example output:

{
"classification": "fake",
"confidence": 0.99,
"explanation": "High confidence synthetic (AI-generated) voice."
}


This module is designed to be imported directly by the API layer after audio preprocessing.

