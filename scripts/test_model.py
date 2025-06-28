import os
import sys

# Add the parent directory to Python path before importing modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from radarscenes_classifier import data_preprocessing
from radarscenes_classifier import evaluation
from radarscenes_classifier import text_explanation
import joblib

DATASET_DIR = os.path.join("dataset", "radar_scenes_pickles")
MODEL_PATH = os.path.join("models", "model_lightgbm.pkl")
ENCODER_PATH = os.path.join("models", "label_encoder.pkl")
SPLIT_DIR = "dataset/split_train_test"  # Pfad zu existierendem Split

# Optional: Liste von Test-Sequenznummern, falls
# nur Teilmenge getestet werden soll

TEST_SEQS = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # None = alle nutzen

if __name__ == "__main__":
    # Modell und Encoder laden
    model = joblib.load(MODEL_PATH)
    label_enc = joblib.load(ENCODER_PATH)

    # Daten laden aus existierendem Split (schneller)
    df_train, df_test = data_preprocessing.prepare_sequence_data(
        DATASET_DIR,
        remove_classes=[],
        limit_n_files=None,
        split_ratio=0.8,
        use_existing_split=True,  # Verwende existierenden Split
        split_dir=SPLIT_DIR,
        save_new_split=False
    )

    # Falls spezifische Test-Sequenzen definiert: Daten filtern
    # Prüfe ob 'sequence' Spalte existiert
    if TEST_SEQS and "sequence" in df_test.columns:
        seq_names = [f"sequence_{i}" for i in TEST_SEQS]
        df_test = df_test[df_test["sequence"].isin(seq_names)].copy()
    else:
        if TEST_SEQS and "sequence" not in df_test.columns:
            print("Warnung: 'sequence' Spalte nicht verfügbar, verwende alle Testdaten")
        df_test = df_test  # Verwende alle Testdaten

    # Erstelle results Verzeichnis
    os.makedirs("results", exist_ok=True)

    # 1. Normale Evaluation für Plots und JSON
    print("=== NORMALE EVALUATION (Plots + JSON) ===")
    evaluation.evaluate_model(
        model, 
        df_test, 
        label_enc,
        output_path="results/test_evaluation.json",
        plot_path="results/test_evaluation.png"
    )

    # 2. Automatische Textauswertungen
    print("\n=== AUTOMATISCHE TEXTAUSWERTUNGEN ===")
    report_dict, cm = text_explanation.evaluate_with_explanations(
        model, 
        df_test, 
        label_enc,
        output_path=None,  # JSON bereits erstellt
        plot_path=None,    # Plots bereits erstellt
        prefix="test_"     # Präfix für Test-Dateien
    )
    
    print("\n=== ALLE ERGEBNISSE ERSTELLT ===")
    print("Ordner 'results/' enthält jetzt:")
    print("- test_evaluation.json (Metriken)")
    print("- test_evaluation_confusion.png (Konfusionsmatrix Plot)")
    print("- test_evaluation_metrics.png (Metriken Plot)")
    print("- test_confusion_matrix_explanation.png (Textauswertung Konfusionsmatrix)")
    print("- test_metrics_explanation.png (Textauswertung Metriken)")
    print("- test_model_info.png (Modellinformationen)")