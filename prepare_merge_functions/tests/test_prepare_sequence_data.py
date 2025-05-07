import pandas as pd
import pytest
from radar_utils.prepare_and_merge import merge_label_ids, prepare_sequence_data


def test_merge_label_ids():
    df = pd.DataFrame({"label_id": [0, 1, 5, 7, 11]})
    mapping = {0: "CAR", 1: "CAR", 5: "TWO", 7: "PED", 11: "INFRA"}
    out = merge_label_ids(df, mapping)
    assert list(out["label_id"]) == ["CAR", "CAR", "TWO", "PED", "INFRA"]


def test_prepare_sequence_data(tmp_path):
    # Create a temporary Pickle file with 3 classes: 0 (CAR), 9, 11 (to be removed)
    df = pd.DataFrame({"label_id": [0, 9, 11]})
    pkl_path = tmp_path / "dummy.pkl"
    df.to_pickle(pkl_path)

    cleaned = prepare_sequence_data(remove_classes=[9, 11], pickle_dir=tmp_path)

    # After filtering and mapping, only 'CAR' should remain
    assert cleaned["label_id"].tolist() == ["CAR"]


def test_prepare_sequence_data_no_files(tmp_path):
    # If no .pkl file exists in the directory, FileNotFoundError should be raised
    with pytest.raises(FileNotFoundError):
        prepare_sequence_data(remove_classes=[], pickle_dir=tmp_path)


#pytest --cov=radar_utils --cov-report=term-missing -q


