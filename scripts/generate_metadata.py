import os
import csv

# project structure
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
DATASET_DIR = os.path.join(PROJECT_ROOT, "dataset")
METADATA_PATH = os.path.join(PROJECT_ROOT, "metadata.csv")

FIELDS = ["filename", "language", "label", "source"]

rows = []

for label in ["human", "ai"]:
    label_dir = os.path.join(DATASET_DIR, label)
    if not os.path.exists(label_dir):
        continue

    for language in os.listdir(label_dir):
        lang_dir = os.path.join(label_dir, language)
        if not os.path.isdir(lang_dir):
            continue

        for file in os.listdir(lang_dir):
            if file.endswith((".wav", ".mp3")):
                rows.append({
                    "filename": file,
                    "language": language,
                    "label": label,
                    "source": "commonvoice" if label == "human" else "tts"
                })

with open(METADATA_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ metadata.csv updated with {len(rows)} entries")
