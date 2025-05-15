import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from radarscenes_classifier import data_preprocessing, training, evaluation
import joblib


DATASET_DIR = os.path.join("dataset", "radar_scenes_pickles")
# REMOVE_CLASSES = [9, 11]  # Beispiel: Klasse 9 und 11 ausschließen (optional)
REMOVE_CLASSES = []  # Beispiel: Klasse 9 und 11 ausschließen (optional)

MODEL_PATH = os.path.join("models", "model_lightgbm.pkl")
ENCODER_PATH = os.path.join("models", "label_encoder.pkl")

if __name__ == "__main__":
    # Daten laden und vorverarbeiten
    df_all = data_preprocessing.prepare_sequence_data(DATASET_DIR,
                                                      remove_classes=REMOVE_CLASSES,
                                                      limit_n_files=30)
    # Modell trainieren
    model, label_enc = training.train_model(df_all)
    # Model und Encoder speichern
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(label_enc, ENCODER_PATH)
    print(f"Modell gespeichert nach {MODEL_PATH}")
    print(f"Label-Encoder gespeichert nach {ENCODER_PATH}")
    # (Optional) Trainingsergebnis auf Trainingsdaten ausgeben:
    evaluation.evaluate_model(model, df_all, label_enc)
