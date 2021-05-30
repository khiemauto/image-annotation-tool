# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(800, 650)
        self.action_new = QAction(main_window)
        self.action_new.setObjectName(u"action_new")
        self.action_open = QAction(main_window)
        self.action_open.setObjectName(u"action_open")
        self.action_about = QAction(main_window)
        self.action_about.setObjectName(u"action_about")
        self.action_quit = QAction(main_window)
        self.action_quit.setObjectName(u"action_quit")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(main_window)
        self.toolBar.setObjectName(u"toolBar")
        main_window.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.action_new)
        self.menuFile.addAction(self.action_open)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.menuHelp.addAction(self.action_about)
        self.toolBar.addAction(self.action_new)
        self.toolBar.addAction(self.action_open)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"Annotation tool", None))
        self.action_new.setText(QCoreApplication.translate("main_window", u"&New", None))
        self.action_open.setText(QCoreApplication.translate("main_window", u"&Open", None))
        self.action_about.setText(QCoreApplication.translate("main_window", u"&About", None))
        self.action_quit.setText(QCoreApplication.translate("main_window", u"&Quit", None))
        self.menuFile.setTitle(QCoreApplication.translate("main_window", u"Fi&le", None))
        self.menuHelp.setTitle(QCoreApplication.translate("main_window", u"&Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("main_window", u"toolBar", None))
    # retranslateUi

