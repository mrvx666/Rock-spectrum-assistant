from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel

from utils.helppictureSliding.ImageSliderUI import Ui_ImageSlider
from utils.config import get_help_manual_page

import apprcc_rc

helpmanualpage = get_help_manual_page()


class ImageSliderWidget(QWidget, Ui_ImageSlider):

    def __init__(self, *args, **kwargs):
        super(ImageSliderWidget, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # 绑定信号槽
        self.pushButtonPrev.clicked.connect(self.prevtpicture)
        self.pushButtonNext.clicked.connect(self.nextpicture)
        self.closeButton.clicked.connect(self.close)

        # 添加图片页面
        for num in range(1, helpmanualpage+1, 1):
            label = QLabel(self.stackedWidget)
            label.setScaledContents(True)
            pic = ':/image/image/helpimage/help ({}).png'.format(str(num))
            label.setPixmap(QPixmap(pic))
            self.stackedWidget.addWidget(label)

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