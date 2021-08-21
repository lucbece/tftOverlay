# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'overlay.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 97)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.leagueImage = QtWidgets.QGraphicsView(self.centralwidget)
        self.leagueImage.setGeometry(QtCore.QRect(340, 10, 61, 61))
        self.leagueImage.setObjectName("leagueImage")
        self.leagueText = QtWidgets.QLabel(self.centralwidget)
        self.leagueText.setGeometry(QtCore.QRect(10, 10, 281, 61))
        self.leagueText.setText("")
        self.leagueText.setObjectName("leagueText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
