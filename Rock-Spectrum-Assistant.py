# -*- coding: utf-8 -*-

"""
这是RSA的主窗体，主要的业务都在这里完成。
"""
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileSystemModel,\
                            QMenu, QMessageBox, QFileDialog, QInputDialog, QLineEdit
import sys
import os
import subprocess
import numpy as np

from ui import Ui_MainWindow
from callaboutdialog import aboutDialogUI
from helppictureSliding import ImageSliderWidget

defaultpathname = "data"
defaultdataformat = ".txt"
testdata = "Wavelength	XK1Y08-100000.asd\n" \
           "350	 0.068295808533771 \n" \
           "351	 6.88503984835842E-02 \n" \
           "353	 6.96586664904809E-02 "
color = ('b', 'c', 'g', 'w', 'm', 'r', 'y', 'k', )


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        # 初始化工作目录
        self.workdir = os.getcwd() + os.sep + defaultpathname

        # 初始化文件指针
        self.fileindex = self.workdir

        # 初始化子窗口错误提示，正常载入不会用到
        self.childwinerror = ''
        self.plotcount = 0
        self.plotlimit = 5

        # 初始化UI
        self._initUI()

        # 初始化文件管理器
        self.model = QFileSystemModel()

        # 判断程序所在目录下data文件夹是否存在
        if os.path.isdir(self.workdir):
            # 存在，设置路径提示文本框
            self.lineEdit.setText(self.workdir)
        else:
            # 不存在，提示用户希望进行的操作
            reply = QMessageBox.question(self, "温馨提示", "没有找到默认数据文件夹，是否浏览目录设置", QMessageBox.Yes | QMessageBox.Cancel,
                                        QMessageBox.Cancel)
            if (reply == QMessageBox.Yes):
                # 用户点击Yes，设置工作目录,模拟用户点击浏览按钮
                self.on_browseButton_clicked()
            if (reply == QMessageBox.Cancel):
                # 用户点击No，设置提示
                self.lineEdit.setText("Click the right side button to set work dir")

        # 设置工作目录
        self.changworkdir(self.workdir)

        if self.childwinerror == '':
            self.statusbar.showMessage("Welcome to Rock Spectrum Assistant")
        # 提示用户子窗体因为各种理由gg
        else:
            self.statusbar.showMessage(self.childwinerror)

    def _initUI(self):
        # 载入UI.py
        self.setupUi(self)

        # 载入子窗体
        try:
            self.aboutwin = aboutDialogUI()
            self.About.triggered.connect(self.aboutthisprogram)

            self.helpwin = ImageSliderWidget()
            self.Help.triggered.connect(self.helpmanual)
        # 当子窗体因为各种理由gg了，确保主窗体可以正常启动
        except:
            self.childwinerror = "child window initialization failed"

        # treeView右键菜单关联
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        # 窗口置顶
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def changworkdir(self, path):
        # 设置treeview工作目录，代码顺序不能颠倒
        self.model.setRootPath(path)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        # 重设工作目录
        self.workdir = self.model.rootPath()
        # 更换目录做一次清空
        self.on_clearButton_clicked()

    def context_menu(self):
        # 设定鼠标点击位置的指针
        index = self.treeView.currentIndex()
        self.fileindex = self.model.filePath(index)

        # 添加右键菜单
        menu = QMenu()

        plot = menu.addAction("plot")
        plot.triggered.connect(self.plotdatafile)
        addfile = menu.addAction("add")
        addfile.triggered.connect(self.addfile)
        editfile = menu.addAction("edit")
        editfile.triggered.connect(self.editfile)
        removefile = menu.addAction("remove")
        removefile.triggered.connect(self.removefile)

        cursor = QCursor()
        menu.exec_(cursor.pos())

    def plotdatafile(self):
        # 绘图板上图形过多，提示用户
        if self.plotcount == self.plotlimit:
            QMessageBox.information(self, "温馨提示", "绘图板上已经超过" + str(self.plotlimit) + "个图形，过多绘图会导致无法分辨，请清除绘图板", QMessageBox.Close, QMessageBox.Close)

        # 选取画笔颜色，防止溢出
        colorindex = self.plotcount
        if self.plotcount > len(color)-1:
            colorindex = self.plotcount % len(color)-1

        # 判断是文件指针指向的是一个目录还是文件
        if os.path.isdir(self.fileindex) or self.fileindex == "":
            # 指向一个目录，提示用户
            QMessageBox.information(self, "温馨提示", "请选择一个数据文件", QMessageBox.Close, QMessageBox.Close)

        elif os.path.isfile(self.fileindex):
            # 指向一个文件，尝试读取数据
            try:
                # 载入数据，如果数据格式有变化这里会报错
                data = np.loadtxt(self.fileindex, dtype=float, skiprows=1, usecols=1)
                # 绘图
                self.pyqtgraph.plot(data, pen=color[colorindex])
                # 在状态栏上显示当前绘图的文件和绘图总数
                self.statusbar.showMessage("plot " + self.fileindex.lstrip(self.workdir)
                                           + " ，当前绘图总数 " + str(self.plotcount + 1))
                self.plotcount += 1
            except:
                QMessageBox.information(self, "警告", "文件打开失败\n请检查数据格式", QMessageBox.Close, QMessageBox.Close)

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
        elif okPressed and filename == '':
            QMessageBox.information(self, "温馨提示", "未输入文件名", QMessageBox.Close, QMessageBox.Close)

    def fileexists(self, filepath):
        # 从传入文件路径获取文件名
        (path, filename) = os.path.split(filepath)

        if os.path.exists(filepath):
            # 文件存在，询问用户希望的操作模式
            reply = QMessageBox.question(self, "温馨提示", filename + "文件在目录\n" + path + "\n已经存在，是否进入编辑模式",
                                        QMessageBox.Yes | QMessageBox.Cancel,
                                        QMessageBox.Cancel)
            if (reply == QMessageBox.Yes):
                # 用户点击Yes，进入编辑模式
                self.editdatafile(filepath)
            if (reply == QMessageBox.Cancel):
                # 用户点击No，什么也不做
                pass
            self.statusbar.showMessage(self.fileindex.lstrip(self.workdir) + filename + " 文件已存在")
            return True

        return False

    def writedatatofile(self, filepath):
        # 弹出提示框让用户输入数据
        data, ok = QInputDialog.getMultiLineText(self, "请输入数据", "请按照示例数据格式输入：", testdata)
        # 用户按下了ok，不按的话不写入数据
        if ok:
            try:
                f = open(filepath, "w")
                f.write(data)
                f.close()
                self.statusbar.showMessage("write " + filepath.lstrip(self.workdir) + " 写入成功")
            except IOError as e:
                QMessageBox.critical(self, "警告", e, QMessageBox.Close, QMessageBox.Close)

    def editfile(self):
        if os.path.isdir(self.fileindex):
            # 打开的是一个目录而不是一个文件时提示用户
            QMessageBox.information(self, "温馨提示", "请选择一个数据文件", QMessageBox.Close, QMessageBox.Close)
        elif os.path.isfile(self.fileindex):
            self.editdatafile(self.fileindex)

    def editdatafile(self, filepath):
        self.statusbar.showMessage("edit " + self.fileindex.lstrip(self.workdir))
        # 这里本来是使用os.system()来启动notepad，但是pyinstall打包后运行这段代码会弹出一个dos窗口，所以做此修改
        try:
            subprocess.call("notepad " + filepath, shell=True)
        except Exception as e:
            QMessageBox.critical(self, "警告", e, QMessageBox.Close, QMessageBox.Close)

    def removefile(self):
        if os.path.isdir(self.fileindex):
            QMessageBox.question(self, "温馨提示", "您所选择的是一个文件夹\n出于数据安全考虑\n本程序不提供删除文件夹功能", QMessageBox.Close, QMessageBox.Close)
        elif os.path.isfile(self.fileindex):
            (filepath, filename) = os.path.split(self.fileindex)
            reply = QMessageBox.warning(self, "温馨提示", "是否确定删除文件"+filename,
                                        QMessageBox.Yes | QMessageBox.Cancel,
                                        QMessageBox.Cancel)
            if (reply == QMessageBox.Yes):
                # 用户点击Yes，删除文件
                os.remove(self.fileindex)
                self.statusbar.showMessage("remove  " + self.fileindex.lstrip(self.workdir))
            if (reply == QMessageBox.Cancel):
                pass

    @pyqtSlot()
    def on_clearButton_clicked(self):
        self.pyqtgraph.clear()
        self.plotcount = 0
        self.statusbar.showMessage("clear plotwidget ")

    @pyqtSlot()
    def on_browseButton_clicked(self):
            fileDialog = QFileDialog()
            fileDialog.setViewMode(QFileDialog.Detail)
            path = QFileDialog.getExistingDirectory(self, '请选择数据文件夹', os.environ['USERPROFILE'] + os.path.sep + 'desktop')
            self.changworkdir(path)
            self.lineEdit.setText(path)
            self.statusbar.showMessage("change work dir to " + path)

    def aboutthisprogram(self):
        self.aboutwin.show()
        self.statusbar.showMessage("about this program")

    def helpmanual(self):
        self.helpwin.show()
        self.helpwin.autoStart()
        self.statusbar.showMessage("start help manual")

    def closeEvent(self, QCloseEvent):
        # 退出程序确认,使用QMessageBox提示
        reply = QMessageBox.warning(self, "温馨提示", "即将退出, 确定？", QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Yes)
        if (reply == QMessageBox.Yes):
            QCloseEvent.accept()
        if (reply == QMessageBox.Cancel):
            QCloseEvent.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
