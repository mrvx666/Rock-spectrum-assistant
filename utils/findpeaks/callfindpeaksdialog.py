from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtGui import QDesktopServices
from utils.findpeaks.findpeaksdialog import Ui_findpeaksdialog
from utils.findpeaks.lib import *


detect_peaks_help_url = "https://nbviewer.jupyter.org/github/demotu/BMC/blob/master/notebooks/DetectPeaks.ipynb"
Janko_Slavic_findpeaks_help_url = "https://github.com/jankoslavic/py-tools/blob/master/findpeaks/Findpeaks%20example.ipynb"
tony_beltramelli_detect_peaks_help_url = "https://github.com/MonsieurV/py-findpeaks/blob/master/tests/libs/tony_beltramelli_detect_peaks.py"

parameters_detect_peaks = {"Minimum distance": 1, "Minimum height": 0.2, "Relative threshold": 0}
parameters_Janko_Slavic_findpeaks = {"spacing": 1, "limit": 7}
parameters_tony_beltramelli_detect_peaks = {"threshold": 0.5}


class findpeaksdialog(QDialog, Ui_findpeaksdialog):

    def __init__(self, *args, **kwargs):
        super(findpeaksdialog, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)

        # 获取标签和数字框数组方便后期调整
        self.parameters_lable_list = [self.parameter1label,
                                 self.parameter2label,
                                 self.parameter3label,
                                 self.parameter4label]
        self.parameters_values_list = [self.parameter1doubleSpinBox,
                                  self.parameter2doubleSpinBox,
                                  self.parameter3doubleSpinBox,
                                  self.parameter4doubleSpinBox]
        # 初始化默认选择的项目参数
        self.selectionchange()

        # 初始化一些参数供RSA主窗体使用
        self.peaksmarklist = []

    def selectionchange(self):
        current_selection = self.comboBox.currentText()
        if current_selection == "detect_peaks":
            self.set_parameters(parameters_detect_peaks)
        if current_selection == "Janko_Slavic_findpeaks":
            self.set_parameters(parameters_Janko_Slavic_findpeaks)
        if current_selection == "tony_beltramelli_detect_peaks":
            self.set_parameters(parameters_tony_beltramelli_detect_peaks)

    def set_parameters(self, parameters):

        # 重置所有选项到可用状态
        for i in range(0, len(self.parameters_lable_list), 1):
            self.parameters_lable_list[i].setEnabled(True)
            self.parameters_values_list[i].setEnabled(True)

        # 填入参数
        i = 0
        for parameter_name, parameter_value in parameters.items():
            self.parameters_lable_list[i].setText(parameter_name)
            # 如果原始方法中对函数的初始值定义为None，则跳过
            if parameter_value is not None:
                self.parameters_values_list[i].setValue(parameter_value)
            i += 1

        # 使超出方法所需要的参数选项框关闭
        if i <= len(self.parameters_lable_list):
            for i in range(i, len(self.parameters_lable_list), 1):
                self.parameters_lable_list[i].setText("Parameter{}".format(i+1))
                self.parameters_lable_list[i].setEnabled(False)
                self.parameters_values_list[i].setValue(0.00)
                self.parameters_values_list[i].setEnabled(False)

    def get_parameters(self):
        parameters_lable_list_text = []
        for lable in self.parameters_lable_list:
            parameters_lable_list_text.append(lable.text())
        parameters_values_list_values = []
        for value in self.parameters_values_list:
            if value.value() is None:
                parameters_values_list_values.append(None)
            else:
                parameters_values_list_values.append(value.value())
        data = dict(map(lambda x,y:[x,y], parameters_lable_list_text, parameters_values_list_values))
        return data

    def find_peaks(self, data):
        parameters = self.get_parameters()
        current_selection = self.comboBox.currentText()
        peaks_index_list = []
        if current_selection == "detect_peaks":
            mph = parameters["Minimum height"]
            mpd = parameters["Minimum distance"]
            threshold = parameters["Relative threshold"]
            peaks_index_list = detect_peaks(x=data, mph=mph, mpd=mpd, threshold=threshold)
        if current_selection == "Janko_Slavic_findpeaks":
            spacing = round(parameters["spacing"])  # 源代码中要求对这个数字必须是整数
            limit = parameters["limit"]
            peaks_index_list = Janko_Slavic_findpeaks(data=data, spacing=spacing, limit=limit)
        if current_selection == "tony_beltramelli_detect_peaks":
            threshold = parameters["threshold"]
            peaks_index_list = tony_beltramelli_detect_peaks(signal=data, threshold=threshold)
        return peaks_index_list

    def clear(self):
        self.textEdit.clear()
        self.textEdit.setEnabled(False)
        self.peaksmarklist.clear()

    @pyqtSlot()
    def on_helpbutton_clicked(self):
        current_selection = self.comboBox.currentText()
        if current_selection == "detect_peaks":
            QDesktopServices.openUrl(QUrl(detect_peaks_help_url))
        if current_selection == "Janko_Slavic_findpeaks":
            QDesktopServices.openUrl(QUrl(Janko_Slavic_findpeaks_help_url))
        if current_selection == "tony_beltramelli_detect_peaks":
            QDesktopServices.openUrl(QUrl(tony_beltramelli_detect_peaks_help_url))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = findpeaksdialog()
    w.show()
    sys.exit(app.exec_())

