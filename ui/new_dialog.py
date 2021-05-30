# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_new_dialog(object):
    def setupUi(self, new_dialog):
        if not new_dialog.objectName():
            new_dialog.setObjectName(u"new_dialog")
        new_dialog.resize(750, 550)
        self.buttonBox = QDialogButtonBox(new_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(580, 510, 160, 30))
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.headline_folder = QLabel(new_dialog)
        self.headline_folder.setObjectName(u"headline_folder")
        self.headline_folder.setGeometry(QRect(10, 10, 431, 30))
        self.headline_num_labels = QLabel(new_dialog)
        self.headline_num_labels.setObjectName(u"headline_num_labels")
        self.headline_num_labels.setGeometry(QRect(10, 210, 431, 30))
        self.labels_inputs_description = QLabel(new_dialog)
        self.labels_inputs_description.setObjectName(u"labels_inputs_description")
        self.labels_inputs_description.setGeometry(QRect(430, 240, 311, 30))
        self.selected_folder_label = QLabel(new_dialog)
        self.selected_folder_label.setObjectName(u"selected_folder_label")
        self.selected_folder_label.setGeometry(QRect(20, 50, 631, 30))
        self.selected_folder_label.setFrameShape(QFrame.Box)
        self.browse_button = QPushButton(new_dialog)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setGeometry(QRect(660, 50, 80, 30))
        self.confirm_num_labels = QPushButton(new_dialog)
        self.confirm_num_labels.setObjectName(u"confirm_num_labels")
        self.confirm_num_labels.setGeometry(QRect(660, 270, 80, 30))
        self.numLabelsInput = QLineEdit(new_dialog)
        self.numLabelsInput.setObjectName(u"numLabelsInput")
        self.numLabelsInput.setGeometry(QRect(540, 270, 113, 30))
        self.radio_label = QLabel(new_dialog)
        self.radio_label.setObjectName(u"radio_label")
        self.radio_label.setGeometry(QRect(10, 90, 431, 30))
        self.csv_radioButton = QRadioButton(new_dialog)
        self.csv_radioButton.setObjectName(u"csv_radioButton")
        self.csv_radioButton.setGeometry(QRect(20, 120, 701, 30))
        self.copy_radioButton = QRadioButton(new_dialog)
        self.copy_radioButton.setObjectName(u"copy_radioButton")
        self.copy_radioButton.setGeometry(QRect(20, 150, 711, 30))
        self.move_radioButton = QRadioButton(new_dialog)
        self.move_radioButton.setObjectName(u"move_radioButton")
        self.move_radioButton.setGeometry(QRect(20, 180, 721, 30))
        self.scroll_area = QScrollArea(new_dialog)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setGeometry(QRect(20, 250, 251, 281))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget = QWidget()
        self.scroll_area_widget.setObjectName(u"scroll_area_widget")
        self.scroll_area_widget.setGeometry(QRect(0, 0, 249, 279))
        self.scroll_area.setWidget(self.scroll_area_widget)

        self.retranslateUi(new_dialog)
        self.buttonBox.rejected.connect(new_dialog.reject)

        QMetaObject.connectSlotsByName(new_dialog)
    # setupUi

    def retranslateUi(self, new_dialog):
        new_dialog.setWindowTitle(QCoreApplication.translate("new_dialog", u"New", None))
        self.headline_folder.setText(QCoreApplication.translate("new_dialog", u"1. Select folder containing images you want to label", None))
        self.headline_num_labels.setText(QCoreApplication.translate("new_dialog", u"3. Specify labels", None))
        self.labels_inputs_description.setText(QCoreApplication.translate("new_dialog", u"How many unique labels you want to assign?", None))
        self.selected_folder_label.setText("")
        self.browse_button.setText(QCoreApplication.translate("new_dialog", u"Browse", None))
        self.confirm_num_labels.setText(QCoreApplication.translate("new_dialog", u"Confirm", None))
        self.radio_label.setText(QCoreApplication.translate("new_dialog", u"2. Select mode", None))
        self.csv_radioButton.setText(QCoreApplication.translate("new_dialog", u"csv (Images in selected folder are labeled and then csv file with assigned labels is &generated.)", None))
        self.copy_radioButton.setText(QCoreApplication.translate("new_dialog", u"cop&y (Creates folder for each label. Labeled images are copied to these folders. Csv is also generated)", None))
        self.move_radioButton.setText(QCoreApplication.translate("new_dialog", u"move (Creates folder for each &label. Labeled images are moved to these folders. Csv is also generated)", None))
    # retranslateUi

