import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import joblib
from radarscenes_classifier import data_preprocessing, training, evaluation

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

DATASET_DIR = os.path.join("dataset", "radar_scenes_pickles")
REMOVE_CLASSES = []  # Beispiel: Klasse 9 und 11 ausschließen (optional)
MODEL_PATH = os.path.join("models", "model_lightgbm.pkl")
ENCODER_PATH = os.path.join("models", "label_encoder.pkl")
SPLIT_DIR = "dataset/split_train_test"  # Pfad zu Train-Test-Split

if __name__ == "__main__":
    # Daten laden und vorverarbeiten
    df_train, df_test = data_preprocessing.prepare_sequence_data(
        DATASET_DIR,
        remove_classes=REMOVE_CLASSES,
        limit_n_files=30,
        split_ratio=0.8,
        use_existing_split=True,
        split_dir=SPLIT_DIR,
        save_new_split=True
    )

    # Modell trainieren
    model, label_enc = training.train_model(df_train)

    # Model und Encoder speichern
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(label_enc, ENCODER_PATH)
    print(f"Modell gespeichert nach {MODEL_PATH}")
    print(f"Label-Encoder gespeichert nach {ENCODER_PATH}")

    # Optional: Trainingsergebnis auf Trainingsdaten ausgeben
    evaluation.evaluate_model(model, df_train, label_enc, output_path="results/train_evaluation.json", plot_path="results/train_confusion_matrix.png")