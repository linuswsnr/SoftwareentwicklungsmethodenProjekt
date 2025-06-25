import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QSplitter  # noqa: E501
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os


class ImageViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RadarScenes Evaluation Viewer")
        self.setGeometry(100, 100, 1200, 800)

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Splitter to separate image area
        splitter = QSplitter(Qt.Horizontal)

        # Left side: show confusion matrix and classification metrics
        left_widget = QWidget()
        left_layout = QVBoxLayout()

        # Label widgets
        self.confusion_label = QLabel("Confusion Matrix")
        self.confusion_image = QLabel()
        self.metrics_label = QLabel("Classification Metrics")
        self.metrics_image = QLabel()

        # Image click handlers
        self.confusion_image.mousePressEvent = self.show_confusion_popup
        self.metrics_image.mousePressEvent = self.show_metrics_popup

        # Add to layout
        left_layout.addWidget(self.confusion_label)
        left_layout.addWidget(self.confusion_image)
        left_layout.addWidget(self.metrics_label)
        left_layout.addWidget(self.metrics_image)

        left_widget.setLayout(left_layout)
        splitter.addWidget(left_widget)

        # Right side placeholder
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_widget.setLayout(right_layout)
        splitter.addWidget(right_widget)

        main_layout.addWidget(splitter)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def load_images(self):
        confusion_path = "results/train_confusion_matrix_confusion.png"
        metrics_path = "results/train_confusion_matrix_metrics.png"

        if os.path.exists(confusion_path):
            pixmap = QPixmap(confusion_path)
            if not pixmap.isNull():
                self.confusion_image.setPixmap(
                    pixmap.scaledToWidth(500, Qt.SmoothTransformation)
                )
            else:
                self.confusion_image.setText(
                    "Bild konnte nicht geladen werden: Confusion Matrix"
                )
        else:
            self.confusion_image.setText("Pfad nicht gefunden: Confusion Matrix")  # noqa: E501

        if os.path.exists(metrics_path):
            pixmap = QPixmap(metrics_path)
            if not pixmap.isNull():
                self.metrics_image.setPixmap(
                    pixmap.scaledToWidth(500, Qt.SmoothTransformation)
                )
            else:
                self.metrics_image.setText(
                    "Bild konnte nicht geladen werden: Classification Metrics"
                )
        else:
            self.metrics_image.setText("Pfad nicht gefunden: Classification Metrics")  # noqa: E501

    def show_confusion_popup(self, event):
        if self.confusion_image.pixmap():
            popup = ImagePopup(self.confusion_image.pixmap(), "Confusion Matrix")  # noqa: E501
            popup.show()

    def show_metrics_popup(self, event):
        if self.metrics_image.pixmap():
            popup = ImagePopup(self.metrics_image.pixmap(), "Classification Metrics")  # noqa: E501
            popup.show()


class ImagePopup(QWidget):
    def __init__(self, pixmap: QPixmap, title: str = "Bildanzeige"):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 1000, 800)

        layout = QVBoxLayout()
        label = QLabel()
        label.setPixmap(pixmap.scaledToWidth(800, Qt.SmoothTransformation))
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.load_images()
    viewer.show()
    sys.exit(app.exec())