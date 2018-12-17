# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileSystemModel,\
                            QMenu, QMessageBox, QFileDialog, QInputDialog, QLineEdit
import PyQt5.QtCore as QtCore
import sys
import os
import subprocess
import numpy as np
from ui import Ui_MainWindow
from callaboutdialog import aboutDialogUI

defaultpathname = "data"
defaultdataformat = ".txt"
testdata = "Wavelength	XK1Y08-100000.asd\n" \
           "350	 0.068295808533771 \n" \
           "351	 6.88503984835842E-02 \n" \
           "353	 6.96586664904809E-02 "


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        # 初始化工作目录
        self.workdir = os.getcwd() + os.sep + defaultpathname
        # 初始化文件指针
        self.fileindex = self.workdir
        self._initUI()
        self.plotcount = 0
        self.plotlimit = 5

    def _initUI(self, path=defaultpathname):
        # 载入UI.py
        self.setupUi(self)
        # 初始化文件管理器
        self.model = QFileSystemModel()
        # 设置工作目录
        self.changworkdir(path)
        # 判断工作目录下data文件夹是否存在
        if os.path.exists(self.workdir):
            # 存在，设置路径提示文本框
            self.lineEdit.setText(self.workdir)
        else:
            # 不存在，提示用户希望进行的操作
            reply = QMessageBox.warning(self, "温馨提示", "没有找到默认数据文件夹，是否浏览目录设置", QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.Yes)
            if (reply == QMessageBox.Yes):
                # 用户点击Yes，设置工作目录,模拟用户点击浏览按钮
                self.on_browserButton_clicked()
            if (reply == QMessageBox.No):
                # 用户点击No，设置提示
                self.lineEdit.setText("请点击右侧按钮设置工作目录")

        # 菜单栏关联子窗体
        self.aboutwin = aboutDialogUI()
        self.About.triggered.connect(self.about)

        # treeView右键菜单关联
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        # 窗口置顶
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def changworkdir(self, path):
        # 设置treeview工作目录，代码顺序不能颠倒
        self.model.setRootPath(path)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        # 重设工作目录
        self.workdir = self.model.rootPath()
        self.lineEdit.setText(self.workdir)
        # 更换目录做一次清空
        self.pyqtgraph.clear()

    def context_menu(self):
        # 设定鼠标点击位置的指针
        index = self.treeView.currentIndex()
        self.fileindex = self.model.filePath(index)

        # 添加右键菜单
        menu = QMenu()

        plot = menu.addAction("plot")
        plot.triggered.connect(self.plotdatafile)
        addfile = menu.addAction("addfile")
        addfile.triggered.connect(self.addfile)
        editfile = menu.addAction("editfile")
        editfile.triggered.connect(self.editfile)
        removefile = menu.addAction("removefile")
        removefile.triggered.connect(self.removefile)

        cursor = QCursor()
        menu.exec_(cursor.pos())

    def plotdatafile(self):
        # 绘图板上图形过多，提示用户
        if self.plotcount >= self.plotlimit:
            QMessageBox.warning(self, "温馨提示", "绘图板上已经超过" + str(self.plotlimit) + "个图形，过多绘图会导致无法分辨，请清除绘图板", QMessageBox.Yes, QMessageBox.Yes)

        try:
            # 载入数据，绘图
            data = np.loadtxt(self.fileindex, dtype=float, skiprows=1, usecols=1)
            self.pyqtgraph.plot(data)
            # 在状态栏上显示当前绘图的文件和绘图总数
            self.statusbar.showMessage("plot " + self.fileindex.lstrip(self.workdir) + " ，当前绘图总数 " + str(self.plotcount+1))
            self.plotcount += 1
        except:
            QMessageBox.critical(self, "警告", "文件打开失败\n请检查数据格式", QMessageBox.Yes, QMessageBox.Yes)

    def addfile(self):
        # 如果文件指针为空，赋值到当前工作目录，防止用户点击顶级目录空白处无法正常addfile
        if self.fileindex == '':
            self.fileindex = self.workdir

        # 弹出对话框，获取文件名；按下ok，okPressed为真
        filename, okPressed = QInputDialog.getText(self, "文件名", "请输入文件名:", QLineEdit.Normal)
        fullfilename = filename + defaultdataformat

        # 这里默认文件指针指向的是一个目录，拼出完整文件路径
        fullfilepath = self.fileindex + os.path.sep + fullfilename

        # 判断文件是否已经存在，如果已经存在就在方法内部处理
        isfileexists = self.fileexists(fullfilepath)
        if not isfileexists:

            # 文件不存在，那么文件指针所指向的是一个文件吗？
            if os.path.isfile(self.fileindex):
                # 指针位置是一个文件，获取文件所在目录，修改路径
                fullfilepath = os.path.dirname(self.fileindex) + os.path.sep + fullfilename
                # 修改目录后，用户指定的文件名是否已经存在？如果已经存在就在方法内部处理
                isfileexists = self.fileexists(fullfilepath)

        # 文件名不为空,用户指定文件不存在，可以执行写入操作
        if okPressed and filename != '' and not isfileexists:
            self.statusbar.showMessage("add " + self.fileindex.lstrip(self.workdir) + os.sep + fullfilename)
            self.writedatatofile(fullfilepath)

        # 文件名为空，提示用户
        elif filename == '':
            QMessageBox.warning(self, "温馨提示", "未输入文件名", QMessageBox.Yes, QMessageBox.Yes)

    def fileexists(self, filepath):
        # 从传入文件指针获取文件名
        (path, filename) = os.path.split(filepath)

        if os.path.exists(filepath):
            # 文件存在，询问用户希望的操作模式
            reply = QMessageBox.warning(self, "温馨提示", filename + "文件在目录\n" + path + "\n已经存在，是否进入编辑模式",
                                        QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            if (reply == QMessageBox.Yes):
                # 用户点击Yes，进入编辑模式
                self.editdatafile(filepath)
            if (reply == QMessageBox.No):
                # 用户点击No，什么也不做
                pass
            self.statusbar.showMessage(self.fileindex.lstrip(self.workdir) + "文件已存在")
            return True

        return False

    def writedatatofile(self, filepath):
        # 弹出提示框让用户输入数据
        data, ok = QInputDialog.getMultiLineText(self, "请输入数据", "请按照示例数据格式输入：", testdata)
        # 用户按下了ok，不按的话不写入数据
        if ok:

            # 检测用户是否完全没有修改数据，同示例数据一样
            if data == testdata:
                reply = QMessageBox.warning(self, "温馨提示", "未检测到数据修改，是否继续写入？",
                                            QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.No)

                if (reply == QMessageBox.Yes):
                    # 用户点击Yes，将示例数据写入到文件
                    try:
                        f = open(filepath, "w")
                        f.write(data)
                        f.close()
                        self.statusbar.showMessage("write " + filepath.strip(self.workdir) + "写入成功")
                    except IOError as e:
                        QMessageBox.critical(self, "警告", e, QMessageBox.Yes, QMessageBox.Yes)

                if (reply == QMessageBox.No):
                    # 用户点击No，什么也不做
                    pass

    def editfile(self):
        if os.path.isdir(self.fileindex):
            # 打开的是一个目录而不是一个文件时提示用户
            QMessageBox.warning(self, "温馨提示", "请选择一个数据文件", QMessageBox.Yes, QMessageBox.Yes)
        elif os.path.isfile(self.fileindex):
            self.editdatafile(self.fileindex)

    def editdatafile(self, filepath):
        self.statusbar.showMessage("edit " + self.fileindex.lstrip(self.workdir))
        # 这里本来是使用os.system()来启动notepad，但是pyinstall打包后运行这段代码会弹出一个dos窗口，所以做此修改
        try:
            subprocess.call("notepad " + filepath, shell=True)
        except Exception as e:
            QMessageBox.critical(self, "警告", e, QMessageBox.Yes, QMessageBox.Yes)

    def removefile(self):
        if os.path.isdir(self.fileindex):
            QMessageBox.warning(self, "温馨提示", "您所选择的是一个文件夹\n出于数据安全考虑\n本程序不提供删除文件夹功能", QMessageBox.Yes, QMessageBox.Yes)
        elif os.path.isfile(self.fileindex):
            (filepath, filename) = os.path.split(self.fileindex)
            reply = QMessageBox.warning(self, "温馨提示", "是否确定删除文件"+filename,
                                        QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            if (reply == QMessageBox.Yes):
                # 用户点击Yes，删除文件
                os.remove(self.fileindex)
                self.statusbar.showMessage("remove  " + self.fileindex.lstrip(self.workdir))
            if (reply == QMessageBox.No):
                pass

    @pyqtSlot()
    def on_clearButton_clicked(self):
        self.pyqtgraph.clear()
        self.plotcount = 0

    @pyqtSlot()
    def on_browserButton_clicked(self):
        fileDialog = QFileDialog()
        fileDialog.setViewMode(QFileDialog.Detail)
        path = QFileDialog.getExistingDirectory(self, '请选择数据文件夹', os.environ['USERPROFILE'] + os.path.sep + 'desktop')
        self.changworkdir(path)
        self.lineEdit.setText(path)
        self.statusbar.showMessage("change work dir  " + path)

    def about(self):
        self.aboutwin.show()

    def closeEvent(self, QCloseEvent):
        # 退出程序确认,使用QMessageBox提示
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
