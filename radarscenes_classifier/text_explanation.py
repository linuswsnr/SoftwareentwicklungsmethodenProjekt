"""
Automatische Textauswertung für Konfusionsmatrizen und Metriken.
Diese Datei enthält Funktionen zur Generierung von Textauswertungen,
die als Bilder gespeichert werden können.
"""

import os
import numpy as np
import pandas as pd

# Import visualization libraries with error handling
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    from PIL import Image, ImageDraw, ImageFont
    VISUALIZATION_AVAILABLE = True
except ImportError:
    print("Warning: matplotlib, seaborn or PIL not available. Visualization will be skipped.")
    VISUALIZATION_AVAILABLE = False


def create_text_image(text, output_path, title="", width=800, height=600, font_size=14):
    """
    Erstellt ein Bild mit Text und speichert es als PNG.
    
    Args:
        text (str): Der zu rendernde Text
        output_path (str): Pfad zum Speichern des Bildes
        title (str): Titel des Bildes
        width (int): Breite des Bildes
        height (int): Höhe des Bildes
        font_size (int): Schriftgröße
    """
    if not VISUALIZATION_AVAILABLE:
        print("PIL not available. Skipping text image creation.")
        return
    
    try:
        # Bild erstellen
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        
        # Versuche eine Standard-Schriftart zu verwenden
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
            title_font = ImageFont.truetype("arial.ttf", font_size + 4)
        except:
            # Fallback auf Standard-Schriftart
            font = ImageFont.load_default()
            title_font = ImageFont.load_default()
        
        # Titel zeichnen
        if title:
            title_bbox = draw.textbbox((0, 0), title, font=title_font)
            title_width = title_bbox[2] - title_bbox[0]
            title_x = (width - title_width) // 2
            draw.text((title_x, 20), title, fill='black', font=title_font)
            y_offset = 60
        else:
            y_offset = 20
        
        # Text in Zeilen aufteilen
        lines = text.split('\n')
        line_height = font_size + 4
        
        for line in lines:
            if y_offset + line_height > height - 20:
                break  # Verhindert Überlauf
            
            # Text zeichnen
            draw.text((20, y_offset), line, fill='black', font=font)
            y_offset += line_height
        
        # Bild speichern
        img.save(output_path)
        print(f"Text image saved to: {output_path}")
        
    except Exception as e:
        print(f"Error creating text image: {e}")


def generate_confusion_matrix_explanation(cm, labels, output_path):
    """
    Generiert eine automatische Textauswertung der Konfusionsmatrix.
    
    Args:
        cm (numpy.ndarray): Konfusionsmatrix
        labels (list): Klassenlabels
        output_path (str): Pfad zum Speichern des Textbildes
    """
    if not VISUALIZATION_AVAILABLE:
        print("Visualization libraries not available. Skipping confusion matrix explanation.")
        return
    
    text_lines = []
    text_lines.append("AUTOMATISCHE AUSWERTUNG DER KONFUSIONSMATRIX")
    text_lines.append("=" * 50)
    text_lines.append("")
    
    # Gesamtanzahl der Proben
    total_samples = np.sum(cm)
    text_lines.append(f"Gesamtanzahl der Proben: {total_samples:,}")
    text_lines.append("")
    
    # Korrekte Klassifikationen pro Klasse
    text_lines.append("KORREKTE KLASSIFIKATIONEN PRO KLASSE:")
    text_lines.append("-" * 40)
    
    for i, label in enumerate(labels):
        correct = cm[i, i]
        total_class = np.sum(cm[i, :])
        accuracy_per_class = (correct / total_class * 100) if total_class > 0 else 0
        
        text_lines.append(f"• {label}: {correct:,} von {total_class:,} korrekt klassifiziert ({accuracy_per_class:.1f}%)")
    
    text_lines.append("")
    
    # Häufigste Fehlklassifikationen
    text_lines.append("HÄUFIGSTE FEHLKLASSIFIKATIONEN:")
    text_lines.append("-" * 40)
    
    # Finde die größten Fehler (außerhalb der Diagonalen)
    errors = []
    for i in range(len(labels)):
        for j in range(len(labels)):
            if i != j and cm[i, j] > 0:
                errors.append((cm[i, j], labels[i], labels[j]))
    
    # Sortiere nach Häufigkeit
    errors.sort(reverse=True)
    
    for i, (count, true_label, pred_label) in enumerate(errors[:5]):  # Top 5 Fehler
        text_lines.append(f"• {count:,} {true_label} wurden als {pred_label} klassifiziert")
    
    text_lines.append("")
    
    # Gesamtgenauigkeit
    total_correct = np.sum(np.diag(cm))
    overall_accuracy = (total_correct / total_samples * 100) if total_samples > 0 else 0
    text_lines.append(f"GESAMTGENAUIGKEIT: {overall_accuracy:.1f}% ({total_correct:,} von {total_samples:,} korrekt)")
    
    # Text als Bild speichern
    text = '\n'.join(text_lines)
    create_text_image(text, output_path, title="Konfusionsmatrix Auswertung")


