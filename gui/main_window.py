from PySide6.QtWidgets import (
    QMainWindow, QFileDialog, QLabel
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from gui.main_window_ui import Ui_MainWindow
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
        self.ui.punktewolke_laden_pushbutton.clicked.connect(
            lambda: self.load_image(self.ui.punktewolke_bild_label)
        )
        # Export-Funktion wird später von einem anderen Teammitglied ergänzt
        self.ui.export_pushbutton.clicked.connect(self.export_pdf_placeholder)

    def load_image(self, label: QLabel):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Bild auswählen", "", "Bilder (*.png *.jpg *.jpeg *.bmp)"
        )
        if file_path and os.path.exists(file_path):
            pixmap = QPixmap(file_path)
            label.setPixmap(pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            label.setText("Bild konnte nicht geladen werden")

    def export_pdf_placeholder(self):
        print("Export-Funktion wird noch implementiert.")
