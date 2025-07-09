import os
import sys

# Add the parent directory to Python path before importing modules
import joblib
from radarscenes_classifier import data_preprocessing, training
from radarscenes_classifier import evaluation, text_explanation
sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
        save_new_split=False  # Verwende existierenden Split
                              # erstelle keinen neuen
    )

    # Modell trainieren
    model, label_enc = training.train_model(df_train)

    # Model und Encoder speichern
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(label_enc, ENCODER_PATH)
    print(f"Modell gespeichert nach {MODEL_PATH}")
    print(f"Label-Encoder gespeichert nach {ENCODER_PATH}")

    # Erstelle results Verzeichnis
    os.makedirs("results", exist_ok=True)

    # 1. Normale Evaluation für Plots und JSON
    print("=== NORMALE EVALUATION (Plots + JSON) ===")
    evaluation.evaluate_model(
        model, df_train, label_enc,
        output_path="results/train_evaluation.json",
        plot_path="results/train_confusion_matrix.png"
    )

    # 2. Automatische Textauswertungen
    print("\n=== AUTOMATISCHE TEXTAUSWERTUNGEN ===")
    report_dict, cm = text_explanation.evaluate_with_explanations(
        model,
        df_train,
        label_enc,
        output_path=None,  # JSON bereits erstellt
        plot_path=None,    # Plots bereits erstellt
        prefix="train_"    # Präfix für Train-Dateien
    )

    print("\n=== ALLE ERGEBNISSE ERSTELLT ===")
    print("Ordner 'results/' enthält jetzt:")
    print("- train_evaluation.json (Metriken)")
    print("- train_confusion_matrix_confusion.png (Konfusionsmatrix Plot)")
    print("- train_confusion_matrix_metrics.png (Metriken Plot)")
    print("- train_confusion_matrix_explanation.png (Textauswertung Konfusionsmatrix)")  # noqa: E501
    print("- train_metrics_explanation.png (Textauswertung Metriken)")
    print("- train_model_info.png (Modellinformationen)")
