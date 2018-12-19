#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel

from UiImageSlider import Ui_Form  # @UnresolvedImport


class ImageSliderWidget(QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super(ImageSliderWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # 绑定信号槽
        self.pushButtonPrev.clicked.connect(self.prevtpicture)
        self.pushButtonNext.clicked.connect(self.nextpicture)
        self.closeButton.clicked.connect(self.close)

        # 添加图片页面
        for name in os.listdir('helpImages'):
            label = QLabel(self.stackedWidget)
            label.setScaledContents(True)
            label.setPixmap(QPixmap('helpImages/' + name))
            self.stackedWidget.addWidget(label)
        self.autoStart()

    def autoStart(self):
        self.stackedWidget.autoStart()

    def autoStop(self):
        self.stackedWidget.autoStop()

    def nextpicture(self):
        self.autoStop()
        self.stackedWidget.slideInNext()

    def prevtpicture(self):
        self.autoStop()
        self.stackedWidget.slideInPrev()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = ImageSliderWidget()
    w.show()
    sys.exit(app.exec_())
