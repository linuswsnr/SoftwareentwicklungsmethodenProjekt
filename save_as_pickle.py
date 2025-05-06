import os
import h5py
import pandas as pd
from tqdm import tqdm

# Verzeichnisse definieren
script_dir = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(script_dir, "dataset", "RadarScenes", "data")
output_path = os.path.join(script_dir, "dataset", "RadarScenes_pickles")

# Zielordner erstellen, falls nicht vorhanden
os.makedirs(output_path, exist_ok=True)

# Nur die ersten 5 Sequenzen laden
sequence_dirs = sorted(
    [d for d in os.listdir(base_path) if d.startswith("sequence_")],
    key=lambda x: int(x.split("_")[1])
)[:10]

for seq in tqdm(sequence_dirs, desc="Verarbeite Sequenzen"):
    seq_path = os.path.join(base_path, seq)
    h5_file_path = os.path.join(seq_path, "radar_data.h5")

    if not os.path.exists(h5_file_path):
        print(f"Datei fehlt: {h5_file_path}")
        continue

    with h5py.File(h5_file_path, "r") as f:
        radar_data = f["radar_data"]
        data_dict = {name: radar_data[name] for name in radar_data.dtype.names}
        df = pd.DataFrame(data_dict)
        df["sequence"] = seq

    # Dateiname: DataSeq_1.pkl, DataSeq_2.pkl, ...
    seq_number = seq.split("_")[1]
    output_filename = f"DataSeq_{seq_number}.pkl"
    output_filepath = os.path.join(output_path, output_filename)

    df.to_pickle(output_filepath)

print("Alle Pickle-Dateien wurden erstellt.")