def generate_metrics_explanation(report_dict, labels, output_path):
    """
    Generiert eine automatische Textauswertung der Metriken.
    
    Args:
        report_dict (dict): Classification report als Dictionary
        labels (list): Klassenlabels
        output_path (str): Pfad zum Speichern des Textbildes
    """
    if not VISUALIZATION_AVAILABLE:
        print("Visualization libraries not available. Skipping metrics explanation.")
        return
    
    text_lines = []
    text_lines.append("AUTOMATISCHE AUSWERTUNG DER METRIKEN")
    text_lines.append("=" * 50)
    text_lines.append("")
    
    # Durchschnittliche Metriken
    if 'macro avg' in report_dict:
        macro_avg = report_dict['macro avg']
        text_lines.append("DURCHSCHNITTLICHE METRIKEN (Macro Average):")
        text_lines.append("-" * 50)
        text_lines.append(f"• Precision: {macro_avg['precision']:.3f} ({macro_avg['precision']*100:.1f}%)")
        text_lines.append(f"• Recall: {macro_avg['recall']:.3f} ({macro_avg['recall']*100:.1f}%)")
        text_lines.append(f"• F1-Score: {macro_avg['f1-score']:.3f} ({macro_avg['f1-score']*100:.1f}%)")
        text_lines.append("")
    
    # Gewichtete durchschnittliche Metriken
    if 'weighted avg' in report_dict:
        weighted_avg = report_dict['weighted avg']
        text_lines.append("GEWICHTETE DURCHSCHNITTLICHE METRIKEN:")
        text_lines.append("-" * 50)
        text_lines.append(f"• Precision: {weighted_avg['precision']:.3f} ({weighted_avg['precision']*100:.1f}%)")
        text_lines.append(f"• Recall: {weighted_avg['recall']:.3f} ({weighted_avg['recall']*100:.1f}%)")
        text_lines.append(f"• F1-Score: {weighted_avg['f1-score']:.3f} ({weighted_avg['f1-score']*100:.1f}%)")
        text_lines.append("")
    
    # Metriken pro Klasse
    text_lines.append("METRIKEN PRO KLASSE:")
    text_lines.append("-" * 30)
    
    for label in labels:
        if label in report_dict:
            metrics = report_dict[label]
            support = metrics['support']
            text_lines.append(f"• {label}:")
            text_lines.append(f"  - Precision: {metrics['precision']:.3f} ({metrics['precision']*100:.1f}%)")
            text_lines.append(f"  - Recall: {metrics['recall']:.3f} ({metrics['recall']*100:.1f}%)")
            text_lines.append(f"  - F1-Score: {metrics['f1-score']:.3f} ({metrics['f1-score']*100:.1f}%)")
            text_lines.append(f"  - Support: {support:,} Proben")
            text_lines.append("")
    
    # Beste und schlechteste Klassen
    f1_scores = [(label, report_dict[label]['f1-score']) for label in labels if label in report_dict]
    f1_scores.sort(key=lambda x: x[1], reverse=True)
    
    if f1_scores:
        best_class = f1_scores[0]
        worst_class = f1_scores[-1]
        
        text_lines.append("BESTE UND SCHLECHTESTE KLASSEN:")
        text_lines.append("-" * 40)
        text_lines.append(f"• Beste Klasse: {best_class[0]} (F1-Score: {best_class[1]:.3f})")
        text_lines.append(f"• Schlechteste Klasse: {worst_class[0]} (F1-Score: {worst_class[1]:.3f})")
    
    # Text als Bild speichern
    text = '\n'.join(text_lines)
    create_text_image(text, output_path, title="Metriken Auswertung")


