# Voice Detection Dataset – Team A

## Contributor
**Prince Dubey**  
Role: Data Collection & Labeling

## Overview
This contribution provides the **dataset preparation layer** for a Human vs AI voice detection system.  
Raw audio files are **not stored in this repository** to follow GitHub best practices.

The repo contains:
- Dataset metadata
- Preprocessing scripts for feature extraction

## Dataset Summary
**Classes:** Human, AI  
**Languages:** English, Hindi, Tamil, Telugu, Malayalam  
**Audio type:** Short speech clips (WAV / MP3)

## Metadata
File: `metadata.csv`

Contains:
- `filename`
- `language`
- `label` (human / ai)
- `source`

This file is used as input for preprocessing and training.

## Preprocessing Scripts
- `scripts/generate_metadata.py`  
  → Generates `metadata.csv` from dataset folders

- `scripts/extract_features.py`  
  → Extracts MFCC features and produces:
  - `X_mfcc.npy`
  - `y_labels.npy`

## Dataset Access
📥 **Download full dataset here:**  
👉 **[https://drive.google.com/drive/folders/1Gs9y63qPlBd93RyMEpj7V3F50bKmC7b3?usp=sharing]**

After download, place the extracted folder as:

Team B – Audio Preprocessing & Feature Pipeline Role

Team B is responsible for building a robust audio preprocessing and feature extraction pipeline that converts raw audio input into a fixed-size numerical feature vector for machine-learning models and APIs.

This module is the bridge between audio data and model inference.

Responsibilities

Decode Base64 audio input (MP3 / WAV)

Normalize audio (mono, fixed sample rate)

Handle empty, silent, or corrupted audio safely

Extract numerical audio features

Guarantee fixed-size output

Ensure downstream components (model / API) never crash

Pipeline Flow
Base64 Audio
   ↓
Decode & Normalize
   ↓
Safety Checks
   ↓
Feature Extraction
   ↓
Fixed-size Feature Vector (128)

Folder Structure
audio_pipeline/
├── __init__.py
├── preprocessing.py   # Base64 decoding & audio normalization
├── features.py        # Feature extraction logic
└── pipeline.py        # End-to-end pipeline entry point

Main Entry Point
pipeline_from_base64
from audio_pipeline.pipeline import pipeline_from_base64

features = pipeline_from_base64(audio_base64)


Input

Base64-encoded audio (MP3 / WAV)

Output

numpy.ndarray of shape (128,)

The function always returns a valid vector, even if the audio input is invalid.

Safety Design

The pipeline includes multiple defensive guards:

If audio decoding fails → returns zero vector

If audio is empty or silent → returns zero vector

If feature extraction fails → returns zero vector

If feature shape is incorrect → auto-pads or trims

This guarantees:

Stable model training

Stable inference

Stable API behavior

Feature Extraction

MFCC-based statistical features

Variable-length audio aggregated using mean and standard deviation

Output padded or trimmed to 128 dimensions

Compatible with:

SVM

XGBoost

MLP

Logistic Regression

Usage by Other Teams
Team C (Model Training)

Uses this pipeline to convert training audio into features

Receives consistent (128,) feature vectors

Team D (API & Deployment)

Uses the same pipeline for live inference

No extra error handling required at API level


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

