from __future__ import annotations
import os
import glob
import pandas as pd
from typing import List, Dict


# Konstante Zuordnung von label_id zu Klassenbezeichnung
LABEL_MAPPING: Dict[int, str] = {
    0: "CAR", 1: "CAR", 2: "CAR", 3: "CAR", 4: "CAR",
    5: "TWO_WHEELER", 6: "TWO_WHEELER",
    7: "PEDESTRIAN", 8: "PEDESTRIAN",
    9: "INFRASTRUCTURE", 10: "INFRASTRUCTURE", 11: "INFRASTRUCTURE"
}


from typing import Optional

from typing import Optional

def prepare_sequence_data(
    pickle_dir: str,
    remove_classes: Optional[List[int]] = None
) -> pd.DataFrame:
    """
    Loads all .pkl files from the specified directory,
    removes unwanted classes if provided, and returns a cleaned DataFrame.

    :param pickle_dir: Directory containing the .pkl files
    :param remove_classes: Optional list of label_ids to remove
    :return: Filtered and merged DataFrame
    """
    frames = []
    for path in glob.glob(os.path.join(pickle_dir, "*.pkl")):
        df = pd.read_pickle(path)
        if remove_classes:
            df = df[~df["label_id"].isin(remove_classes)]
        df = df.dropna()
        frames.append(df)

    if not frames:
        raise FileNotFoundError(f"No pickle files found in {pickle_dir}")

    combined = pd.concat(frames, ignore_index=True)
    combined = merge_label_ids(combined, LABEL_MAPPING)
    return combined




def merge_label_ids(
    df: pd.DataFrame,
    merge_map: Dict[int, int | str]
) -> pd.DataFrame:
    """
    Ersetzt label_id-Werte gemäß einer Mapping-Tabelle (merge_map).

    :param df: DataFrame mit numerischen label_id-Werten
    :param merge_map: Mapping {id: Klassenname}
    :return: DataFrame mit String-Labels in "label_id"
    """
    df = df.copy()
    df["label_id"] = df["label_id"].replace(merge_map)
    return df
