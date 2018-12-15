# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 386)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/图标/JLUgeo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pyqtgraph = PlotWidget(self.centralwidget)
        self.pyqtgraph.setGeometry(QtCore.QRect(20, 20, 375, 320))
        self.pyqtgraph.setObjectName("pyqtgraph")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(410, 280, 301, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.clearButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout.addWidget(self.clearButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(410, 50, 301, 221))
        self.treeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeView.setAutoScroll(False)
        self.treeView.setObjectName("treeView")
        self.browserButton = QtWidgets.QPushButton(self.centralwidget)
        self.browserButton.setGeometry(QtCore.QRect(660, 20, 51, 21))
        self.browserButton.setObjectName("browserButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(410, 20, 241, 21))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Spectrum Assistant"))
        self.pyqtgraph.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>根据选择数据绘出的结果图</p></body></html>"))
        self.checkBox_2.setText(_translate("MainWindow", "自动保存"))
        self.checkBox.setText(_translate("MainWindow", "自动载入"))
        self.clearButton.setText(_translate("MainWindow", "清空绘图"))
        self.browserButton.setText(_translate("MainWindow", "浏览"))

from pyqtgraph import PlotWidget
import apprcc_rc
