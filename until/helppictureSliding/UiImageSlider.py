# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiImageSlider.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(656, 612)
        Form.setMinimumSize(QtCore.QSize(656, 612))
        Form.setMaximumSize(QtCore.QSize(656, 612))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/image/JLUgeo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = SlidingStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout.addWidget(self.stackedWidget)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
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
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "帮助手册"))
        self.groupBox_4.setTitle(_translate("Form", "翻页"))
        self.pushButtonPrev.setText(_translate("Form", "上一页"))
        self.pushButtonNext.setText(_translate("Form", "下一页"))
        self.closeButton.setText(_translate("Form", "关闭"))

from until.helppictureSliding.SlidingStackedWidget import SlidingStackedWidget
import apprcc_rc
