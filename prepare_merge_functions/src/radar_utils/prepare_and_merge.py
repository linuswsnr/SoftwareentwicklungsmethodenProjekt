

from __future__ import annotations

import glob
import os
from typing import Dict, List, Optional

import pandas as pd

__all__ = [
    "prepare_sequence_data",
    "merge_label_ids",
]

###############################################################################
# 1) Mapping: Roh‑IDs → Meta‑IDs (nur IDs aus dem Ticket explizit zuordnen)
###############################################################################
_RAW2META: Dict[int, int] = {
    0: 20, 1: 20,        # CAR
    5: 21, 6: 21,        # TWO_WHEELER
    7: 22, 8: 22,        # PEDESTRIAN
    11: 23,              # INFRASTRUCTURE
    # alle übrigen IDs implicit → 30 (OTHER)
}

###############################################################################
# 2) Mapping: Meta‑ID → Klassenname
###############################################################################
_META2NAME: Dict[int, str] = {
    20: "CAR",
    21: "TWO_WHEELER",
    22: "PEDESTRIAN",
    23: "INFRASTRUCTURE",
    30: "OTHER",
}

###############################################################################
# Funktion: Pickle‑Dateien einlesen und DataFrame zurückgeben
###############################################################################

def prepare_sequence_data(
    pickle_dir: str,
    drop_features: Optional[List[str]] = None,
    label_column: str = "label_id",
) -> pd.DataFrame:
    """Lädt alle *.pkl-Dateien und reduziert *label_id* auf 5 Klassen."""
    frames: list[pd.DataFrame] = []

    for path in glob.glob(os.path.join(pickle_dir, "*.pkl")):
        df = pd.read_pickle(path)
        df = df.dropna()
        frames.append(df)

    if not frames:
        raise FileNotFoundError(
            f"Keine Pickle-Dateien im Verzeichnis gefunden: {pickle_dir}")

    combined = pd.concat(frames, ignore_index=True)
    combined = merge_label_ids(combined, label_column=label_column)

    if drop_features:
        cols_to_drop = [c for c in drop_features if c in combined.columns]
        combined = combined.drop(columns=cols_to_drop)

    return combined

###############################################################################
# Funktion: Label‑IDs zusammenführen
###############################################################################

def merge_label_ids(
    df: pd.DataFrame,
    label_column: str = "label_id",
) -> pd.DataFrame:
    """Reduziert *label_id* auf fünf Zielklassen laut Mapping oben."""
    df_copy = df.copy()

    def to_meta(x):
        try:
            return _RAW2META.get(int(x), 30)  # unbekannt = 30 → OTHER
        except (ValueError, TypeError):
            return 30

    df_copy[label_column] = df_copy[label_column].apply(to_meta)
    df_copy[label_column] = df_copy[label_column].map(_META2NAME)

    return df_copy

###############################################################################
# Beispielaufruf (für schnelles Testen) ---------------------------------------
# if __name__ == "__main__":
#     df = prepare_sequence_data("./pickle_dir")
#     print(df["label_id"].value_counts())
