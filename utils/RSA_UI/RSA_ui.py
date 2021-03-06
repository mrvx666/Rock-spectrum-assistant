# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RSA_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 390)
        MainWindow.setMinimumSize(QtCore.QSize(921, 390))
        MainWindow.setMaximumSize(QtCore.QSize(921, 390))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/image/JLUgeo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.pyqtgraph = PlotWidget(self.centralwidget)
        self.pyqtgraph.setGeometry(QtCore.QRect(20, 9, 461, 331))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.pyqtgraph.setFont(font)
        self.pyqtgraph.setObjectName("pyqtgraph")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(500, 10, 401, 331))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.searchbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.searchbutton.setFont(font)
        self.searchbutton.setObjectName("searchbutton")
        self.horizontalLayout_2.addWidget(self.searchbutton)
        self.browsebutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.browsebutton.setFont(font)
        self.browsebutton.setObjectName("browsebutton")
        self.horizontalLayout_2.addWidget(self.browsebutton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.treeView = QtWidgets.QTreeView(self.verticalLayoutWidget_2)
        self.treeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeView.setAutoScroll(False)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.crosshaircheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.crosshaircheckbox.setFont(font)
        self.crosshaircheckbox.setObjectName("crosshaircheckbox")
        self.verticalLayout.addWidget(self.crosshaircheckbox)
        self.showgridcheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.showgridcheckbox.setFont(font)
        self.showgridcheckbox.setChecked(True)
        self.showgridcheckbox.setObjectName("showgridcheckbox")
        self.verticalLayout.addWidget(self.showgridcheckbox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.clearbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.clearbutton.setFont(font)
        self.clearbutton.setObjectName("clearbutton")
        self.horizontalLayout.addWidget(self.clearbutton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 921, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuSetting = QtWidgets.QMenu(self.menuBar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menuBar)
        self.About = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.About.setFont(font)
        self.About.setObjectName("About")
        self.Help = QtWidgets.QAction(MainWindow)
        self.Help.setObjectName("Help")
        self.Notepad = QtWidgets.QAction(MainWindow)
        self.Notepad.setObjectName("Notepad")
        self.Findpeaks = QtWidgets.QAction(MainWindow)
        self.Findpeaks.setObjectName("Findpeaks")
        self.menuSetting.addAction(self.Findpeaks)
        self.menuSetting.addAction(self.Notepad)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.Help)
        self.menuSetting.addAction(self.About)
        self.menuBar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.browsebutton, self.treeView)
        MainWindow.setTabOrder(self.treeView, self.lineEdit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Spectrum Assistant"))
        self.pyqtgraph.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>根据选择数据绘出的结果图</p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "Working directory"))
        self.searchbutton.setText(_translate("MainWindow", "search"))
        self.browsebutton.setText(_translate("MainWindow", "browse"))
        self.crosshaircheckbox.setText(_translate("MainWindow", "Crosshair"))
        self.showgridcheckbox.setText(_translate("MainWindow", "ShowGrid"))
        self.clearbutton.setText(_translate("MainWindow", "Clear"))
        self.menuSetting.setTitle(_translate("MainWindow", "Modules"))
        self.About.setText(_translate("MainWindow", "About"))
        self.Help.setText(_translate("MainWindow", "Help"))
        self.Notepad.setText(_translate("MainWindow", "Notepad"))
        self.Findpeaks.setText(_translate("MainWindow", "Findpeaks"))


from pyqtgraph import PlotWidget
import apprcc_rc
