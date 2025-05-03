import os
import h5py
import pandas as pd
from tqdm import tqdm

# 🔧 Root-Pfad zum RadarScenes-Datensatz anpassen
base_path = "dataset/RadarScenes/data"

# 🔄 Alle Sequenzordner finden
sequence_dirs = sorted([d for d in os.listdir(base_path) if d.startswith("sequence_")])

all_data = []

for seq in tqdm(sequence_dirs, desc="Sequenzen laden"):
    seq_path = os.path.join(base_path, seq)
    h5_file_path = os.path.join(seq_path, "radar_data.h5")

    if not os.path.exists(h5_file_path):
        print(f"⚠️ Datei fehlt: {h5_file_path}")
        continue

    with h5py.File(h5_file_path, "r") as f:
        radar_data = f["radar_data"]
        data_dict = {name: radar_data[name] for name in radar_data.dtype.names}
        df = pd.DataFrame(data_dict)
        
        # 🏷️ Sequenz-ID hinzufügen
        df["sequence"] = seq
        
        all_data.append(df)

# 🧩 Alle Sequenzen zusammenführen
full_df = pd.concat(all_data, ignore_index=True)

# 💾 Optional speichern (Pickle ist am schnellsten)
full_df.to_pickle("radarscenes_all.pkl")
# Alternativ: full_df.to_csv("radarscenes_all.csv", index=False)

# ✅ Vorschau
print(full_df.head())
print("\n📐 Gesamtgröße:", full_df.shape)
print("\n🔣 Label-Verteilung:")
print(full_df["label_id"].value_counts())