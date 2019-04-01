from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QDialog


from utils.helpdialog.helpdialog import Ui_helpDialog
from utils.config import get_help_documentation_url

help_documentation_url = get_help_documentation_url()


class helpdialog(QDialog,Ui_helpDialog):
    def __init__(self, *args, **kwargs):
        super(helpdialog, self).__init__(*args, **kwargs)
        self.setupUi(self)

    @pyqtSlot()
    def on_open_help_documentation_url_Button_clicked(self):
        QDesktopServices.openUrl(QUrl(help_documentation_url))

    @pyqtSlot()
    def on_closeButton_clicked(self):
        self.close()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = helpdialog()
    w.show()
    sys.exit(app.exec_())