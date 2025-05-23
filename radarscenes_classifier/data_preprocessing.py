import os, glob
import pandas as pd
from typing import Optional, List


# Mapping: numerische Label-IDs -> Klassenname (vereinheitlichte Labels)
BASIS_LABEL_MAPPING = {
    0: "CAR", 1: "CAR", 2: "CAR", 3: "CAR", 4: "CAR",
    5: "TWO-WHEELER", 6: "TWO-WHEELER",
    7: "PEDESTRIAN", 8: "PEDESTRIAN",
    9: "INFRASTRUCTURE", 10: "INFRASTRUCTURE", 11: "INFRASTRUCTURE"
}

def merge_label_ids(df: pd.DataFrame, merge_map: Optional[dict] = None) -> pd.DataFrame:
    """
    Ersetzt label_id-Werte gemäß Mapping-Tabelle (merge_map) durch Klassen-Namen.
    Wenn kein Mapping übergeben wird, wird das Standard-LABEL_MAPPING genutzt.
    """
    df = df.copy()

    if merge_map is None:
        merge_map = BASIS_LABEL_MAPPING
        df["label_id"] = df["label_id"].replace(merge_map)
    else:
        # Beispiel: {"VEHICLE": ["CAR", "TRUCK"]} → {"CAR": "VEHICLE", "TRUCK": "VEHICLE"}
        reverse_map = {}
        for target, sources in merge_map.items():
            for source in sources:
                reverse_map[source] = target
        df["label_id"] = df["label_id"].replace(reverse_map)

    return df

def prepare_sequence_data(
    pickle_dir: str,
    remove_classes: Optional[List[int]] = None,
    limit_n_files: Optional[int] = None
) -> pd.DataFrame:
    """
    Lädt bis zu 'limit_n_files' .pkl-Dateien aus dem Verzeichnis und vereinigt sie in einem DataFrame.
    
    Parameter:
      - pickle_dir: Verzeichnis mit Pickle-Dateien
      - remove_classes: Liste von Label-IDs, die ausgeschlossen werden sollen
      - limit_n_files: Optional: Anzahl der zu ladenden Dateien begrenzen
    
    Rückgabe:
      - kombinierter DataFrame mit vereinheitlichten Labels
    """
    import glob

    pkl_paths = glob.glob(os.path.join(pickle_dir, "*.pkl"))
    if limit_n_files is not None:
        pkl_paths = pkl_paths[:limit_n_files]

    frames = []
    for pkl_path in pkl_paths:
        df = pd.read_pickle(pkl_path)
        if remove_classes:
            df = df[~df["label_id"].isin(remove_classes)]
        df = df.dropna()
        frames.append(df)

    if not frames:
        raise FileNotFoundError(f"Keine Pickle-Dateien in {pickle_dir} gefunden.")

    combined = pd.concat(frames, ignore_index=True)

    """
    # Beispiel für eine alternative Mapping-Tabelle
    LABEL_MAPPING =  {
    0: "CAR", 1: "CAR", 2: "CAR", 3: "CAR", 4: "CAR",
    5: "TWO-WHEELER", 6: "TWO-WHEELER",
    7: "PEDESTRIAN", 8: "PEDESTRIAN",
    9: "INFRASTRUCTURE", 10: "INFRASTRUCTURE", 11: "INFRASTRUCTURE"
    }
    """

    combined = merge_label_ids(combined) # <-- für Standard-Mapping, sonst merge_label_ids(combined, LABEL_MAPPING)
    return combined
