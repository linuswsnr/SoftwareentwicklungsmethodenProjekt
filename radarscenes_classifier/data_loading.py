import os
import h5py
import pandas as pd
from tqdm import tqdm


def load_sequence_raw(seq_path: str) -> pd.DataFrame:
    """Lädt die Radar-Rohdaten einer Sequenz und gibt sie als DataFrame zurück."""
    h5_file = os.path.join(seq_path, "radar_data.h5")
    if not os.path.exists(h5_file):
        raise FileNotFoundError(f"Datei nicht gefunden: {h5_file}")
    # HDF5-Datei öffnen und Datensatz laden
    with h5py.File(h5_file, "r") as f:
        radar_data = f["radar_data"]  # strukturierter NumPy-Datensatz
        data_dict = {name: radar_data[name] for name in radar_data.dtype.names}
    df = pd.DataFrame(data_dict)
    df["sequence"] = os.path.basename(seq_path)  # Sequenz-ID als Spalte hinzufügen
    return df


def save_sequence_pickle(seq_path: str, output_dir: str) -> None:
    """Speichert die Daten einer Sequenz als Pickle-Datei im output_dir."""
    df = load_sequence_raw(seq_path)
    # Sequenznummer aus Ordnernamen extrahieren, z.B. "sequence_1" -> "1"
    seq_name = os.path.basename(seq_path)
    seq_number = seq_name.split("_")[1] if "_" in seq_name else seq_name
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"DataSeq_{seq_number}.pkl")
    df.to_pickle(output_path)
    # Optional: Logging
    print(f"Pickle gespeichert: {output_path}")


def generate_all_sequence_pickles(base_path: str, output_dir: str) -> None:
    """Erstellt Pickle-Dateien für alle Sequenzen unter base_path 
    im output_dir."""
    seq_dirs = sorted(d for d in os.listdir(base_path) 
                      if d.startswith("sequence_"))
    if not seq_dirs:
        raise FileNotFoundError(f"Keine Sequenzen in {base_path} gefunden.")
    for seq in tqdm(seq_dirs, desc="Sequenzen verarbeiten"):
        seq_path = os.path.join(base_path, seq)
        try:
            save_sequence_pickle(seq_path, output_dir)
        except FileNotFoundError as e:
            print(e)
    print("Alle Pickle-Dateien wurden erstellt in:", output_dir)
