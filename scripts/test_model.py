import os
import sys
from radarscenes_classifier import data_preprocessing
from radarscenes_classifier import evaluation
import joblib


# Projektpfad hinzufügen (für relative Importe)
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

sys.path.insert(0,
                os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "..")))

DATASET_DIR = os.path.join("dataset", "radar_scenes_pickles")
MODEL_PATH = os.path.join("models", "model_lightgbm.pkl")
ENCODER_PATH = os.path.join("models", "label_encoder.pkl")

# Optional: Liste von Test-Sequenznummern, falls
# nur Teilmenge getestet werden soll

TEST_SEQS = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # None = alle nutzen

if __name__ == "__main__":
    # Modell und Encoder laden
    model = joblib.load(MODEL_PATH)
    label_enc = joblib.load(ENCODER_PATH)

    # Daten laden (mit derselben Filterung wie beim Training)
    df_all, _ = data_preprocessing.prepare_sequence_data(
        DATASET_DIR,
        remove_classes=[],
        limit_n_files=None
    )

    # Falls spezifische Test-Sequenzen definiert: Daten filtern
    if TEST_SEQS:
        seq_names = [f"sequence_{i}" for i in TEST_SEQS]
        df_test = df_all[df_all["sequence"].isin(seq_names)].copy()
    else:
        df_test = df_all

    # Modell evaluieren
    evaluation.evaluate_model(model, df_test, label_enc)
