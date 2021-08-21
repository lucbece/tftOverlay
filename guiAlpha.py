# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiAlpha.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 218)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 701, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.summonerLabel = QtWidgets.QLabel(self.horizontalGroupBox)
        self.summonerLabel.setObjectName("summonerLabel")
        self.horizontalLayout.addWidget(self.summonerLabel)
        self.summonerEntry = QtWidgets.QLineEdit(self.horizontalGroupBox)
        self.summonerEntry.setObjectName("summonerEntry")
        self.horizontalLayout.addWidget(self.summonerEntry)
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        self.horizontalGroupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.horizontalGroupBox_2.setObjectName("horizontalGroupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.regionLabel = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.regionLabel.setObjectName("regionLabel")
        self.horizontalLayout_2.addWidget(self.regionLabel, 0, QtCore.Qt.AlignLeft)
        self.regionList = QtWidgets.QComboBox(self.horizontalGroupBox_2)
        self.regionList.setObjectName("regionList")
        self.horizontalLayout_2.addWidget(self.regionList)
        self.verticalLayout.addWidget(self.horizontalGroupBox_2)
        self.searchSummonerButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.searchSummonerButton.setObjectName("searchSummonerButton")
        self.verticalLayout.addWidget(self.searchSummonerButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.summonerLabel.setBuddy(self.searchSummonerButton)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.summonerLabel.setText(_translate("MainWindow", "Summoner\'s name"))
        self.regionLabel.setText(_translate("MainWindow", "Region"))
        self.searchSummonerButton.setText(_translate("MainWindow", "Search Summoner"))
