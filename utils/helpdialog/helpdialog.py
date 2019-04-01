# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpdialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpDialog(object):
    def setupUi(self, helpDialog):
        helpDialog.setObjectName("helpDialog")
        helpDialog.resize(304, 383)
        helpDialog.setMinimumSize(QtCore.QSize(304, 383))
        helpDialog.setMaximumSize(QtCore.QSize(304, 383))
        self.verticalLayoutWidget = QtWidgets.QWidget(helpDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 282, 356))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textlabel.setFont(font)
        self.textlabel.setObjectName("textlabel")
        self.verticalLayout.addWidget(self.textlabel)
        self.QRcodelabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.QRcodelabel.setText("")
        self.QRcodelabel.setPixmap(QtGui.QPixmap(":/image/image/help_documentation_url-QRcode.png"))
        self.QRcodelabel.setObjectName("QRcodelabel")
        self.verticalLayout.addWidget(self.QRcodelabel)
        self.open_help_documentation_url_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_help_documentation_url_Button.setObjectName("open_help_documentation_url_Button")
        self.verticalLayout.addWidget(self.open_help_documentation_url_Button)
        self.closeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)

        self.retranslateUi(helpDialog)
        QtCore.QMetaObject.connectSlotsByName(helpDialog)

    def retranslateUi(self, helpDialog):
        _translate = QtCore.QCoreApplication.translate
        helpDialog.setWindowTitle(_translate("helpDialog", "RSA：帮助手册"))
        self.textlabel.setText(_translate("helpDialog", "需要帮助？\n"
"扫描二维码或点击按钮，打开RSA说明书"))
        self.open_help_documentation_url_Button.setText(_translate("helpDialog", "打开说明书（浏览器）"))
        self.closeButton.setText(_translate("helpDialog", "关闭"))


import apprcc_rc
