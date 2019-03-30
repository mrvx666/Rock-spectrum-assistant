# -*- coding: utf-8 -*-

"""
这是RSA的主窗体，主要的业务都在这里完成。
"""
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileSystemModel,\
                            QMenu, QMessageBox, QFileDialog, QInputDialog, QLineEdit
import os
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

        # 声明两个数组，用于向鼠标追踪方法传递数据
        self.axis_y_data_arr = []
        self.axis_x_dict_arr = []

        # checkbox相关设置
        self.crosshaircheckbox.stateChanged.connect(lambda: self.crosshaircheckboxstateChanged(self.crosshaircheckbox))
        self.showgridcheckbox.stateChanged.connect(lambda: self.showgridcheckboxstateChanged(self.showgridcheckbox))

        # 判断程序所在目录下data文件夹是否存在
        if os.path.isdir(self.workdir):
            # 存在，设置路径提示文本框
            self.lineEdit.setText(self.workdir)
            # 设置工作目录
            self.changeworkdir(self.workdir)
        else:
            # 首次启动，默认工作目录未找到，询问用户是否设置工作目录
            self.set_work_dir(True)

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
        self.Notepad.triggered.connect(self.notepadwin)
        self.notepad = Notepad(self.workdir)

        # 把搜索子窗体双击事件连接到RSA主窗体进行处理
        self.searchdialog.listWidget.itemDoubleClicked.connect(self.searchdialogitemdoubleclicked)

        # treeView右键菜单关联
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)

        # 绘图板鼠标追踪鼠标跟踪
        self.pyqtgraph.setMouseTracking(True)
        self.pyqtgraph.scene().sigMouseMoved.connect(self.mouseMoved)

    def changeworkdir(self, path, isdialogflag=False):
        # 设置treeview工作目录，代码顺序不能颠倒
        self.model.setRootPath(path)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        # 重设工作目录
        self.workdir = self.model.rootPath()
        # 更换目录做一次清空,仅限不是由子窗口调用的时候
        if not isdialogflag:
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
            QMessageBox.information(self, "温馨提示", "选择的是一个目录，请选择一个数据文件", QMessageBox.Close, QMessageBox.Close)

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
        data = load_data(file)
        self.axis_y_data_arr.append(data)

        # 将数据表索引（波长）转换为绘图时的坐标轴数据
        x_dict = dict(enumerate(data.index))
        self.axis_x_dict_arr.append(x_dict)
        axis_x_data = [(i, list(data.index)[i]) for i in range(0, len(data.index), get_ticks_spacing())]
        stringaxis = self.plotItem.getAxis(name='bottom')
        stringaxis.setTicks([axis_x_data, x_dict.items()])
        self.pyqtgraph.plot(x=list(x_dict.keys()), y=data.iloc[:, 0].values, pen=color[colorindex])

        self.crosshaircheckboxstateChanged(self.crosshaircheckbox)

        # 用数据数组长度来给绘图计数器赋值
        self.plotcount = len(self.axis_y_data_arr)
        # 在状态栏上显示当前绘图的文件和绘图总数
        self.statusbar.showMessage("RSA:plot " + file.lstrip(self.workdir) + " ，当前绘图总数 "
                                   + str(self.plotcount))

    def addfile(self):
        self.statusbar.showMessage("RSA:add file")
        self.notepad.newFile(get_testdata())
        self.notepad.show()

    def editfile(self):
        if os.path.isdir(self.mouseindex):
            # 打开的是一个目录而不是一个文件时提示用户
            QMessageBox.information(self, "温馨提示", "选择的是一个目录，请选择一个数据文件", QMessageBox.Close, QMessageBox.Close)
        elif os.path.isfile(self.mouseindex):
            # 分割文件拓展名，并与默认数据文件拓展名作比较
            file_extension = os.path.splitext(self.mouseindex)[1]
            if file_extension == get_default_data_file_extension():
                self.edit(self.mouseindex)
            else:
                QMessageBox.information(self, "温馨提示", "文件拓展名与数据库默认拓展名不相符", QMessageBox.Close, QMessageBox.Close)

    def edit(self, file):
        self.statusbar.showMessage("RSA:edit " + file.lstrip(self.workdir))
        self.notepad.openFileEvent(file)
        self.notepad.show()

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
        self.plotItem.getAxis('bottom').setTicks(ticks=None)
        self.plotItem.getAxis('right').setTicks(ticks=None)
        self.axis_y_data_arr.clear()
        self.axis_x_dict_arr.clear()
        self.plotcount = len(self.axis_y_data_arr)
        self.statusbar.showMessage("RSA:reset")

    @pyqtSlot()
    def on_browsebutton_clicked(self, path=None, isdialogflag=False):
        if path is None:
            path = self.get_path_from_user()

        # TODO:当窗口返回的是工作目录是空字符串，重复要求用户设置
        if path == '':
            self.set_work_dir(False)

        else:
            self.changeworkdir(path, isdialogflag)
            self.lineEdit.setText(path)
            # 重设记事本模块工作目录
            self.notepad.changeworkdir(self.workdir)
            self.statusbar.showMessage("RSA:change work dir to " + path)

    def set_work_dir(self, firstworkdirflag=False):
        if firstworkdirflag is True:
            text = "没有找到默认数据文件夹，是否浏览目录设置"
        else:
            text = "未选择工作目录，是否浏览目录设置"
        self.lineEdit.setText("Working directory")
        reply = QMessageBox.question(self, "温馨提示", text, QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            # 用户点击Yes，设置工作目录,模拟用户点击浏览按钮
            self.on_browsebutton_clicked()
        if reply == QMessageBox.Cancel:
            pass

    # 我是不想搞这个额外的方法的，但是如果不做分离上面两个函数不正常
    def get_path_from_user(self):
        filedialog = QFileDialog()
        filedialog.setViewMode(QFileDialog.Detail)
        path = QFileDialog.getExistingDirectory(self, '请选择数据文件夹', os.environ['USERPROFILE'] + os.path.sep + 'desktop')
        return path

    @pyqtSlot()
    def on_searchbutton_clicked(self):
        self.searchdialog.show()

    def crosshaircheckboxstateChanged(self, checkbox):
        # 十字光标相关设置,添加元素到绘图元件中
        if checkbox.isChecked():
            self.label = pg.TextItem()  # 创建一个文本项
            self.plotItem.addItem(self.label)  # 在图形部件中添加文本项
            self.vLine = pg.InfiniteLine(angle=90, movable=False, )  # 创建一个垂直线条
            self.hLine = pg.InfiniteLine(angle=0, movable=False, )  # 创建一个水平线条
            self.plotItem.addItem(self.vLine, ignoreBounds=True)  # 在图形部件中添加垂直线条
            self.plotItem.addItem(self.hLine, ignoreBounds=True)  # 在图形部件中添加水平线条
            self.showgridcheckboxstateChanged(self.showgridcheckbox)  # 显示网格
        # 如果用户取消了checkbox的状态，那就删除这三个item
        if not checkbox.isChecked():
            self.plotItem.removeItem(self.hLine)
            self.plotItem.removeItem(self.vLine)
            self.plotItem.removeItem(self.label)

    def searchdialogitemdoubleclicked(self, event):
        index = event.text()
        if os.path.isdir(index):
            self.on_browsebutton_clicked(index, isdialogflag=True)
            self.searchdialog.close()
        elif os.path.isfile(index):
            path = os.path.dirname(index)
            self.on_browsebutton_clicked(path, isdialogflag=True)
            self.mouseindex = index
            self.plotfile()
            self.searchdialog.close()

    def aboutthisprogram(self):
        self.statusbar.showMessage("RSA:about this program")
        self.aboutwin.show()

    def helpmanual(self):
        self.statusbar.showMessage("RSA:start help manual")
        self.helpwin.show()
        self.helpwin.autoStart()

    def notepadwin(self):
        self.statusbar.showMessage("RSA:start notepad")
        self.notepad.show()

    def showgridcheckboxstateChanged(self, checkbox):
        self.plotItem.showGrid(x=checkbox.checkState(), y=checkbox.checkState(), alpha=get_grid_alpha())

    def mouseMoved(self, event):
        # 必须勾选crosshair的checkbox且绘图板上有图形才会进行鼠标追踪
        if self.crosshaircheckbox.isChecked() and self.plotcount >= 1:
            if event is None:
                pass
            else:
                pos = event  # 获取事件的鼠标位置
                try:
                    # 如果鼠标位置在绘图部件中
                    if self.plotItem.sceneBoundingRect().contains(pos):
                        mousePoint = self.plotItem.vb.mapSceneToView(pos)  # 转换鼠标坐标
                        index = int(mousePoint.x())  # 鼠标所处的X轴坐标
                        # pos_y = int(mousePoint.y())  # 鼠标所处的Y轴坐标
                        # TODO:如果多次载入数据长度不一样，这里可能会引发错误
                        if -1 < index < len(self.axis_y_data_arr[0].index):
                            # 在label中写入HTML
                            self.label.setHtml(self.generatemousetrackinglabel(self.plotcount, index))
                            self.label.setPos(mousePoint.x(), mousePoint.y())  # 设置label的位置
                        # 设置垂直线条和水平线条的位置组成十字光标
                        self.vLine.setPos(mousePoint.x())
                        self.hLine.setPos(mousePoint.y())
                except Exception as e:
                    QMessageBox.information(self, "提示", "鼠标追踪错误\n{}".format(e), QMessageBox.Close,
                                            QMessageBox.Close)

    def generatemousetrackinglabel(self, count, index):
        labletext = ""
        for i in range(count):
            labletext = labletext + "<p style='color:white'><strong>波长：{} 数据：{}</strong></p>"\
                .format(self.axis_x_dict_arr[i][index], self.axis_y_data_arr[i].iloc[index].values)
        return labletext

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
