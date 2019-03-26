# -*- coding: utf-8 -*-

"""
这是RSA的主窗体，主要的业务都在这里完成。
"""
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileSystemModel,\
                            QMenu, QMessageBox, QFileDialog, QInputDialog, QLineEdit
import os
import subprocess
import pyqtgraph as pg

from utils import *

color = ('b', 'c', 'g', 'w', 'm', 'r', 'y', 'k')


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)

        # 初始化工作目录
        self.workdir = os.getcwd() + os.sep + get_default_workdir()

        # 初始化UI
        self._initUI()

        # 初始化文件管理器
        self.model = QFileSystemModel()

        # 获取pyqtgraph绘图对象
        self.plotItem = self.pyqtgraph.getPlotItem()

        self.plotcount = 0

        # 判断程序所在目录下data文件夹是否存在
        if os.path.isdir(self.workdir):
            # 存在，设置路径提示文本框
            self.lineEdit.setText(self.workdir)
            # 设置工作目录
            self.changworkdir(self.workdir)
        else:
            # 不存在，提示用户希望进行的操作
            reply = QMessageBox.question(self, "温馨提示", "没有找到默认数据文件夹，是否浏览目录设置",
                                         QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                # 用户点击Yes，设置工作目录,模拟用户点击浏览按钮
                try:
                    self.on_browsebutton_clicked()
                except:
                    self.lineEdit.setText("Click the right side button to set work directory")
            if reply == QMessageBox.Cancel:
                # 用户点击No，设置提示
                self.lineEdit.setText("Click the right side button to set work directory")

        # 状态栏提示欢迎语
        self.statusbar.showMessage("RSA:Welcome to Rock-Spectrum-Assistant")

        # 唤醒窗口，把窗口提到最前方
        self.raise_()

    def _initUI(self):
        # 载入UI.py
        self.setupUi(self)

        # 载入子窗体
        self.aboutwin = aboutDialog()
        self.Help.triggered.connect(self.helpmanual)
        self.helpwin = ImageSliderWidget()
        self.About.triggered.connect(self.aboutthisprogram)
        self.searchdialog = searchdialog(self.workdir)
        # 把搜索子窗体双击事件连接到RSA主窗体进行处理
        self.searchdialog.listWidget.itemDoubleClicked.connect(self.searchdialogitemdoubleclicked)

        # treeView右键菜单关联
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)

        # 绘图板鼠标追踪鼠标跟踪
        self.pyqtgraph.setMouseTracking(True)
        self.pyqtgraph.scene().sigMouseMoved.connect(self.mouseMoved)

    def changworkdir(self, path, isdialogparent=False):
        # 设置treeview工作目录，代码顺序不能颠倒
        self.model.setRootPath(path)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        # 重设工作目录
        self.workdir = self.model.rootPath()
        # 更换目录做一次清空,仅限不是由子窗口调用的时候
        if not isdialogparent:
            self.on_clearbutton_clicked()

    def context_menu(self):

        # 设定鼠标点击位置的指针
        index = self.treeView.currentIndex()
        self.mouseindex = self.model.filePath(index)

        # 添加右键菜单
        menu = QMenu()

        plotfile = menu.addAction("plot")
        plotfile.triggered.connect(self.plotfile)
        addfile = menu.addAction("add")
        addfile.triggered.connect(self.addfile)
        editfile = menu.addAction("edit")
        editfile.triggered.connect(self.editfile)
        removefile = menu.addAction("remove")
        removefile.triggered.connect(self.removefile)

        cursor = QCursor()
        menu.exec_(cursor.pos())

    def plotfile(self):
        # 绘图板上图形过多，提示用户
        if self.plotcount == get_plot_limit():
            QMessageBox.information(self, "温馨提示", "绘图板上已经超过" + str(get_plot_limit()) + "个图形，过多绘图会导致无法分辨，请清除绘图板", QMessageBox.Close, QMessageBox.Close)

        # 判断是文件指针指向的是一个目录还是文件
        if os.path.isdir(self.mouseindex) or self.mouseindex == "":
            # 指向一个目录，提示用户
            QMessageBox.information(self, "温馨提示", "请选择一个数据文件", QMessageBox.Close, QMessageBox.Close)

            # 指向一个文件，尝试读取数据
        elif os.path.isfile(self.mouseindex):

            try:
                self.plot(self.mouseindex)

            # 捕获异常
            except Exception as e:
                QMessageBox.information(self, "警告", "文件打开失败\n请检查数据格式\n{}".format(e), QMessageBox.Close, QMessageBox.Close)
                self.statusbar.showMessage("RSA:please check the data file format")

    def plot(self, file):
        # 选取画笔颜色，防止溢出
        colorindex = self.plotcount
        if self.plotcount > len(color) - 1:
            colorindex = self.plotcount % len(color) - 1

        # 载入数据，如果数据格式有变化这里会报错
        self.y_data = load_data(file)

        # 将数据表索引（波长）转换为绘图时的坐标轴数据
        self.x_dict = dict(enumerate(self.y_data.index))
        axis_x_data = [(i, list(self.y_data.index)[i]) for i in range(0, len(self.y_data.index), get_ticks_spacing())]
        stringaxis = self.plotItem.getAxis(name='bottom')
        stringaxis.setTicks([axis_x_data, self.x_dict.items()])
        self.pyqtgraph.plot(x=list(self.x_dict.keys()), y=self.y_data.iloc[:, 0].values, pen=color[colorindex])

        # 十字光标相关设置
        self.label = pg.TextItem()  # 创建一个文本项
        self.plotItem.addItem(self.label)  # 在图形部件中添加文本项

        if self.detailplotcheckbox.isChecked():
            self.vLine = pg.InfiniteLine(angle=90, movable=False, )  # 创建一个垂直线条
            self.hLine = pg.InfiniteLine(angle=0, movable=False, )  # 创建一个水平线条
            self.plotItem.addItem(self.vLine, ignoreBounds=True)  # 在图形部件中添加垂直线条
            self.plotItem.addItem(self.hLine, ignoreBounds=True)  # 在图形部件中添加水平线条

        # 在状态栏上显示当前绘图的文件和绘图总数
        self.plotcount += 1
        self.statusbar.showMessage("RSA:plot " + file.lstrip(self.workdir) + " ，当前绘图总数 "
                                   + str(self.plotcount))

    def addfile(self):
        # 如果文件指针为空，赋值到当前工作目录，防止用户点击顶级目录空白处无法正常addfile
        if self.mouseindex == '':
            self.mouseindex = self.workdir

        # 弹出对话框，获取文件名；按下ok，okPressed为真
        filename, okPressed = QInputDialog.getText(self, "文件名", "请输入文件名:", QLineEdit.Normal)
        fullfilename = filename + get_default_data_filename_extension()

        # 这里默认文件指针指向的是一个目录，拼出完整文件路径
        fullfilepath = self.mouseindex + os.path.sep + fullfilename

        # 判断文件是否已经存在，如果已经存在就在方法内部处理
        isfileexists = self.fileexists(fullfilepath)
        if not isfileexists:

            # 文件不存在，那么文件指针所指向的是一个文件吗？
            if os.path.isfile(self.mouseindex):
                # 指针位置是一个文件，获取文件所在目录，修改路径
                fullfilepath = os.path.dirname(self.mouseindex) + os.path.sep + fullfilename
                # 修改目录后，用户指定的文件名是否已经存在？如果已经存在就在方法内部处理
                isfileexists = self.fileexists(fullfilepath)

        # 文件名不为空,用户指定文件不存在，可以执行写入操作
        if okPressed and filename != '' and not isfileexists:
            self.statusbar.showMessage("add " + self.mouseindex.lstrip(self.workdir) + os.sep + fullfilename)
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
                                        QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                # 用户点击Yes，进入编辑模式
                self.editdatafile(filepath)
            if reply == QMessageBox.Cancel:
                # 用户点击No，什么也不做
                pass
            self.statusbar.showMessage("RSA:" + self.mouseindex.lstrip(self.workdir) + filename + " 文件已存在")
            return True

        return False

    def writedatatofile(self, filepath):
        # 弹出提示框让用户输入数据
        data, ok = QInputDialog.getMultiLineText(self, "请输入数据", "请按照示例数据格式输入：", get_testdata())
        # 用户按下了ok，不按的话不写入数据
        if ok:
            try:
                f = open(filepath, "w")
                f.write(data)
                f.close()
                self.statusbar.showMessage("RSA:write " + filepath.lstrip(self.workdir) + " 写入成功")
            except Exception as e:
                QMessageBox.critical(self, "警告", "文件写入不正确\n{}".format(e), QMessageBox.Close, QMessageBox.Close)

    def editfile(self):
        if os.path.isdir(self.mouseindex):
            # 打开的是一个目录而不是一个文件时提示用户
            QMessageBox.information(self, "温馨提示", "请选择一个数据文件", QMessageBox.Close, QMessageBox.Close)
        elif os.path.isfile(self.mouseindex):
            # 分割文件拓展名，并与默认数据文件拓展名作比较
            file_extension = os.path.splitext(self.mouseindex)[1]
            if file_extension == get_default_data_filename_extension():
                self.editdatafile(self.mouseindex)
            else:
                QMessageBox.information(self, "温馨提示", "请选择一个数据文件", QMessageBox.Close, QMessageBox.Close)

    def editdatafile(self, file):
        # 这里本来是使用os.system()来启动notepad，但是pyinstall打包后运行这段代码会弹出一个dos窗口，所以做此修改
        try:
            subprocess.check_call("notepad {}".format(file), shell=True)
        except Exception as e:
            QMessageBox.critical(self, "警告", "文件编辑不正确\n{}".format(e), QMessageBox.Close, QMessageBox.Close)
        self.statusbar.showMessage("RSA:edit " + file.lstrip(self.workdir))

    def removefile(self):
        if os.path.isdir(self.mouseindex):
            QMessageBox.question(self, "温馨提示", "您所选择的是一个文件夹\n出于数据安全考虑\n本程序不提供删除文件夹功能", QMessageBox.Close, QMessageBox.Close)
        elif os.path.isfile(self.mouseindex):
            (filepath, filename) = os.path.split(self.mouseindex)
            reply = QMessageBox.warning(self, "温馨提示", "是否确定删除文件"+filename,
                                        QMessageBox.Yes | QMessageBox.Cancel,
                                        QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                # 用户点击Yes，删除文件
                os.remove(self.mouseindex)
                self.statusbar.showMessage("RSA:remove " + self.mouseindex.lstrip(self.workdir))
            if reply == QMessageBox.Cancel:
                pass

    @pyqtSlot()
    def on_clearbutton_clicked(self):
        self.pyqtgraph.clear()
        self.plotcount = 0
        self.mousepointtrackinglabel.setText("MousePoint")
        self.plotItem.getAxis('bottom').setTicks(ticks=None)
        self.plotItem.getAxis('right').setTicks(ticks=None)
        self.statusbar.showMessage("RSA:reset")

    @pyqtSlot()
    def on_browsebutton_clicked(self, path=None, isdialogparent=False):
        if path is None:
            filedialog = QFileDialog()
            filedialog.setViewMode(QFileDialog.Detail)
            path = QFileDialog.getExistingDirectory(self, '请选择数据文件夹', os.environ['USERPROFILE'] + os.path.sep + 'desktop')
        self.changworkdir(path, isdialogparent)
        self.lineEdit.setText(path)
        self.statusbar.showMessage("RSA:change work dir to " + path)

    @pyqtSlot()
    def on_searchbutton_clicked(self):
        self.searchdialog.show()

    def searchdialogitemdoubleclicked(self, event):
        index = event.text()
        if os.path.isdir(index):
            self.on_browsebutton_clicked(index, isdialogparent=True)
        elif os.path.isfile(index):
            path = os.path.dirname(index)
            self.on_browsebutton_clicked(path, isdialogparent=True)
            self.mouseindex = index
            self.plotfile()
            self.searchdialog.close()

        if self.closesearchchechbox.isChecked():
            self.searchdialog.close()

    def aboutthisprogram(self):
        self.aboutwin.show()
        self.statusbar.showMessage("RSA:about this program")

    def helpmanual(self):
        self.helpwin.show()
        self.helpwin.autoStart()
        self.statusbar.showMessage("RSA:start help manual")

    def mouseMoved(self, event):
        if self.detailplotcheckbox.isChecked() and self.plotcount >= 1:
            if event is None:
                print("事件为空")
            else:
                pos = event  # 获取事件的鼠标位置
                try:
                    # 如果鼠标位置在绘图部件中
                    if self.plotItem.sceneBoundingRect().contains(pos):
                        mousePoint = self.plotItem.vb.mapSceneToView(pos)  # 转换鼠标坐标
                        index = int(mousePoint.x())  # 鼠标所处的X轴坐标
                        # pos_y = int(mousePoint.y())  # 鼠标所处的Y轴坐标
                        if -1 < index < len(self.y_data.index):
                            # 在label中写入HTML
                            self.label.setHtml(
                                "<p style='color:white'><strong>波长：{0}</strong></p><p style='color:white'>数据：{1}</p></p>"
                                    .format(self.x_dict[index], self.y_data.iloc[index].values))
                            self.label.setPos(mousePoint.x(), mousePoint.y())  # 设置label的位置
                        # 设置垂直线条和水平线条的位置组成十字光标
                        self.vLine.setPos(mousePoint.x())
                        self.hLine.setPos(mousePoint.y())
                except Exception as e:
                    QMessageBox.information(self, "提示", "鼠标追踪错误\n{}".format(e), QMessageBox.Close,
                                            QMessageBox.Close)

    def closeEvent(self, QCloseEvent):
        # 退出程序确认,使用QMessageBox提示
        reply = QMessageBox.warning(self, "温馨提示", "即将退出RSA, 确定？", QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            QCloseEvent.accept()
        if reply == QMessageBox.Cancel:
            QCloseEvent.ignore()


if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()
