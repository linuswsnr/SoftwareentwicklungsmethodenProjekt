from PySide6.QtWidgets import (
    QMainWindow, QFileDialog, QLabel
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from gui.main_window_ui import Ui_MainWindow
from PySide6.QtWidgets import QMessageBox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button-Klicks mit Funktionen verbinden
        self.ui.konf_laden_pushbotten.clicked.connect(
            lambda: self.load_image(self.ui.konfusionsmatrix_label)
        )
        self.ui.metrik_laden_pushbotton.clicked.connect(
            lambda: self.load_image(self.ui.metriken_label)
        )
        self.ui.konf_text_laden_pushbutton.clicked.connect(
            lambda: self.load_image(self.ui.konf_text_label)
        )
        self.ui.metriken_text_laden_pushbutton.clicked.connect(
            lambda: self.load_image(self.ui.metriken_text_label)
        )
        self.ui.modell_info_laden_pushbutton.clicked.connect(
            lambda: self.load_image(self.ui.modell_info_label)
        )
        self.ui.punktewolke_laden_pushbutton.clicked.connect(
            lambda: self.load_image(self.ui.punktewolke_bild_label)
        )
        # Export-Funktion wird später von einem anderen Teammitglied ergänzt
        self.ui.export_pushbutton.clicked.connect(self.export_pdf)

    def load_image(self, label: QLabel):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Bild auswählen", "", "Bilder (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path and os.path.exists(file_path):
            pixmap = QPixmap(file_path)
            label.setPixmap(pixmap.scaled(label.size(),
                            Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            label.setText("Bild konnte nicht geladen werden")

    def export_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "PDF speichern", "", "PDF-Dateien (*.pdf)")  # noqa: E501
        if not file_path:
            return

        try:
            c = canvas.Canvas(file_path, pagesize=A4)
            width, height = A4
            margin = 50
            y_position = height - margin  # initiale y-Position

            # Titel
            c.setFont("Helvetica-Bold", 20)
            c.drawCentredString(width / 2, y_position, "Ergebnisse der LightGBM Klassifikation")  # noqa: E501
            y_position -= 60  # Abstand nach dem Titel

            # Liste deiner QLabel-Bildquellen
            image_labels = [
                self.ui.konfusionsmatrix_label,
                self.ui.konf_text_label,
                self.ui.metriken_label,
                self.ui.metriken_text_label,
                self.ui.punktewolke_bild_label,
            ]

            for idx, label in enumerate(image_labels):
                pixmap = label.pixmap()
                if pixmap and not pixmap.isNull():
                    temp_path = f"temp_export_{idx}.png"
                    pixmap.save(temp_path)

                    img = ImageReader(temp_path)
                    iw, ih = pixmap.width(), pixmap.height()
                    max_width = width - 2 * margin
                    scale = max_width / iw
                    display_height = ih * scale

                    # Seitenumbruch falls nötig
                    if y_position - display_height < margin:
                        c.showPage()
                        y_position = height - margin

                    y_position -= display_height
                    c.drawImage(img, margin, y_position, width=max_width, height=display_height)  # noqa: E501
                    y_position -= 30  # Abstand nach Bild

                    os.remove(temp_path)

            c.save()
            QMessageBox.information(self, "Erfolg", f"PDF erfolgreich gespeichert:\n{file_path}")  # noqa: E501

        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"PDF-Export fehlgeschlagen:\n{str(e)}")  # noqa: E501
