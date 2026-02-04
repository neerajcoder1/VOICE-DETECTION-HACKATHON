# Voice Detection Dataset – Member A

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




---

## Sample Audio Files (Reference Only)

These samples are provided only for **quick reference and verification**.  
They are **not included in the repository**.

### Hindi – AI Voice Sample
- **Type:** AI-generated  
- **Language:** Hindi  
👉 https://drive.google.com/file/d/1ppn6uWGaKKnin0lPwVt0eYlsCZwPU0dK/view?usp=sharing

### Hindi – Human Voice Sample
- **Type:** Human  
- **Language:** Hindi  
👉 https://drive.google.com/file/d/1CNCr6iWdyMpCURWMwz5puKjOydIyiWv4/view?usp=sharing

These samples help reviewers understand the difference between AI-generated and human speech used in the dataset.



## ( Member B)
## Contributor -
**Neeraj Gahlout**  
Role: Team B is responsible for building a robust audio preprocessing and feature extraction pipeline that converts raw audio input into a fixed-size numerical feature vector for machine-learning models and APIs.
This module is the bridge between audio data and model inference.
## Pipeline Flow
-`Base64 Audio`
   
-`Decode & Normalize`
   
-`Safety Checks`
   
-`Feature Extraction`
   
-`Fixed-size Feature Vector (128)`

## Folder Structure
`audio_pipeline/`
`├── __init__.py`
`├── preprocessing.py`
`├── features.py`
`└── pipeline.py`

## Summary

`Team B delivers a fault-tolerant, production-ready audio feature pipeline that ensures system stability across training, inference, and deployment.
This module is a core dependency and should not be modified without coordination.`


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





API & Deployment (Member D)
Contributor

Aryan Singh Thapa
Role: API Integration, Authentication & Deployment




Overview

This contribution provides the production-ready API layer and deployment setup for the AI vs Human Voice Detection system.

The API acts as the final integration point, connecting:

Team B’s audio preprocessing pipeline

Team C’s model inference logic and exposing them through a secure, public REST API suitable for automated evaluation.



Responsibilities

Build FastAPI-based inference endpoint

Handle audio input (Base64-encoded MP3/WAV)

Manage authentication using API keys

Integrate preprocessing and model inference

Deploy and maintain a stable public endpoint



API Flow (End-to-End):-

Client Request (Base64 Audio)
        ↓
API Authentication (x-api-key)
        ↓
Team B Audio Pipeline (decode + safety checks)
        ↓
Temporary WAV conversion
        ↓
Team C Model Inference
        ↓
Structured JSON Response




Public API Endpoint

Method: POST
Endpoint:
/predict

Authentication Header:

x-api-key: DEV_KEY





Request Format
{
  "audio_base64": "<BASE64_ENCODED_AUDIO>"
}

Audio may be MP3 or WAV
Base64 string must not contain line breaks




Response Format:

{
  "classification": "AI | Human",
  "confidence": 0.95,
  "explanation": "Human-readable explanation of the prediction"
}



Error Handling

The API is designed to be fault-tolerant:

Invalid or corrupted audio → safe fallback response

Authentication failures → HTTP 401

Internal errors → HTTP 500 with descriptive message

The service never crashes on malformed input.



Deployment

Platform: Cloud-based web service

Framework: FastAPI

Server: Uvicorn

Public HTTPS endpoint provided for evaluation

No audio files are stored permanently

The service is configured to remain accessible during automated evaluation.



API Key Management

Authentication is enforced via a static API key

API key is configured through environment variables

Example (local / evaluation):

API_KEY=DEV_KEY




Notes for Evaluators

Endpoint is live and publicly accessible

Supports automated testing workflows

Complies with hackathon evaluation requirements

Designed for low-latency, stable inference




Summary

Member D delivers a secure, stable, and evaluation-ready API layer that exposes the full AI voice detection pipeline as a production-grade service. This module finalizes the system and enables automated testing and scoring.



