import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow

if __name__ == "__main__":
    # QApplication initialisieren
    app = QApplication(sys.argv)

    # Hauptfenster erstellen und anzeigen
    window = MainWindow()
    window.showMaximized()
    window.show()

    # Event-Loop starten
    sys.exit(app.exec())
