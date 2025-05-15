from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd


def evaluate_model(model, df: pd.DataFrame, label_encoder) -> None:
    """
    Bewertet das gegebene Modell mit den Daten in df und gibt Metriken aus.
    Nutzt den label_encoder, um die true labels zu encodieren.
    """
    df_eval = df.copy()
    # Wie im Training: irrelevante Spalten entfernen
    for col in ["sequence", "track_id", "uuid", "timestamp"]:
        if col in df_eval.columns:
            df_eval.drop(columns=col, inplace=True)
    y_true_str = df_eval.pop("label_id")
    X_eval = df_eval.select_dtypes(include=["number"])
    # Labels encodieren mit demselben Encoder wie im Training
    y_true = label_encoder.transform(y_true_str)
    # Vorhersagen
    y_pred = model.predict(X_eval)
    # Metriken berechnen
    target_names = label_encoder.classes_
    print("**Classification Report:**")
    print(classification_report(y_true, y_pred, target_names=target_names))
    cm = confusion_matrix(y_true, y_pred)
    print("**Confusion Matrix:**")
    print(cm)
