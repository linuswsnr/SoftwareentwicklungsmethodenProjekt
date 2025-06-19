# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 649)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(1)

        self.allgemeiner_text_label = QLabel(self.centralwidget)
        self.allgemeiner_text_label.setObjectName("allgemeiner_text_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.allgemeiner_text_label.setSizePolicy(sizePolicy)
        self.allgemeiner_text_label.setStyleSheet("QLabel { background-color: white; color: #2c2c2c; font-size: 10pt; font-weight: bold; padding: 10px; border: 1px solid #cccccc; border-radius: 5px; qproperty-alignment: 'AlignLeft'; }")
        self.gridLayout_2.addWidget(self.allgemeiner_text_label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.export_pushbutton = QPushButton(self.centralwidget)
        self.export_pushbutton.setObjectName("export_pushbutton")
        self.export_pushbutton.setStyleSheet("color: white; font-size: 10pt; font-weight: bold; background-color: green; border: 1px solid #cccccc; padding: 8px;")
        self.gridLayout_2.addWidget(self.export_pushbutton, 0, 2, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QTabWidget.North)

        # Performance Tab
        self.performance_tab = QWidget()
        self.performance_tab.setObjectName("performance_tab")
        self.gridLayout = QGridLayout(self.performance_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.konf_laden_pushbotten = QPushButton(self.performance_tab)
        self.konf_laden_pushbotten.setObjectName("konf_laden_pushbotten")
        self.gridLayout.addWidget(self.konf_laden_pushbotten, 0, 0, 1, 1)

        self.metrik_laden_pushbotton = QPushButton(self.performance_tab)
        self.metrik_laden_pushbotton.setObjectName("metrik_laden_pushbotton")
        self.gridLayout.addWidget(self.metrik_laden_pushbotton, 0, 1, 1, 1)

        self.modell_info_label = QLabel(self.performance_tab)
        self.modell_info_label.setObjectName("modell_info_label")
        sizePolicy.setHeightForWidth(self.modell_info_label.sizePolicy().hasHeightForWidth())
        self.modell_info_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.modell_info_label.setFont(font)
        self.modell_info_label.setStyleSheet("background-color: white; border: 1px solid #cccccc; padding: 2px; qproperty-alignment: 'AlignCenter'")
        self.gridLayout.addWidget(self.modell_info_label, 0, 2, 1, 1)

        self.konfusionsmatrix_label = QLabel(self.performance_tab)
        self.konfusionsmatrix_label.setObjectName("konfusionsmatrix_label")
        self.konfusionsmatrix_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.konfusionsmatrix_label.setStyleSheet("background-color: white; border: 1px solid #cccccc; padding: 8px; qproperty-alignment: 'AlignCenter'")
        self.gridLayout.addWidget(self.konfusionsmatrix_label, 1, 0, 1, 1)

        self.metriken_label = QLabel(self.performance_tab)
        self.metriken_label.setObjectName("metriken_label")
        self.metriken_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.metriken_label.setStyleSheet("background-color: white; border: 1px solid #cccccc; padding: 8px; qproperty-alignment: 'AlignCenter'")
        self.gridLayout.addWidget(self.metriken_label, 1, 1, 1, 1)

        self.konf_text_label = QLabel(self.performance_tab)
        self.konf_text_label.setObjectName("konf_text_label")
        self.konf_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.konf_text_label.setStyleSheet("background-color: white; border: 1px solid #cccccc; padding: 8px; qproperty-alignment: 'AlignCenter'")
        self.gridLayout.addWidget(self.konf_text_label, 2, 0, 1, 1)

        self.metriken_text_label = QLabel(self.performance_tab)
        self.metriken_text_label.setObjectName("metriken_text_label")
        self.metriken_text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.metriken_text_label.setStyleSheet("background-color: white; border: 1px solid #cccccc; padding: 8px; qproperty-alignment: 'AlignCenter'")
        self.gridLayout.addWidget(self.metriken_text_label, 2, 1, 1, 1)

        self.konf_text_laden_pushbutton = QPushButton(self.performance_tab)
        self.konf_text_laden_pushbutton.setObjectName("konf_text_laden_pushbutton")
        self.gridLayout.addWidget(self.konf_text_laden_pushbutton, 3, 0, 1, 1)

        self.metriken_text_laden_pushbutton = QPushButton(self.performance_tab)
        self.metriken_text_laden_pushbutton.setObjectName("metriken_text_laden_pushbutton")
        self.gridLayout.addWidget(self.metriken_text_laden_pushbutton, 3, 1, 1, 1)

        self.modell_und_parameter_inhalt_label = QLabel(self.performance_tab)
        self.modell_und_parameter_inhalt_label.setObjectName("modell_und_parameter_inhalt_label")
        self.modell_und_parameter_inhalt_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.modell_und_parameter_inhalt_label.setStyleSheet("background-color: white; border: 1px solid #cccccc; padding: 8px; qproperty-alignment: 'AlignCenter'")
        self.gridLayout.addWidget(self.modell_und_parameter_inhalt_label, 1, 2, 2, 1)

        self.modell_info_laden_pushbutton = QPushButton(self.performance_tab)
        self.modell_info_laden_pushbutton.setObjectName("modell_info_laden_pushbutton")
        self.gridLayout.addWidget(self.modell_info_laden_pushbutton, 3, 2, 1, 1)

        self.tabWidget.addTab(self.performance_tab, "Performance Übersicht")

        # Classification Tab
        self.classification_tab = QWidget()
        self.classification_tab.setObjectName("classification_tab")
        self.gridLayout_3 = QGridLayout(self.classification_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.punktewolke_laden_pushbutton = QPushButton(self.classification_tab)
        self.punktewolke_laden_pushbutton.setObjectName("punktewolke_laden_pushbutton")
        self.gridLayout_3.addWidget(self.punktewolke_laden_pushbutton, 0, 0, 1, 1)

        self.punktewolke_bild_label = QLabel(self.classification_tab)
        self.punktewolke_bild_label.setObjectName("punktewolke_bild_label")
        self.punktewolke_bild_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.punktewolke_bild_label.setStyleSheet("background-color: white; border: 1px solid #cccccc; padding: 8px; qproperty-alignment: 'AlignCenter'")
        self.gridLayout_3.addWidget(self.punktewolke_bild_label, 1, 0, 1, 1)

        self.tabWidget.addTab(self.classification_tab, "Klassifikator anwenden")

        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow"))
        self.konf_laden_pushbotten.setText(QCoreApplication.translate("MainWindow", "Konfusionsmatrix Grafik auswählen..."))
        self.metrik_laden_pushbotton.setText(QCoreApplication.translate("MainWindow", "Metriken Grafik auswählen..."))
        self.modell_info_label.setText(QCoreApplication.translate("MainWindow", "Verwendetes Modell und Parameter"))
        self.konfusionsmatrix_label.setText(QCoreApplication.translate("MainWindow", "Hier Konfusionsmatrix-Bild"))
        self.metriken_label.setText(QCoreApplication.translate("MainWindow", "Hier Metriken-Bild"))
        self.konf_text_label.setText(QCoreApplication.translate("MainWindow", "Hier Konfusionsmatrix-Erläuterung"))
        self.metriken_text_label.setText(QCoreApplication.translate("MainWindow", "Hier Metriken-Erläuterung"))
        self.konf_text_laden_pushbutton.setText(QCoreApplication.translate("MainWindow", "Konfusionsmatrix Erläuterung auswählen..."))
        self.metriken_text_laden_pushbutton.setText(QCoreApplication.translate("MainWindow", "Metriken Erläuterung auswählen..."))
        self.modell_und_parameter_inhalt_label.setText(QCoreApplication.translate("MainWindow", "Hier die Erläuterung des Modells\nund der verwendeten Parameter"))
        self.modell_info_laden_pushbutton.setText(QCoreApplication.translate("MainWindow", "Modell Erläuterung auswählen..."))
        self.punktewolke_laden_pushbutton.setText(QCoreApplication.translate("MainWindow", "Subplot auswählen..."))
        self.punktewolke_bild_label.setText(QCoreApplication.translate("MainWindow", "Hier die gelabelte Punktewolke und das dazugehörige Bild aus dem Datensatz"))
        self.export_pushbutton.setText(QCoreApplication.translate("MainWindow", "PDF-Export"))
        self.allgemeiner_text_label.setText(QCoreApplication.translate("MainWindow", "Übersicht der Modellleistung mit Möglichkeit zur Anzeige und Erläuterung der Ergebnisse."))
