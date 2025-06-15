import os
import json
from sklearn.metrics import classification_report, confusion_matrix

def save_confusion_matrix(y_true, y_pred, labels, path='results/confusion_matrix.json'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    matrix = confusion_matrix(y_true, y_pred).tolist()
    with open(path, 'w') as f:
        json.dump({
            "labels": labels,
            "matrix": matrix
        }, f, indent=4)
    print(f"Konfusionsmatrix gespeichert unter {path}")

def save_classification_report(y_true, y_pred, labels, path='results/classification_report.json'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    report = classification_report(y_true, y_pred, target_names=labels, output_dict=True)
    with open(path, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"Classification Report gespeichert unter {path}")