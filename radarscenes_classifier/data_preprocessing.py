import os, glob
import pandas as pd
from typing import Optional, List


# Mapping: numerische Label-IDs -> Klassenname (vereinheitlichte Labels)
LABEL_MAPPING = {
    0: "CAR", 1: "CAR", 
    5: "TWO-WHEELER", 6: "TWO-WHEELER",
    7: "PEDESTRIAN", 8: "PEDESTRIAN",
    9: "INFRASTRUCTURE", 10: "INFRASTRUCTURE", 11: "INFRASTRUCTURE"
    # (Eventuell weitere IDs 2,3,4 als "CAR" etc. ergänzen, siehe RadarScenes-Doku)
}

def merge_label_ids(df: pd.DataFrame, merge_map: dict) -> pd.DataFrame:
    """Ersetzt label_id-Werte gemäß Mapping-Tabelle (merge_map) durch Klassen-Namen."""
    df = df.copy()
    df["label_id"] = df["label_id"].replace(merge_map)
    return df

def prepare_sequence_data(pickle_dir: str, remove_classes: Optional[List[int]] = None) -> pd.DataFrame:
    """
    Lädt alle .pkl-Dateien aus dem Verzeichnis und vereinigt sie in einem DataFrame.
    Optionale Parameter:
      - remove_classes: Liste von Label-IDs, die *ausgeschlossen* werden sollen.
    Return:
      - kombinierter DataFrame mit vereinheitlichten Labels (label_id als Klassenname).
    """
    frames = []
    for pkl_path in glob.glob(os.path.join(pickle_dir, "*.pkl")):
        df = pd.read_pickle(pkl_path)
        # Falls bestimmte Klassen ignoriert werden sollen:
        if remove_classes:
            df = df[~df["label_id"].isin(remove_classes)]
        df = df.dropna()  # Unvollständige Daten entfernen
        frames.append(df)
    if not frames:
        raise FileNotFoundError(f"⚠️ Keine Pickle-Dateien in {pickle_dir} gefunden.")
    combined = pd.concat(frames, ignore_index=True)
    # Label-IDs zu Klassenlabels mappen
    combined = merge_label_ids(combined, LABEL_MAPPING)
    return combined
