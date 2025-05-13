import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
import joblib

# Modell & Encoder laden
model = joblib.load("models/model_lightgbm.pkl")
le = joblib.load("models/label_encoder.pkl")

# Mapping wie im Training
id_to_class = {
    0: "CAR", 1: "CAR", 2: "CAR", 3: "CAR", 4: "CAR",
    5: "TWO-WHEELER", 6: "TWO-WHEELER",
    7: "PEDESTRIAN", 8: "PEDESTRIAN",
    9: "INFRASTRUCTURE", 10: "INFRASTRUCTURE", 11: "INFRASTRUCTURE"
}

# Testsequenzen 6–10 laden
dfs = []
for i in range(6, 11):
    path = f"dataset/RadarScenes_pickles/DataSeq_{i}.pkl"
    dfs.append(pd.read_pickle(path))

df_test = pd.concat(dfs, ignore_index=True)

# Vorverarbeitung
df_test = df_test[df_test["label_id"].isin(id_to_class.keys())]
df_test = df_test.drop(columns=["timestamp", "uuid", "track_id", "sequence"], errors="ignore")
df_test = df_test.dropna()
df_test["label_name"] = df_test["label_id"].map(id_to_class)

# Auf bekannte Klassen filtern
df_test = df_test[df_test["label_name"].isin(le.classes_)]

X_test = df_test.drop(columns=["label_id", "label_name"]).values
y_test = df_test["label_name"].values
y_test_encoded = le.transform(y_test)

# Vorhersage & Evaluation
y_pred = model.predict(X_test)
print("Testergebnisse auf Sequenzen 6–10:")
print(classification_report(y_test_encoded, y_pred, target_names=le.classes_))
