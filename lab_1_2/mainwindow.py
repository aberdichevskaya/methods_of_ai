# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.get_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_file_button.setGeometry(QtCore.QRect(280, 30, 80, 22))
        self.get_file_button.setObjectName("get_file_button")
        self.recognize_button = QtWidgets.QPushButton(self.centralwidget)
        self.recognize_button.setGeometry(QtCore.QRect(280, 70, 80, 22))
        self.recognize_button.setObjectName("recognize_button")
        self.recognized_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.recognized_text.setGeometry(QtCore.QRect(30, 130, 104, 70))
        self.recognized_text.setReadOnly(True)
        self.recognized_text.setObjectName("recognized_text")
        self.translated_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.translated_text.setGeometry(QtCore.QRect(220, 130, 104, 70))
        self.translated_text.setReadOnly(True)
        self.translated_text.setObjectName("translated_text")
        self.translate_button = QtWidgets.QPushButton(self.centralwidget)
        self.translate_button.setGeometry(QtCore.QRect(280, 100, 80, 22))
        self.translate_button.setObjectName("translate_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.get_file_button.setText(_translate("MainWindow", "обзор"))
        self.recognize_button.setText(_translate("MainWindow", "распознать"))
        self.translate_button.setText(_translate("MainWindow", "Перевести"))
