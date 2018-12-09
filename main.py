# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication,QTreeView,QFileSystemModel,QMenu
import PyQt5.QtCore as QtCore
import pyqtgraph as pg
from ui import Ui_MainWindow
import sys,os,time
import fileBrower

abspath = r"C:\Users\MrvX\Desktop\MSA\data"
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
        # pyqtgraph setting
        pg.setConfigOptions(antialias=True)  # 使曲线看起来更光滑，而不是锯齿状
        pg.setConfigOptions(leftButtonPan=False)
        #treeView右键菜单设置
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)

        self.model = QFileSystemModel()
        self.model.setRootPath(path)
        root = QTreeView(self.treeView)
        root.setModel(self.model)
        root.setRootIndex(self.model.index(path))


    def context_menu(self):
        menu = QMenu()
        open = menu.addAction("Open in new maya")
        open.triggered.connect(self.open_file)

        cursor = QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)


    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """

        self.pyqtgraph.clear() # 清空里面的内容，否则会发生重复绘图的结果

        #测试用示例数据
        data = fileBrower.openDataFile(testdata)
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
