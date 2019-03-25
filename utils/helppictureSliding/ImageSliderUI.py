# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageSliderUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageSlider(object):
    def setupUi(self, ImageSlider):
        ImageSlider.setObjectName("ImageSlider")
        ImageSlider.resize(656, 612)
        ImageSlider.setMinimumSize(QtCore.QSize(656, 612))
        ImageSlider.setMaximumSize(QtCore.QSize(656, 612))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/image/JLUgeo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ImageSlider.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(ImageSlider)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = SlidingStackedWidget(ImageSlider)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout.addWidget(self.stackedWidget)
        self.groupBox_4 = QtWidgets.QGroupBox(ImageSlider)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButtonPrev = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.horizontalLayout_4.addWidget(self.pushButtonPrev)
        self.pushButtonNext = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.horizontalLayout_4.addWidget(self.pushButtonNext)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.closeButton = QtWidgets.QPushButton(ImageSlider)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(ImageSlider)
        QtCore.QMetaObject.connectSlotsByName(ImageSlider)

    def retranslateUi(self, ImageSlider):
        _translate = QtCore.QCoreApplication.translate
        ImageSlider.setWindowTitle(_translate("ImageSlider", "帮助手册"))
        self.groupBox_4.setTitle(_translate("ImageSlider", "翻页"))
        self.pushButtonPrev.setText(_translate("ImageSlider", "上一页"))
        self.pushButtonNext.setText(_translate("ImageSlider", "下一页"))
        self.closeButton.setText(_translate("ImageSlider", "关闭"))


from utils.helppictureSliding.SlidingStackedWidget import SlidingStackedWidget
import apprcc_rc
