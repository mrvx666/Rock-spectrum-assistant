# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileSystemModel,QMenu
import PyQt5.QtCore as QtCore
from ui import Ui_MainWindow
import sys
import numpy as np

path = "./data/"
testdataname = "Test.txt"
testdata = path + testdataname


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self._initUI()

    def _initUI(self):
        print("_initUI process")
        self.setupUi(self)
        #初始化文件管理器
        self.model = QFileSystemModel()
        #设置工作目录
        self.model.setRootPath(path)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        #treeView右键菜单设置
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)

    def context_menu(self):
        menu = QMenu()
        open = menu.addAction("添加到绘图")
        open.triggered.connect(self.plotDataFile)
        clear = menu.addAction("清除绘图")
        clear.triggered.connect(self.clear)
        cursor = QCursor()
        menu.exec_(cursor.pos())

    def plotDataFile(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        data = self.openDataFile(file_path)
        self.pyqtgraph.plot(data)

    def openDataFile(self,filepath):
        return np.loadtxt(filepath, dtype=float, skiprows=1, usecols=1)

    def clear(self):
        #清空绘图区域内容
        self.pyqtgraph.clear()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """

        #测试用示例数据
        data = self.openDataFile(testdata)
        data1 = data-0.1

        #绘制图形曲线
        self.pyqtgraph.plot(data, pen="r")
        self.pyqtgraph.plot(data1, pen="b")

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.pyqtgraph.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
