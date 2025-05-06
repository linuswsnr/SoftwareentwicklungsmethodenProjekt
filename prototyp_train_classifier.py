import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from lightgbm import LGBMClassifier
import joblib
import os

# Trainingssequenzen 1 bis 5 laden
dfs = []
for i in range(1, 6):
    path = f"dataset/RadarScenes_pickles/DataSeq_{i}.pkl"
    dfs.append(pd.read_pickle(path))

df = pd.concat(dfs, ignore_index=True)

# Mapping auf 4 Klassen
id_to_class = {
    0: "CAR", 1: "CAR", 2: "CAR", 3: "CAR", 4: "CAR",
    5: "TWO-WHEELER", 6: "TWO-WHEELER",
    7: "PEDESTRIAN", 8: "PEDESTRIAN",
    9: "INFRASTRUCTURE", 10: "INFRASTRUCTURE", 11: "INFRASTRUCTURE"
}

# Vorverarbeitung
df = df[df["label_id"].isin(id_to_class.keys())]
df = df.drop(columns=["timestamp", "uuid", "track_id", "sequence"], errors="ignore")
df = df.dropna()
df["label_name"] = df["label_id"].map(id_to_class)

X = df.drop(columns=["label_id", "label_name"]).values
y = df["label_name"].values

# Label-Encoding
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Modell trainieren
model = LGBMClassifier()
model.fit(X, y_encoded)

# Trainingsauswertung
y_pred = model.predict(X)
print("Trainingsdaten-Ergebnisse (Sequenzen 1–5):")
print(classification_report(y_encoded, y_pred, target_names=le.classes_))

# Speichern
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model_lightgbm.pkl")
joblib.dump(le, "models/label_encoder.pkl")
