## Team - <img width="300" height="300" alt="ChatGPT Image Feb 4, 2026, 08_39_33 PM" src="https://github.com/user-attachments/assets/574bcdee-bb77-4c68-9684-45e161ef7309" />

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





## API Integration & Deployment (Member D)

### Contributor: Aryan Singh Thapa
### Role: API Integration, Authentication & Deployment

## Objective

Deploy a public, stable API endpoint for AI-Generated Voice Detection that can be used by the hackathon’s automated evaluation system.

The API accepts Base64-encoded audio input, performs inference, and returns a structured JSON response containing classification results.

## Final System Flow

User Audio (Base64)

        ↓
API Authentication (API Key)

        ↓
Audio Preprocessing (Team B)

        ↓
Model Inference (Team C)

        ↓
JSON Response


## Public API Endpoint

Method: POST

Endpoint: /predict

### Authentication

Requests must include a valid API key in the header:

x-api-key: DEV_KEY

### Request Format

The API accepts Base64-encoded MP3/WAV audio.

{

  "audio_base64": "<BASE64_ENCODED_AUDIO>"
  
}

### Response Format

The API returns a structured JSON response as required by the problem statement.

{

  "classification": "AI | Human",
  
  "confidence": 0.95,
  
  "explanation": "Human-readable explanation of the prediction"
  
}

## API Behavior & Validation

### The endpoint is designed to:

Validate authentication using the API key

Correctly parse and validate request data

Handle invalid or corrupted inputs gracefully

Return consistent JSON responses

Remain stable under multiple requests

## Deployment

Framework: FastAPI

Server: Uvicorn

Deployed as a public HTTPS endpoint

No audio files are stored permanently

Optimized for low latency and reliability during evaluation

## API Key Management

API key is configured using environment variables

Required for all prediction requests

Used by the automated evaluation system for authentication

## Evaluation Readiness

This API meets all hackathon evaluation requirements:

Public and accessible endpoint

Stable request handling

Correct JSON response structure

Authentication enforced

Ready for automated testing with official audio samples

## Summary

This module delivers the final API layer of the project, enabling automated evaluation by exposing the AI voice detection system through a secure, production-ready endpoint.


## OUTPUT
![WhatsApp Image 2026-02-04 at 1 08 37 AM](https://github.com/user-attachments/assets/fec2a70d-2992-480d-ac6f-7cf3c4a3a72e)




