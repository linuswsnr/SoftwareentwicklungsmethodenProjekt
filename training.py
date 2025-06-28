from sklearn.preprocessing import LabelEncoder
from radarscenes_classifier import model
import pandas as pd


def train_model(df: pd.DataFrame):
    """
    Trainiert das Modell auf den gegebenen Daten-DataFrame.
    Return: (trained_model, label_encoder)
    """
    # Features (X) und Label (y) trennen:
    # Unnötige Spalten entfernen (sofern vorhanden)
    df_train = df.copy()
    for col in ["sequence", "track_id", "uuid", "timestamp"]:
        if col in df_train.columns:
            df_train.drop(columns=col, inplace=True)
    # Label-Spalte isolieren und aus Feature-Frame entfernen
    y = df_train.pop("label_id")
    X = df_train.select_dtypes(include=["number"])  # nur numerische Merkmale
    # Label-Encoding (String -> Integer)
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    # Modell erzeugen und trainieren
    clf = model.create_model()
    clf.fit(X, y_encoded)
    return clf, label_encoder
