# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'open_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_open_dialog(object):
    def setupUi(self, open_dialog):
        if not open_dialog.objectName():
            open_dialog.setObjectName(u"open_dialog")
        open_dialog.resize(750, 205)
        self.buttonBox = QDialogButtonBox(open_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(580, 170, 160, 30))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_folder = QLabel(open_dialog)
        self.label_folder.setObjectName(u"label_folder")
        self.label_folder.setGeometry(QRect(10, 10, 231, 30))
        self.selected_csv_label = QLabel(open_dialog)
        self.selected_csv_label.setObjectName(u"selected_csv_label")
        self.selected_csv_label.setGeometry(QRect(10, 110, 641, 30))
        self.selected_csv_label.setAutoFillBackground(False)
        self.selected_csv_label.setFrameShape(QFrame.Box)
        self.selected_folder_label = QLabel(open_dialog)
        self.selected_folder_label.setObjectName(u"selected_folder_label")
        self.selected_folder_label.setGeometry(QRect(10, 40, 641, 30))
        self.selected_folder_label.setAutoFillBackground(False)
        self.selected_folder_label.setFrameShape(QFrame.Box)
        self.openfolder_button = QPushButton(open_dialog)
        self.openfolder_button.setObjectName(u"openfolder_button")
        self.openfolder_button.setGeometry(QRect(660, 39, 80, 30))
        self.opencsv_button = QPushButton(open_dialog)
        self.opencsv_button.setObjectName(u"opencsv_button")
        self.opencsv_button.setGeometry(QRect(660, 110, 80, 30))
        self.label_csvfile = QLabel(open_dialog)
        self.label_csvfile.setObjectName(u"label_csvfile")
        self.label_csvfile.setGeometry(QRect(10, 80, 500, 30))

        self.retranslateUi(open_dialog)
        self.buttonBox.rejected.connect(open_dialog.reject)

        QMetaObject.connectSlotsByName(open_dialog)
    # setupUi

    def retranslateUi(self, open_dialog):
        open_dialog.setWindowTitle(QCoreApplication.translate("open_dialog", u"Open", None))
        self.label_folder.setText(QCoreApplication.translate("open_dialog", u"Select folder containing images", None))
        self.selected_csv_label.setText("")
        self.selected_folder_label.setText("")
        self.openfolder_button.setText(QCoreApplication.translate("open_dialog", u"...", None))
        self.opencsv_button.setText(QCoreApplication.translate("open_dialog", u"...", None))
        self.label_csvfile.setText(QCoreApplication.translate("open_dialog", u"Select csv file", None))
    # retranslateUi

