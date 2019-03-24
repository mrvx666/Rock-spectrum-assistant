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
        self.pyqtgraph.setGeometry(QtCore.QRect(20, 20, 461, 320))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        self.pyqtgraph.setFont(font)
        self.pyqtgraph.setObjectName("pyqtgraph")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(500, 50, 411, 221))
        self.treeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeView.setAutoScroll(False)
        self.treeView.setObjectName("treeView")
        self.browsebutton = QtWidgets.QPushButton(self.centralwidget)
        self.browsebutton.setGeometry(QtCore.QRect(860, 20, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.browsebutton.setFont(font)
        self.browsebutton.setObjectName("browsebutton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(500, 20, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.clearbutton = QtWidgets.QPushButton(self.centralwidget)
        self.clearbutton.setGeometry(QtCore.QRect(780, 290, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.clearbutton.setFont(font)
        self.clearbutton.setObjectName("clearbutton")
        self.detailpoltcheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.detailpoltcheckbox.setGeometry(QtCore.QRect(500, 290, 145, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.detailpoltcheckbox.setFont(font)
        self.detailpoltcheckbox.setObjectName("detailpoltcheckbox")
        self.mousepointtrackingchechbox = QtWidgets.QCheckBox(self.centralwidget)
        self.mousepointtrackingchechbox.setGeometry(QtCore.QRect(610, 290, 145, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.mousepointtrackingchechbox.setFont(font)
        self.mousepointtrackingchechbox.setChecked(True)
        self.mousepointtrackingchechbox.setObjectName("mousepointtrackingchechbox")
        self.mousepointtrackinglabel = QtWidgets.QLabel(self.centralwidget)
        self.mousepointtrackinglabel.setGeometry(QtCore.QRect(510, 310, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mousepointtrackinglabel.setFont(font)
        self.mousepointtrackinglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mousepointtrackinglabel.setObjectName("mousepointtrackinglabel")
        self.searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.searchbutton.setGeometry(QtCore.QRect(800, 20, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.searchbutton.setFont(font)
        self.searchbutton.setObjectName("searchbutton")
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
        self.browsebutton.setText(_translate("MainWindow", "browse"))
        self.lineEdit.setText(_translate("MainWindow", "Working directory"))
        self.clearbutton.setText(_translate("MainWindow", "Clear"))
        self.detailpoltcheckbox.setText(_translate("MainWindow", "DetailPolt"))
        self.mousepointtrackingchechbox.setText(_translate("MainWindow", "MousePointTracking"))
        self.mousepointtrackinglabel.setText(_translate("MainWindow", "MousePoint"))
        self.searchbutton.setText(_translate("MainWindow", "search"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.About.setText(_translate("MainWindow", "About"))
        self.Help.setText(_translate("MainWindow", "Help"))


from pyqtgraph import PlotWidget
import apprcc_rc
