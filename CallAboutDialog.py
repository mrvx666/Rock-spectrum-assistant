# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog,QApplication,QMessageBox
from PyQt5.QtCore import pyqtSlot,QUrl,QEvent,Qt
from PyQt5.QtGui import QDesktopServices,QMouseEvent
import sys
from aboutdialog import Ui_aboutDialog

jlu_geo_website = "http://geo.jlu.edu.cn/"
project_gituhub_url = "https://github.com/mrvx666/Rock-spectrum-assistant"
SB_jjh = "https://www.zhihu.com/question/42012531"


class aboutDialogUI(QDialog,Ui_aboutDialog):
    def __init__(self, parent=None):
        super(aboutDialogUI, self).__init__(parent)
        self._initUI()
        self.clickcount = 0

    def _initUI(self):
        self.setupUi(self)
        self.geoicolabel.installEventFilter(self)

    @pyqtSlot()
    def on_projectgituhubButton_clicked(self):
        QDesktopServices.openUrl(QUrl(project_gituhub_url))

    @pyqtSlot()
    def on_geowebsiteButton_clicked(self):
        QDesktopServices.openUrl(QUrl(jlu_geo_website))

    @pyqtSlot()
    def on_closeButton_clicked(self):
        self.close()

    # 这段代码没什么用，纯粹为了发泄而已，如果改做它用建议把这段代码删了
    def eventFilter(self, watched, event):
        if watched == self.geoicolabel:
            if event.type() == QEvent.MouseButtonPress:
                mouseEvent = QMouseEvent(event)
                self.clickcount += 1
                if mouseEvent.button() == Qt.LeftButton:
                    if self.clickcount == 4:
                        QMessageBox.information(self, "学长真言", "你似乎发现了彩蛋\n再点击5次即可查看", QMessageBox.Yes,
                                                QMessageBox.Yes)
                    if self.clickcount == 9:
                        reply = QMessageBox.information(self, "学长真言", "金锦花是傻逼，萨比，撒币\n点击确定查看九评金锦花", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                        if (reply == QMessageBox.Yes):
                            QDesktopServices.openUrl(QUrl(SB_jjh))
                        if (reply == QMessageBox.No):
                            pass
                        self.clickcount = 0

        return QDialog.eventFilter(self, watched, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ad = aboutDialogUI()
    ad.show()
    sys.exit(app.exec_())

