# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'labeler_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_labeler_widget(object):
    def setupUi(self, labeler_widget):
        if not labeler_widget.objectName():
            labeler_widget.setObjectName(u"labeler_widget")
        labeler_widget.resize(800, 570)
        self.progress_bar = QLabel(labeler_widget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(10, 90, 421, 30))
        self.progress_bar.setFrameShape(QFrame.Box)
        self.next_im_btn = QPushButton(labeler_widget)
        self.next_im_btn.setObjectName(u"next_im_btn")
        self.next_im_btn.setGeometry(QRect(540, 50, 80, 30))
        self.generate_xlsx_checkbox = QCheckBox(labeler_widget)
        self.generate_xlsx_checkbox.setObjectName(u"generate_xlsx_checkbox")
        self.generate_xlsx_checkbox.setGeometry(QRect(120, 520, 181, 30))
        self.prev_im_btn = QPushButton(labeler_widget)
        self.prev_im_btn.setObjectName(u"prev_im_btn")
        self.prev_im_btn.setGeometry(QRect(450, 50, 80, 30))
        self.generate_csv_btn = QPushButton(labeler_widget)
        self.generate_csv_btn.setObjectName(u"generate_csv_btn")
        self.generate_csv_btn.setGeometry(QRect(10, 520, 100, 30))
        self.image_box = QLabel(labeler_widget)
        self.image_box.setObjectName(u"image_box")
        self.image_box.setGeometry(QRect(10, 140, 521, 371))
        self.image_box.setFrameShape(QFrame.Box)
        self.image_box.setScaledContents(True)
        self.show_next_checkbox = QCheckBox(labeler_widget)
        self.show_next_checkbox.setObjectName(u"show_next_checkbox")
        self.show_next_checkbox.setGeometry(QRect(450, 10, 341, 30))
        self.csv_note = QLabel(labeler_widget)
        self.csv_note.setObjectName(u"csv_note")
        self.csv_note.setGeometry(QRect(360, 520, 431, 30))
        self.img_name_label = QLabel(labeler_widget)
        self.img_name_label.setObjectName(u"img_name_label")
        self.img_name_label.setGeometry(QRect(10, 10, 421, 71))
        self.img_name_label.setFrameShape(QFrame.Box)
        self.img_name_label.setWordWrap(True)

        self.retranslateUi(labeler_widget)

        QMetaObject.connectSlotsByName(labeler_widget)
    # setupUi

    def retranslateUi(self, labeler_widget):
        labeler_widget.setWindowTitle(QCoreApplication.translate("labeler_widget", u"Labeler", None))
        self.progress_bar.setText("")
        self.next_im_btn.setText(QCoreApplication.translate("labeler_widget", u"Next", None))
        self.generate_xlsx_checkbox.setText(QCoreApplication.translate("labeler_widget", u"Also generate .xlsx file", None))
        self.prev_im_btn.setText(QCoreApplication.translate("labeler_widget", u"Prev", None))
        self.generate_csv_btn.setText(QCoreApplication.translate("labeler_widget", u"Generate csv", None))
        self.image_box.setText("")
        self.show_next_checkbox.setText(QCoreApplication.translate("labeler_widget", u"Automatically show next image when labeled", None))
        self.csv_note.setText(QCoreApplication.translate("labeler_widget", u"(csv will be also generated automatically after closing the app)", None))
        self.img_name_label.setText("")
    # retranslateUi

