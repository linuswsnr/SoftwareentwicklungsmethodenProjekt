# gui/image_viewer.py
from PySide6.QtWidgets import QWidget, QLabel, QScrollArea, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        # Layout für ImageViewer (einfach vertikal, da nur ein Widget enthalten ist)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # QLabel zur Anzeige des Bildes
        self.image_label = QLabel("Noch kein Bild geladen")
        self.image_label.setAlignment(Qt.AlignCenter)  # zentriere Text/Bild
        # Optional: Rahmen um das Label (für besseres Erkennen des Bereichs)
        # self.image_label.setFrameShape(QFrame.Box)

        # QScrollArea, die das QLabel enthält
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.image_label)
        # ScrollArea soll nur so groß wie nötig sein und Scrollbars zeigen, wenn nötig
        self.scroll_area.setWidgetResizable(False)
        # (Wenn man setWidgetResizable(True) setzt, würde das Label die ScrollArea ausfüllen.
        # Hier belassen wir False, sodass das Label seine Größe vom Bild bezieht.)

        layout.addWidget(self.scroll_area)

    def set_image(self, file_path: str):
        """Lädt das Bild vom gegebenen Dateipfad und zeigt es an."""
        pixmap = QPixmap(file_path)
        if pixmap.isNull():
            # Bild konnte nicht geladen werden (unsupported format oder Fehler)
            self.image_label.setText("Fehler: Bild konnte nicht geladen werden.")
        else:
            self.image_label.setPixmap(pixmap)
            # Größe des Labels an Bildgröße anpassen, damit ScrollArea weiß, wann zu scrollen ist
            self.image_label.adjustSize()
