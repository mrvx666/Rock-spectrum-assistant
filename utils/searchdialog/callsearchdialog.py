from PyQt5.QtWidgets import QDialog, QListWidgetItem, QApplication
from PyQt5.QtCore import pyqtSlot
import os
import sys

from utils.searchdialog.searchdialog import Ui_searchdialog
from utils.config import get_default_data_file_extension

Test_workdir = ".." + os.sep + ".." + os.sep + "data"


class searchdialog(QDialog, Ui_searchdialog):

    def __init__(self, workdir, parent=None):
        super(searchdialog, self).__init__(parent)
        self._initUI()
        self.workdir = workdir
        self.lineEdit.setPlaceholderText("input keywords to search...")

    def _initUI(self):
        self.setupUi(self)

    @pyqtSlot()
    def on_searchbutton_clicked(self):
        keyword = self.lineEdit.text()  # 获取搜索词
        self.listWidget.clear()  # 清空搜索结果列表
        for root, dirs, files in os.walk(self.workdir):
            #print(root,dirs,files)
            if self.dirnamecheckbox.isChecked():
                for dir in dirs:  # 遍历子目录
                    if keyword in dir:
                        fulldir = root + os.sep + dir
                        self.add_to_list(fulldir)

            for file in files:  # 遍历目录下的文件
                fullfilepath = root + os.sep + file
                if os.path.splitext(fullfilepath)[1] == get_default_data_file_extension():  # 匹配默认数据格式
                    if keyword in file:
                        self.add_to_list(fullfilepath)

                    if self.contentcheckbox.isChecked():
                        with open(fullfilepath, encoding='utf-8') as files:
                            content = files.read()
                        if keyword in content:
                            self.add_to_list(fullfilepath)

    # 添加到列表中
    def add_to_list(self, index):
        f = QListWidgetItem(index)  # 创建一个搜索结果项
        self.listWidget.addItem(f)  # 将搜索结果添加到搜索部件中


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sd = searchdialog(Test_workdir)
    sd.show()
    sys.exit(app.exec_())

