import os
import sys

# Add the parent directory to Python path before importing modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from radarscenes_classifier import data_loading

RAW_DATA_DIR = os.path.join("dataset", "radar_scenes", "data")
OUTPUT_DIR = os.path.join("dataset", "radar_scenes_pickles")

if __name__ == "__main__":
    try:
        data_loading.generate_all_sequence_pickles(RAW_DATA_DIR, OUTPUT_DIR)
    except Exception as e:
        print(f"Fehler bei der Datensatzerstellung: {e}")
