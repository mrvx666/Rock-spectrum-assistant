# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(531, 266)
        aboutDialog.setMinimumSize(QtCore.QSize(531, 266))
        aboutDialog.setMaximumSize(QtCore.QSize(531, 266))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        aboutDialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/image/JLUgeo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutDialog.setWindowIcon(icon)
        self.closeButton = QtWidgets.QPushButton(aboutDialog)
        self.closeButton.setGeometry(QtCore.QRect(380, 200, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.picturelabel = QtWidgets.QLabel(aboutDialog)
        self.picturelabel.setGeometry(QtCore.QRect(0, 0, 284, 229))
        self.picturelabel.setText("")
        self.picturelabel.setPixmap(QtGui.QPixmap(":/image/image/鸽子楼.png"))
        self.picturelabel.setScaledContents(True)
        self.picturelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.picturelabel.setObjectName("picturelabel")
        self.geoicolabel = QtWidgets.QLabel(aboutDialog)
        self.geoicolabel.setGeometry(QtCore.QRect(360, 0, 100, 100))
        self.geoicolabel.setText("")
        self.geoicolabel.setPixmap(QtGui.QPixmap(":/image/image/院标(蓝).png"))
        self.geoicolabel.setScaledContents(True)
        self.geoicolabel.setAlignment(QtCore.Qt.AlignCenter)
        self.geoicolabel.setObjectName("geoicolabel")
        self.textlabel = QtWidgets.QLabel(aboutDialog)
        self.textlabel.setGeometry(QtCore.QRect(320, 140, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.textlabel.setFont(font)
        self.textlabel.setScaledContents(False)
        self.textlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.textlabel.setObjectName("textlabel")
        self.addresslabel = QtWidgets.QLabel(aboutDialog)
        self.addresslabel.setGeometry(QtCore.QRect(10, 240, 511, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.addresslabel.setFont(font)
        self.addresslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addresslabel.setObjectName("addresslabel")
        self.RSAtextlabel = QtWidgets.QLabel(aboutDialog)
        self.RSAtextlabel.setGeometry(QtCore.QRect(318, 110, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.RSAtextlabel.setFont(font)
        self.RSAtextlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RSAtextlabel.setObjectName("RSAtextlabel")
        self.geowebsiteButton = QtWidgets.QPushButton(aboutDialog)
        self.geowebsiteButton.setGeometry(QtCore.QRect(320, 170, 81, 21))
        self.geowebsiteButton.setObjectName("geowebsiteButton")
        self.projectgituhubButton = QtWidgets.QPushButton(aboutDialog)
        self.projectgituhubButton.setGeometry(QtCore.QRect(430, 170, 81, 21))
        self.projectgituhubButton.setObjectName("projectgituhubButton")

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "关于"))
        self.closeButton.setText(_translate("aboutDialog", "好的"))
        self.textlabel.setText(_translate("aboutDialog", "本程序由吉林大学地球科学学院开发"))
        self.addresslabel.setText(_translate("aboutDialog", "地址: 吉林省长春市建设街2199号   邮编:130061  电话:0431-88502278  传真:0431-88502055"))
        self.RSAtextlabel.setText(_translate("aboutDialog", "Rock Spectrum Assistant"))
        self.geowebsiteButton.setText(_translate("aboutDialog", "地球科学学院"))
        self.projectgituhubButton.setText(_translate("aboutDialog", "项目Github"))


import apprcc_rc
