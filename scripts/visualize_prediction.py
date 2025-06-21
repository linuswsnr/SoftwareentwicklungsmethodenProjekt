import os
import pickle
import random
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from PIL import Image


SEQUENCE_NUM = 1  # Sequenznummer aus der eine Punktewolke klassifiziert wird
SEQUENCE_NAME = f"sequence_{SEQUENCE_NUM}"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PKL_PATH = os.path.join(BASE_DIR, "..", "dataset", "radar_scenes_pickles", f"DataSeq_{SEQUENCE_NUM}.pkl")
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "model_lightgbm.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "..","models", "label_encoder.pkl")
CAMERA_IMG_DIR = os.path.join(BASE_DIR, "..","dataset", "radar_scenes", "data", f"sequence_{SEQUENCE_NUM}", "camera")
RESULTS_DIR = os.path.join(BASE_DIR, "..","results")
os.makedirs(RESULTS_DIR, exist_ok=True)


# Daten laden
with open(PKL_PATH, "rb") as f:
    df = pickle.load(f)

# Zufälligen Timestamp wählen
unique_timestamps = df["timestamp"].unique()
chosen_timestamp = random.choice(unique_timestamps)

# Alle Punkte mit diesem Timestamp
points = df[df["timestamp"] == chosen_timestamp].copy()

# Features vorbereiten (analog zur Modell-Trainingslogik in train_model())
X = points.drop(columns=["sequence", "track_id", "uuid", "timestamp", "label_id"], errors="ignore")
X = X.select_dtypes(include=["number"])

# Modell & Label-Encoder laden
model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)

# Vorhersage
preds_encoded = model.predict(X)
preds = label_encoder.inverse_transform(preds_encoded) # Integer -> Strings
points["predicted_label"] = preds

# Farben pro Klasse festlegen
label_colors = {
    "CAR": "blue",
    "TWO_WHEELER": "green",
    "PEDESTRIAN": "red",
    "TRUCK": "orange",
    "OTHER": "gray"
}

# Plotten
plt.figure(figsize=(8, 6))
for label in np.unique(preds):
    subset = points[points["predicted_label"] == label]
    plt.scatter(subset["x_cc"], subset["y_cc"], label=label, color=label_colors.get(label, "black"), alpha=0.7)
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.legend()
plt.title(f"Radarpunkt-Klassifikation für Timestamp {chosen_timestamp}")
plt.grid(True)
plt.savefig(os.path.join(RESULTS_DIR, "radar_classification_plot.png"))
plt.close()

# === Kamera-Bild laden, das dem Timestamp am nächsten ist ===
def find_closest_image(timestamp, image_dir):
    image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
    image_timestamps = [int(f.replace(".jpg", "")) for f in image_files]
    closest_ts = min(image_timestamps, key=lambda x: abs(x - timestamp))
    return os.path.join(image_dir, f"{closest_ts}.jpg")

try:
    closest_img_path = find_closest_image(chosen_timestamp, CAMERA_IMG_DIR)
    img = Image.open(closest_img_path)
    img.save(os.path.join(RESULTS_DIR, "camera_image.jpg"))
    print(f"Kamerabild gespeichert unter: {os.path.join(RESULTS_DIR, 'camera_image.jpg')}")
except Exception as e:
    print(f"Fehler beim Laden des Kamerabildes: {e}")
