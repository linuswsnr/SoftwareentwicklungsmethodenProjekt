from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QFrame, QFileDialog
)
from PySide6.QtGui import QCloseEvent
# Import der ImageViewer-Komponente (siehe image_viewer.py)
from gui.image_viewer import ImageViewer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ergebnisvisualisierung")

        # Zentrales Widget und Hauptlayout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(10, 10, 10, 10)

        # Titel-Label (Überschrift)
        title_label = QLabel("Ergebnisvisualisierung")
        title_label.setStyleSheet("font-weight: bold; font-size: 16pt;")
        layout.addWidget(title_label)

        # Info-Label (Beschreibungstext)
        info_text = (
            "Diese Anwendung ermöglicht es, Ergebnisgrafiken "
            "(z.B. Konfusionsmatrizen) anzuzeigen.\n"
            "Wählen Sie dazu eine Bilddatei aus dem Ergebnis-Ordner aus."
        )
        info_label = QLabel(info_text)
        info_label.setStyleSheet("font-size: 10pt;")
        info_label.setWordWrap(True)
        layout.addWidget(info_label)

        # Optionale Trennlinie
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Button zum Öffnen des Datei-Dialogs
        open_button = QPushButton("Bild laden...")
        open_button.clicked.connect(self.open_image_file)
        layout.addWidget(open_button)

        # ImageViewer-Komponente für die Bildanzeige
        self.image_viewer = ImageViewer()
        layout.addWidget(self.image_viewer)

    def open_image_file(self):
        """
        Öffnet einen Dateidialog, damit der Nutzer ein Bild wählen kann
        und zeigt das gewählte Bild im ImageViewer an.
        """
        file_types = "Bilddateien (*.png *.jpg *.jpeg *.bmp)"
        start_dir = ""  # z. B. "./results"
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Bild auswählen", start_dir, file_types
        )
        if file_path:
            self.image_viewer.set_image(file_path)

    def closeEvent(self, event: QCloseEvent):
        event.accept()
