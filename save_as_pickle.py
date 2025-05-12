import os
import h5py
import pandas as pd
from tqdm import tqdm


# Root path to the original sequences
BASE_PATH = "dataset/RadarScenes/data"

# Root path to the filtered sequences saves as pickle files
PKL_PATH = "dataset/RadarScenes_pickles"


def main():
    if not os.path.exists(PKL_PATH):
        os.makedirs(PKL_PATH)

    sequence_dirs = sorted(
        [d for d in os.listdir(BASE_PATH) if d.startswith("sequence_")],
        key=extract_number
    )

    for seq in tqdm(sequence_dirs, desc="Convert h5 to pickle"):
        convert_sequence_to_pickle(seq, BASE_PATH, PKL_PATH)


# Find and organize all sequence folders, ignore other files
def extract_number(x):
    try:
        return int(x.split("_")[1])
    except (IndexError, ValueError):
        return float('inf')  # sorts invalid entries to the end


def convert_sequence_to_pickle(seq, BASE_PATH, PKL_PATH):
    seq_path = os.path.join(BASE_PATH, seq)
    h5_file_path = os.path.join(seq_path, "radar_data.h5")

    if not os.path.exists(h5_file_path):
        print(f"File missing: {h5_file_path}")
        return

    try:
        with h5py.File(h5_file_path, "r") as f:
            radar_data = f["radar_data"]
            df = pd.DataFrame({name: radar_data[name] for name in radar_data.dtype.names})
            df.to_pickle(os.path.join(PKL_PATH, f"{seq}.pkl"))
    except Exception as e:
        print(f"Error processing {h5_file_path}: {e}")


if __name__ == "__main__":
    main()