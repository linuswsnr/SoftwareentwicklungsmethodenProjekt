import os
import glob
import pandas as pd
from typing import Optional, List
from tqdm import tqdm


# Mapping: numerische Label-IDs -> Klassenname (vereinheitlichte Labels)
BASIS_LABEL_MAPPING = {
    0: "CAR", 1: "CAR", 2: "CAR", 3: "CAR", 4: "CAR",
    5: "TWO-WHEELER", 6: "TWO-WHEELER",
    7: "PEDESTRIAN", 8: "PEDESTRIAN",
    9: "INFRASTRUCTURE", 10: "INFRASTRUCTURE", 11: "INFRASTRUCTURE"
}


def merge_label_ids(
    df: pd.DataFrame, merge_map: Optional[dict] = None
) -> pd.DataFrame:
    """
    Ersetzt label_id-Werte gemäß Mapping-Tabelle
    (merge_map) durch Klassen-Namen. Wenn kein Mapping
    übergeben wird, wird das Standard-LABEL_MAPPING genutzt.
    """
    df = df.copy()
    forbidden_ids = {7, 8, 9, 10, 11}

    if merge_map is None:
        merge_map = BASIS_LABEL_MAPPING
        df["label_id"] = df["label_id"].replace(merge_map)
    else:
        forbidden = [
            k for k, v in merge_map.items()
            if v == "CAR" and k in forbidden_ids
        ]
        if forbidden:
            raise ValueError(
                "Ungültige Zuordnung: Diese label_ids dürfen nicht auf "
                f"'CAR' gemappt werden: {forbidden}"
            )
        df["label_id"] = df["label_id"].replace(merge_map)

    return df


def prepare_sequence_data(
    pickle_dir: str,
    remove_classes: Optional[List[int]] = None,
    limit_n_files: Optional[int] = None,
    split_ratio: float = 0.8,
    use_existing_split: bool = False,
    split_dir: str = "dataset/split_train_test",
    save_new_split: bool = False,
    remove_features: Optional[List[str]] = None
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Lädt Pickle-Dateien aus dem Verzeichnis und
    bereitet Trainings-/Testdaten vor.
    """
    train_path = os.path.join(split_dir, "train.pkl")
    test_path = os.path.join(split_dir, "test.pkl")

    if use_existing_split:
        if os.path.exists(train_path) and os.path.exists(test_path):
            print("Bestehender Split wird geladen.")
            df_train = pd.read_pickle(train_path)
            df_test = pd.read_pickle(test_path)
            return df_train, df_test
        else:
            raise FileNotFoundError(
                f"Train/Test-Split konnte unter {split_dir} "
                "nicht gefunden werden"
            )

    pkl_paths = glob.glob(os.path.join(pickle_dir, "*.pkl"))

    if limit_n_files is not None:
        pkl_paths = pkl_paths[:limit_n_files]

    frames = []
    for pkl_path in tqdm(pkl_paths, desc="Lade Pickle-Dateien"):
        df = pd.read_pickle(pkl_path)

        if remove_classes:
            df = df[~df["label_id"].isin(remove_classes)]

        if remove_features:
            df = df.drop(
                columns=[col for col in remove_features if col in df.columns],
                errors="ignore"
            )

        df = df.dropna()
        frames.append(df)

    if not frames:
        raise FileNotFoundError(
            f"Keine Pickle-Dateien in {pickle_dir} gefunden."
        )

    combined = pd.concat(frames, ignore_index=True)
    combined = merge_label_ids(combined)

    from sklearn.model_selection import train_test_split
    df_train, df_test = train_test_split(
        combined,
        test_size=(1 - split_ratio),
        random_state=42,
        shuffle=True
    )

    if save_new_split and not use_existing_split:
        os.makedirs(split_dir, exist_ok=True)
        df_train.to_pickle(train_path)
        df_test.to_pickle(test_path)
        print("Neuer Split als Pickle gespeichert.")

    return df_train, df_test


if __name__ == "__main__":
    test_map = {
        0: "CAR", 1: "CAR", 2: "CAR", 3: "CAR", 4: "CAR", 7: "CAR",
        5: "TWO-WHEELER", 6: "TWO-WHEELER",
        8: "PEDESTRIAN",
        9: "INFRASTRUCTURE", 10: "INFRASTRUCTURE", 11: "INFRASTRUCTURE"
    }

    df_train, df_test = prepare_sequence_data(
        "dataset/radar_scenes_pickles",
        None,
        5,
        remove_features=["x_cc"]
    )

    df_checked = merge_label_ids(df_train)

    features = ["x_cc", "y_cc", "rcs"]
    for f in features:
        if f in df_checked.columns:
            print(f"{f} vorhanden")
        else:
            print(f"{f} fehlt")
