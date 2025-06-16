# -*- coding: utf-8 -*-
"""
Schritte:
1. Alle .pkl-Dateien im Ordner finden
2. Spalte 'label_id' einlesen
3. Roh-IDs → Meta-IDs → Klassenname übersetzen
4. Gesamte Verteilung ausgeben
5. Stratified Split (80 % Train / 20 % Test)
6. Verteilung je Teilmenge ausgeben
7. Train- und Test-DataFrames als Pickle-Dateien sichern
"""

# -------------------------------------------------
# 0) Benötigte Bibliotheken
# -------------------------------------------------
import os
import glob
import pickle
from typing import Dict, List

import pandas as pd  # pandas
from sklearn.model_selection import train_test_split  # scikit-learn


# -------------------------------------------------
# 1) Ordnerpfad der Pickle-Dateien
# -------------------------------------------------
DIR = r"D:\dataset\RadarScenes_pickles"  # ggf. anpassen
pkl_files: List[str] = glob.glob(os.path.join(DIR, "*.pkl"))
print(f"{len(pkl_files)} Dateien gefunden.\n")


# -------------------------------------------------
# 2) Mapping: Roh-ID → Meta-ID  und  Meta-ID → Klassenname
# -------------------------------------------------
RAW2META: Dict[int, int] = {
    0: 20, 1: 20, 2: 20, 3: 20, 4: 20,  # CAR
    5: 21, 6: 21,                       # TWO_WHEELER
    7: 22, 8: 22,                       # PEDESTRIAN
    11: 23,                             # INFRASTRUCTURE
    # alle übrigen IDs → 30 (OTHER)
}

META2NAME: Dict[int, str] = {
    20: "CAR",
    21: "TWO_WHEELER",
    22: "PEDESTRIAN",
    23: "INFRASTRUCTURE",
    30: "OTHER",
}


def raw_to_class(raw_id: int) -> str:
    """Wandelt Roh-ID in endgültigen Klassennamen um."""
    meta_id = RAW2META.get(raw_id, 30)  # Standard = OTHER
    return META2NAME[meta_id]


# -------------------------------------------------
# 3) Alle Label aus allen Dateien sammeln
# -------------------------------------------------
labels: List[str] = []
problem_files: List[str] = []

for fp in pkl_files:
    with open(fp, "rb") as f:
        obj = pickle.load(f)

    # Erwartung: DataFrame mit Spalte 'label_id'
    if isinstance(obj, pd.DataFrame) and "label_id" in obj.columns:
        raw_ids = obj["label_id"].tolist()
        labels.extend(raw_to_class(x) for x in raw_ids)
    else:
        problem_files.append(fp)

if problem_files:
    print("⚠️  Dateien ohne 'label_id' oder unbekannte Struktur:")
    for fp in problem_files:
        print("   ", fp)
    print()


# -------------------------------------------------
# 4) Einspaltigen DataFrame aus Labels erstellen
# -------------------------------------------------
labels_df = pd.DataFrame({"label": labels})

print("📊 Gesamte Verteilung aller Labels:")
print(labels_df["label"].value_counts(), "\n")


# -------------------------------------------------
# 5) Stratified Split 80 % / 20 %
# -------------------------------------------------
train_df, test_df = train_test_split(
    labels_df,
    test_size=0.20,
    stratify=labels_df["label"],
    random_state=42,
)


# -------------------------------------------------
# 6) Verteilung in Train und Test ausgeben
# -------------------------------------------------
print("👟 Trainingsmenge:")
print(train_df["label"].value_counts(), "\n")

print("🧪 Testmenge:")
print(test_df["label"].value_counts(), "\n")


# -------------------------------------------------
# 7) DataFrames als Pickle-Dateien speichern
# -------------------------------------------------
TRAIN_OUT = r"D:\dataset\RadarScenes_pickles\train_labels.pkl"
TEST_OUT = r"D:\dataset\RadarScenes_pickles\test_labels.pkl"

train_df.to_pickle(TRAIN_OUT)
test_df.to_pickle(TEST_OUT)

print("✅  Dateien geschrieben:")
print("   ", TRAIN_OUT)
print("   ", TEST_OUT)
