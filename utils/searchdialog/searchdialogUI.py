# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchdialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_searchdialog(object):
    def setupUi(self, searchdialog):
        searchdialog.setObjectName("searchdialog")
        searchdialog.resize(412, 340)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/image/JLUgeo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        searchdialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(searchdialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 392, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.searchbutton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.searchbutton.setObjectName("searchbutton")
        self.horizontalLayout.addWidget(self.searchbutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dirnamecheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.dirnamecheckbox.setChecked(True)
        self.dirnamecheckbox.setObjectName("dirnamecheckbox")
        self.horizontalLayout_2.addWidget(self.dirnamecheckbox)
        self.contentcheckbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.contentcheckbox.setObjectName("contentcheckbox")
        self.horizontalLayout_2.addWidget(self.contentcheckbox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(searchdialog)
        QtCore.QMetaObject.connectSlotsByName(searchdialog)

    def retranslateUi(self, searchdialog):
        _translate = QtCore.QCoreApplication.translate
        searchdialog.setWindowTitle(_translate("searchdialog", "RSA:search file"))
        self.searchbutton.setText(_translate("searchdialog", "search"))
        self.dirnamecheckbox.setText(_translate("searchdialog", "search include directory name"))
        self.contentcheckbox.setText(_translate("searchdialog", "search include file content"))


import apprcc_rc
