from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import json
import numpy as np

# Import visualization libraries with error handling
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    VISUALIZATION_AVAILABLE = True
except ImportError:
    print("Warning: matplotlib or seaborn not available. Visualization will be skipped.")
    VISUALIZATION_AVAILABLE = False


def plot_confusion_matrix(cm, labels, plot_path):
    """Plot confusion matrix with log scaling."""
    if not VISUALIZATION_AVAILABLE:
        print("Visualization libraries not available. Skipping confusion matrix plot.")
        return
    
    # Log-Skalierung vorbereiten (0 wird zu 0.1)
    cm_log = np.log10(np.where(cm == 0, 0.1, cm))

    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        cm_log,
        annot=cm,
        fmt="d",
        cmap="Blues",
        xticklabels=labels,
        yticklabels=labels,
        cbar=False,
        linewidths=0.5,
        linecolor='black',
        square=True
    )

    ax.set_xlabel("Predicted Label", fontsize=16, weight='bold')
    ax.set_ylabel("True Label", fontsize=16, weight='bold')
    ax.tick_params(axis='both', labelsize=10)

    plt.title("Confusion Matrix", fontsize=14)
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()


def plot_classification_report(report_dict, labels, plot_path):
    """
    Erstellt eine PNG-Grafik des Classification Reports
    (Precision, Recall, F1-Score, Support).
    """
    if not VISUALIZATION_AVAILABLE:
        print("Visualization libraries not available. Skipping classification report plot.")
        return

    metrics = ["precision", "recall", "f1-score", "support"]
    values = {m: [report_dict[label][m] for label in labels]
              for m in metrics}

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs = axs.flatten()
    colors = ['#4c72b0', '#55a868', '#c44e52', '#8172b3']

    for i, metric in enumerate(metrics):
        axs[i].bar(labels, values[metric], color=colors)
        axs[i].set_title(metric.capitalize())
        axs[i].set_ylabel(metric.capitalize())
        axs[i].set_ylim(0, max(values[metric]) * 1.1)
        axs[i].tick_params(axis='x', rotation=15)

    plt.suptitle("Klassifikationsmetriken pro Klasse", fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(plot_path)
    plt.close()


def evaluate_model(model, df: pd.DataFrame, label_encoder,
                   output_path: str = None, plot_path: str = None) -> None:
    """
    Bewertet das Modell und gibt die Metriken aus.
    Speichert optional JSON- und PNG-Dateien.
    """
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
    cm_list = cm.tolist()

    print("**Classification Report:**")
    print(classification_report(y_true, y_pred, target_names=target_names))
    print("**Confusion Matrix:**")
    print(cm)

    # Falls gewünscht: in Datei schreiben
    if output_path:
        try:
            output_data = {
                "classification_report": report_dict,
                "confusion_matrix": cm_list,
                "labels": target_names.tolist()
            }
            with open(output_path, "w", encoding='utf-8') as f:
                json.dump(output_data, f, indent=2)
            print(f"Results saved to: {output_path}")
        except Exception as e:
            print(f"Error saving results to {output_path}: {e}")

    # Visualisierung speichern
    if plot_path and VISUALIZATION_AVAILABLE:
        try:
            # Konfusionsmatrix
            plot_confusion_matrix(cm, target_names,
                                  plot_path.replace(".png", "_confusion.png"))

            # Klassifikationsmetriken
            plot_classification_report(report_dict, target_names,
                                       plot_path.replace(".png", "_metrics.png"))
            print(f"Plots saved to: {plot_path.replace('.png', '_confusion.png')} and {plot_path.replace('.png', '_metrics.png')}")
        except Exception as e:
            print(f"Error creating plots: {e}")
    elif plot_path and not VISUALIZATION_AVAILABLE:
        print("Skipping plot creation due to missing visualization libraries.")


