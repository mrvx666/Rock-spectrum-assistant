# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findpeaksdialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_findpeaksdialog(object):
    def setupUi(self, findpeaksdialog):
        findpeaksdialog.setObjectName("findpeaksdialog")
        findpeaksdialog.resize(440, 248)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/image/JLUgeo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        findpeaksdialog.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(findpeaksdialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 331, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.parameter1label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.parameter1label.setFont(font)
        self.parameter1label.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter1label.setObjectName("parameter1label")
        self.verticalLayout.addWidget(self.parameter1label)
        self.parameter1doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.parameter1doubleSpinBox.setSingleStep(0.01)
        self.parameter1doubleSpinBox.setObjectName("parameter1doubleSpinBox")
        self.verticalLayout.addWidget(self.parameter1doubleSpinBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.parameter2label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.parameter2label.setFont(font)
        self.parameter2label.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter2label.setObjectName("parameter2label")
        self.verticalLayout_5.addWidget(self.parameter2label)
        self.parameter2doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.parameter2doubleSpinBox.setSingleStep(0.01)
        self.parameter2doubleSpinBox.setObjectName("parameter2doubleSpinBox")
        self.verticalLayout_5.addWidget(self.parameter2doubleSpinBox)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.parameter3label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.parameter3label.setFont(font)
        self.parameter3label.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter3label.setObjectName("parameter3label")
        self.verticalLayout_6.addWidget(self.parameter3label)
        self.parameter3doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.parameter3doubleSpinBox.setSingleStep(0.01)
        self.parameter3doubleSpinBox.setObjectName("parameter3doubleSpinBox")
        self.verticalLayout_6.addWidget(self.parameter3doubleSpinBox)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.parameter4label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        self.parameter4label.setFont(font)
        self.parameter4label.setAlignment(QtCore.Qt.AlignCenter)
        self.parameter4label.setObjectName("parameter4label")
        self.verticalLayout_7.addWidget(self.parameter4label)
        self.parameter4doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.parameter4doubleSpinBox.setSingleStep(0.01)
        self.parameter4doubleSpinBox.setObjectName("parameter4doubleSpinBox")
        self.verticalLayout_7.addWidget(self.parameter4doubleSpinBox)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(findpeaksdialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(350, 20, 81, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.findpeaksbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.findpeaksbutton.setObjectName("findpeaksbutton")
        self.verticalLayout_3.addWidget(self.findpeaksbutton)
        self.helpbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.helpbutton.setObjectName("helpbutton")
        self.verticalLayout_3.addWidget(self.helpbutton)
        self.clearbutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.clearbutton.setObjectName("clearbutton")
        self.verticalLayout_3.addWidget(self.clearbutton)
        self.closebutton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.closebutton.setObjectName("closebutton")
        self.verticalLayout_3.addWidget(self.closebutton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(findpeaksdialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 120, 331, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.peakmarkcheckbox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.peakmarkcheckbox.setChecked(True)
        self.peakmarkcheckbox.setObjectName("peakmarkcheckbox")
        self.horizontalLayout_2.addWidget(self.peakmarkcheckbox)
        self.peaktextchebox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.peaktextchebox.setObjectName("peaktextchebox")
        self.horizontalLayout_2.addWidget(self.peaktextchebox)
        self.textEdit = QtWidgets.QTextEdit(findpeaksdialog)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(10, 150, 421, 81))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(findpeaksdialog)
        QtCore.QMetaObject.connectSlotsByName(findpeaksdialog)

    def retranslateUi(self, findpeaksdialog):
        _translate = QtCore.QCoreApplication.translate
        findpeaksdialog.setWindowTitle(_translate("findpeaksdialog", "RSA:Findpeaks"))
        self.comboBox.setItemText(0, _translate("findpeaksdialog", "detect_peaks"))
        self.comboBox.setItemText(1, _translate("findpeaksdialog", "Janko_Slavic_findpeaks"))
        self.comboBox.setItemText(2, _translate("findpeaksdialog", "tony_beltramelli_detect_peaks"))
        self.parameter1label.setText(_translate("findpeaksdialog", "parameter1"))
        self.parameter2label.setText(_translate("findpeaksdialog", "parameter2"))
        self.parameter3label.setText(_translate("findpeaksdialog", "parameter3"))
        self.parameter4label.setText(_translate("findpeaksdialog", "parameter4"))
        self.findpeaksbutton.setText(_translate("findpeaksdialog", "findpeaks"))
        self.helpbutton.setText(_translate("findpeaksdialog", "help"))
        self.clearbutton.setText(_translate("findpeaksdialog", "clear"))
        self.closebutton.setText(_translate("findpeaksdialog", "close"))
        self.peakmarkcheckbox.setText(_translate("findpeaksdialog", "peak mark"))
        self.peaktextchebox.setText(_translate("findpeaksdialog", "peak text"))
        self.textEdit.setHtml(_translate("findpeaksdialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">peaks index and peaks values will show here. </span></p></body></html>"))


import apprcc_rc
