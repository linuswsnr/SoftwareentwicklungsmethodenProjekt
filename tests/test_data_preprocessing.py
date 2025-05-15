import pandas as pd
import pytest

from radarscenes_classifier import data_preprocessing as dp

def test_merge_label_ids():
    df = pd.DataFrame({"label_id": [0, 1, 5, 7, 11]})
    mapping = {0: "CAR", 1: "CAR", 5: "TWO", 7: "PED", 11: "INFRA"}
    result = dp.merge_label_ids(df, mapping)
    assert list(result["label_id"]) == ["CAR", "CAR", "TWO", "PED", "INFRA"]

def test_prepare_sequence_data(tmp_path):
    # Dummy-Pickle mit Labels 0,9,11 erzeugen
    df = pd.DataFrame({"label_id": [0, 9, 11]})
    pkl_file = tmp_path / "dummy.pkl"
    df.to_pickle(pkl_file)
    # remove_classes=[9,11] -> es sollte nur Label 0 ("CAR") übrig bleiben
    combined = dp.prepare_sequence_data(pickle_dir=tmp_path, remove_classes=[], limit_n_files=1)
    assert combined["label_id"].tolist() == ["CAR"]

def test_prepare_sequence_data_no_files(tmp_path):
    # Leeres Verzeichnis -> sollte FileNotFoundError werfen
    with pytest.raises(FileNotFoundError):
        dp.prepare_sequence_data(pickle_dir=tmp_path, remove_classes=[], limit_n_files=1)
