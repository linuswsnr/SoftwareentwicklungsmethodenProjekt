import os
import pickle
import random
import joblib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


SEQUENCE_NUM = 2  # Sequenznummer aus der eine Punktewolke klassifiziert wird
SEQUENCE_NAME = f"sequence_{SEQUENCE_NUM}"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PKL_PATH = os.path.join(BASE_DIR, "..", "dataset", "radar_scenes_pickles", f"DataSeq_{SEQUENCE_NUM}.pkl")
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "model_lightgbm.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "..","models", "label_encoder.pkl")
CAMERA_IMG_DIR = os.path.join(BASE_DIR, "..","dataset", "radar_scenes", "data", f"sequence_{SEQUENCE_NUM}", "camera")
RESULTS_DIR = os.path.join(BASE_DIR, "..","results")
os.makedirs(RESULTS_DIR, exist_ok=True)


with open(PKL_PATH, "rb") as f:
    df = pickle.load(f)

# Modell & Label-Encoder laden
model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)

# Zufälligen Timestamp wählen
unique_timestamps = df["timestamp"].unique()
chosen_timestamp = random.choice(unique_timestamps)

# Alle Radarpunkte dieses Timestamps auswählen
points = df[df["timestamp"] == chosen_timestamp].copy()

# Features vorbereiten (analog zur Modell-Trainingslogik in train_model())
X = points.drop(columns=["sequence", "track_id", "uuid", "timestamp", "label_id"], errors="ignore")
X = X.select_dtypes(include=["number"])


# Radarpunkte klassifizieren
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

# Gemeinsamer Plot für klassifizierte Punktewolke + RGB Bild
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# === Radarpunktwolke ===
for label in np.unique(preds):
    subset = points[points["predicted_label"] == label]
    axs[0].scatter(subset["x_cc"], subset["y_cc"],
                   label=label,
                   color=label_colors.get(label, "black"),
                   alpha=0.7,
                   s=10)
axs[0].set_xlabel("x [m], tangential zum Fahrzeug")
axs[0].set_ylabel("y [m], lateral zum Fahrzeug")
axs[0].legend()
axs[0].set_title(f"Radar-Klassifikation @ Timestamp: {chosen_timestamp}")
axs[0].grid(True)

# Funktion, die das Kamerabild mit dem zeitlich nächstgelegenen 
# Timestamp zum gegebenen Timestamp findet
def find_closest_image(timestamp, image_dir):
    image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
    image_timestamps = [int(f.replace(".jpg", "")) for f in image_files]
    closest_ts = min(image_timestamps, key=lambda x: abs(x - timestamp))
    return os.path.join(image_dir, f"{closest_ts}.jpg")


closest_img_path = find_closest_image(chosen_timestamp, CAMERA_IMG_DIR)

# === Kamera-Bild ===
try:
    img = mpimg.imread(closest_img_path)
    axs[1].imshow(img)
    axs[1].axis('off')
    axs[1].set_title("RGB-Kamerabild")
except Exception as e:
    print(f"Kamerabild konnte nicht geladen werden: {e}")
    axs[1].text(0.5, 0.5, "Kein Bild verfügbar",
                ha='center', va='center', fontsize=12)
    axs[1].axis('off')

plt.suptitle("Radarpunkt-Klassifikation + Kameraansicht", fontsize=14)
plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.savefig(os.path.join(RESULTS_DIR, "combined_radar_camera_plot.png"))
plt.show()
