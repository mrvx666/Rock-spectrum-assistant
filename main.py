# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileSystemModel, QMenu, QMessageBox, QFileDialog
import PyQt5.QtCore as QtCore
from ui import Ui_MainWindow
import sys, os
import numpy as np

defaultpathname = "data"


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self._initUI()

    def _initUI(self, path=defaultpathname):
        self.setupUi(self)
        #初始化文件管理器
        self.model = QFileSystemModel()
        #设置工作目录
        self.changworkdir(path)
        #判断工作目录下data文件夹是否存在
        if os.path.exists(os.getcwd()+os.path.sep+defaultpathname):
            #存在，设置目录提示
            self.lineEdit.setText(os.getcwd()+os.path.sep+defaultpathname)
        else:
            #提示用户浏览目录
            reply = QMessageBox.warning(self, "温馨提示", "没有找到默认数据文件夹，是否浏览目录设置", QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)
            if (reply == QMessageBox.Yes):
                #设置工作目录
                self.on_browserButton_clicked()
            if (reply == QMessageBox.No):
                self.lineEdit.setText("请点击右侧按钮设置工作目录")

        #treeView右键菜单设置
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        #窗口置顶
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def changworkdir(self,path):
        self.model.setRootPath(path)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        # 更换目录做一次清空
        self.pyqtgraph.clear()

    def context_menu(self):
        menu = QMenu()
        open = menu.addAction("添加到绘图")
        open.triggered.connect(self.plotdatafile)
        cursor = QCursor()
        menu.exec_(cursor.pos())

    def plotdatafile(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        try:
            data = np.loadtxt(file_path, dtype=float, skiprows=1, usecols=1)
            self.pyqtgraph.plot(data)
        except:
            QMessageBox.warning(self, "警告", "你所选择的文件不是一个数据文件", QMessageBox.Yes, QMessageBox.Yes)

    @pyqtSlot()
    def on_clearButton_clicked(self):
        self.pyqtgraph.clear()

    @pyqtSlot()
    def on_browserButton_clicked(self):
        fileDialog = QFileDialog()
        fileDialog.setViewMode(QFileDialog.Detail)
        path = QFileDialog.getExistingDirectory(self, '请选择数据文件夹', os.environ['USERPROFILE'] + os.path.sep + 'desktop')
        self.lineEdit.setText(path)
        self.changworkdir(path)

    def closeEvent(self, QCloseEvent):
        #  推出程序确认,使用QMessageBox提示
        reply = QMessageBox.warning(self, "温馨提示", "即将退出, 确定？", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if (reply == QMessageBox.Yes):
            QCloseEvent.accept()
        if (reply == QMessageBox.No):
            QCloseEvent.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
