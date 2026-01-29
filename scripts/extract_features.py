import os
import numpy as np
import pandas as pd
import librosa

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
DATASET_DIR = os.path.join(PROJECT_ROOT, "dataset")
METADATA_PATH = os.path.join(PROJECT_ROOT, "metadata.csv")

X_OUTPUT = os.path.join(PROJECT_ROOT, "X_mfcc.npy")
Y_OUTPUT = os.path.join(PROJECT_ROOT, "y_labels.npy")

SAMPLE_RATE = 16000
N_MFCC = 13

df = pd.read_csv(METADATA_PATH)

features = []
labels = []

for _, row in df.iterrows():
    audio_path = os.path.join(
        DATASET_DIR,
        row["label"],
        row["language"],
        row["filename"]
    )

    if not os.path.exists(audio_path):
        continue

    audio, sr = librosa.load(audio_path, sr=SAMPLE_RATE)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=N_MFCC)
    mfcc_mean = np.mean(mfcc, axis=1)

    features.append(mfcc_mean)
    labels.append(0 if row["label"] == "human" else 1)

X = np.array(features)
y = np.array(labels)

np.save(X_OUTPUT, X)
np.save(Y_OUTPUT, y)

print("✅ Feature extraction complete")
print("X shape:", X.shape)
print("y shape:", y.shape)