def generate_model_info(model, df_train, output_path):
    """
    Generiert Informationen über das Modell und speichert sie als Bild.
    
    Args:
        model: Das trainierte Modell
        df_train (pd.DataFrame): Trainingsdaten
        output_path (str): Pfad zum Speichern des Textbildes
    """
    if not VISUALIZATION_AVAILABLE:
        print("Visualization libraries not available. Skipping model info generation.")
        return
    
    text_lines = []
    text_lines.append("MODELLINFORMATIONEN")
    text_lines.append("=" * 30)
    text_lines.append("")
    
    # Modelltyp
    model_type = type(model).__name__
    text_lines.append(f"Modelltyp: {model_type}")
    text_lines.append("")
    
    # Trainingsdaten
    text_lines.append("TRAININGSDATEN:")
    text_lines.append("-" * 20)
    text_lines.append(f"• Anzahl Proben: {len(df_train):,}")
    text_lines.append(f"• Anzahl Features: {len(df_train.columns) - 1}")  # -1 für label_id
    text_lines.append("")
    
    # Feature-Namen
    feature_cols = [col for col in df_train.columns if col != 'label_id']
    text_lines.append("VERWENDETE FEATURES:")
    text_lines.append("-" * 20)
    for feature in feature_cols:
        text_lines.append(f"• {feature}")
    text_lines.append("")
    
    # Modell-spezifische Informationen
    if hasattr(model, 'n_estimators'):
        text_lines.append(f"Anzahl Bäume: {model.n_estimators}")
    
    if hasattr(model, 'max_depth'):
        text_lines.append(f"Maximale Tiefe: {model.max_depth}")
    
    if hasattr(model, 'learning_rate'):
        text_lines.append(f"Lernrate: {model.learning_rate}")
    
    if hasattr(model, 'random_state'):
        text_lines.append(f"Random State: {model.random_state}")
    
    # Text als Bild speichern
    text = '\n'.join(text_lines)
    create_text_image(text, output_path, title="Modell Informationen")


def generate_automatic_explanations(model, df, label_encoder, cm, report_dict, results_dir="results", prefix=""):
    """
    Generiert automatische Textauswertungen für alle Evaluationsergebnisse.
    
    Args:
        model: Das trainierte Modell
        df (pd.DataFrame): Evaluationsdaten
        label_encoder: Label Encoder
        cm (numpy.ndarray): Konfusionsmatrix
        report_dict (dict): Classification report
        results_dir (str): Verzeichnis zum Speichern der Ergebnisse
        prefix (str): Präfix für Dateinamen (z.B. "train_" oder "test_")
    """
    # Erstelle results Verzeichnis falls es nicht existiert
    os.makedirs(results_dir, exist_ok=True)
    
    # Labels extrahieren
    labels = label_encoder.classes_
    
    # Konfusionsmatrix Auswertung
    confusion_explanation_path = os.path.join(results_dir, f"{prefix}confusion_matrix_explanation.png")
    generate_confusion_matrix_explanation(cm, labels, confusion_explanation_path)
    
    # Metriken Auswertung
    metrics_explanation_path = os.path.join(results_dir, f"{prefix}metrics_explanation.png")
    generate_metrics_explanation(report_dict, labels, metrics_explanation_path)
    
    # Modell Informationen
    model_info_path = os.path.join(results_dir, f"{prefix}model_info.png")
    generate_model_info(model, df, model_info_path)
    
    print("Automatische Textauswertungen wurden erstellt:")
    print(f"- Konfusionsmatrix: {confusion_explanation_path}")
    print(f"- Metriken: {metrics_explanation_path}")
    print(f"- Modellinfo: {model_info_path}")


def evaluate_with_explanations(model, df, label_encoder, output_path=None, plot_path=None, prefix=""):
    """
    Bewertet das Modell und generiert automatische Textauswertungen.
    Diese Funktion ist eine Erweiterung der normalen evaluate_model Funktion.
    
    Args:
        model: Das trainierte Modell
        df (pd.DataFrame): Evaluationsdaten
        label_encoder: Label Encoder
        output_path (str): Pfad für JSON-Ausgabe
        plot_path (str): Pfad für Plot-Ausgabe
        prefix (str): Präfix für Dateinamen (z.B. "train_" oder "test_")
    """
    from sklearn.metrics import classification_report, confusion_matrix
    
    df_eval = df.copy()
    for col in ["sequence", "track_id", "uuid", "timestamp"]:
        if col in df_eval.columns:
            df_eval.drop(columns=col, inplace=True)

    y_true_str = df_eval.pop("label_id")
    X_eval = df_eval.select_dtypes(include=["number"])
    y_true = label_encoder.transform(y_true_str)
    y_pred = model.predict(X_eval)

    target_names = label_encoder.classes_
    report_dict = classification_report(y_true, y_pred,
                                        target_names=target_names,
                                        output_dict=True)
    cm = confusion_matrix(y_true, y_pred)

    print("**Classification Report:**")
    print(classification_report(y_true, y_pred, target_names=target_names))
    print("**Confusion Matrix:**")
    print(cm)

    # Automatische Textauswertungen generieren
    try:
        # Bestimme das results Verzeichnis basierend auf plot_path oder output_path
        if plot_path:
            results_dir = os.path.dirname(plot_path)
        elif output_path:
            results_dir = os.path.dirname(output_path)
        else:
            results_dir = "results"
        
        generate_automatic_explanations(model, df, label_encoder, cm, report_dict, results_dir, prefix)
    except Exception as e:
        print(f"Error generating automatic explanations: {e}")
    
    return report_dict, cm 