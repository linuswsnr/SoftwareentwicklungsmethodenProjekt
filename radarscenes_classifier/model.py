from lightgbm import LGBMClassifier

def create_model():
    """Erstellt und konfiguriert das Klassifikationsmodell."""
    # Hier ggf. Hyperparameter an LightGBM übergeben, falls gewünscht.
    return LGBMClassifier()
