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
        helpDialog.resize(574, 396)
        helpDialog.setMinimumSize(QtCore.QSize(574, 396))
        helpDialog.setMaximumSize(QtCore.QSize(574, 396))
        self.verticalLayoutWidget = QtWidgets.QWidget(helpDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 10, 271, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.textlabel.setFont(font)
        self.textlabel.setObjectName("textlabel")
        self.verticalLayout.addWidget(self.textlabel)
        self.QRcodelabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.QRcodelabel.setText("")
        self.QRcodelabel.setPixmap(QtGui.QPixmap(":/image/image/help_documentation_url-QRcode.png"))
        self.QRcodelabel.setScaledContents(True)
        self.QRcodelabel.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.QRcodelabel.setObjectName("QRcodelabel")
        self.verticalLayout.addWidget(self.QRcodelabel)
        self.open_help_documentation_url_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.open_help_documentation_url_Button.setFont(font)
        self.open_help_documentation_url_Button.setObjectName("open_help_documentation_url_Button")
        self.verticalLayout.addWidget(self.open_help_documentation_url_Button)
        self.closeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout.addWidget(self.closeButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(helpDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 261, 371))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/image/image/Author_QQ-QRcode.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self.retranslateUi(helpDialog)
        QtCore.QMetaObject.connectSlotsByName(helpDialog)

    def retranslateUi(self, helpDialog):
        _translate = QtCore.QCoreApplication.translate
        helpDialog.setWindowTitle(_translate("helpDialog", "RSA：帮助手册"))
        self.textlabel.setText(_translate("helpDialog", "需要帮助？\n"
"扫描二维码或点击按钮，打开RSA说明书"))
        self.open_help_documentation_url_Button.setText(_translate("helpDialog", "打开说明书（浏览器）"))
        self.closeButton.setText(_translate("helpDialog", "关闭"))
        self.label.setText(_translate("helpDialog", "需要支持？\n"
"扫描二维码，添加作者QQ获取帮助"))


import apprcc_rc
