from PyQt5.QtWidgets import QDialog
from utils.findpeaks.findpeaksdialog import Ui_findpeaksdialog
import numpy as np
from math import sqrt

parameters_detect_peaks = {"Minimum distance": None, "Minimum height": 1, "Relative threshold": 0}
parameters_Janko_Slavic_findpeaks = {"spacing": None, "limit": 7}
parameters_tony_beltramelli_detect_peaks = {"Amplitude": None, "threshold": 0.5}


class findpeaks(QDialog, Ui_findpeaksdialog):

    def __init__(self, *args, **kwargs):
        super(findpeaks, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        # 初始化默认选择的项目参数
        self.selectionchange()

    def selectionchange(self):
        current_selection = self.comboBox.currentText()
        if current_selection == "detect_peaks":
            self.set_parameters(parameters_detect_peaks)
        if current_selection == "Janko_Slavic_findpeaks":
            self.set_parameters(parameters_Janko_Slavic_findpeaks)
        if current_selection == "tony_beltramelli_detect_peaks":
            self.set_parameters(parameters_tony_beltramelli_detect_peaks)

    def set_parameters(self, parameters):
        parameters_lable_list = [self.parameter1label,
                                 self.parameter2label,
                                 self.parameter3label,
                                 self.parameter4label]
        parameters_values_list = [self.parameter1doubleSpinBox,
                                self.parameter2doubleSpinBox,
                                self.parameter3doubleSpinBox,
                                self.parameter4doubleSpinBox]
        i = 0  # 填入默认参数
        for parameter_name, parameter_value in parameters.items():
            parameters_lable_list[i].setText(parameter_name)
            if parameter_value is not None:
                parameters_values_list[i].setValue(parameter_value)
            i += 1

        if i <= len(parameters_lable_list):
            for i in range(i, len(parameters_lable_list),1):
                parameters_lable_list[i].setEnabled(False)
                parameters_values_list[i].setEnabled(False)

    def detect_peaks(x, mph=None, mpd=1, threshold=0, edge='rising',
                     kpsh=False, valley=False):

        """Detect peaks in data based on their amplitude and other features.

        Parameters
        ----------
        x : 1D array_like
            data.
        mph : {None, number}, optional (default = None)
            detect peaks that are greater than minimum peak height.
        mpd : positive integer, optional (default = 1)
            detect peaks that are at least separated by minimum peak distance (in
            number of data).
        threshold : positive number, optional (default = 0)
            detect peaks (valleys) that are greater (smaller) than `threshold`
            in relation to their immediate neighbors.
        edge : {None, 'rising', 'falling', 'both'}, optional (default = 'rising')
            for a flat peak, keep only the rising edge ('rising'), only the
            falling edge ('falling'), both edges ('both'), or don't detect a
            flat peak (None).
        kpsh : bool, optional (default = False)
            keep peaks with same height even if they are closer than `mpd`.
        valley : bool, optional (default = False)
            if True (1), detect valleys (local minima) instead of peaks.
        show : bool, optional (default = False)
            if True (1), plot data in matplotlib figure.
        ax : a matplotlib.axes.Axes instance, optional (default = None).

        Returns
        -------
        ind : 1D array_like
            indeces of the peaks in `x`.

        Notes
        -----
        The detection of valleys instead of peaks is performed internally by simply
        negating the data: `ind_valleys = detect_peaks(-x)`

        The function can handle NaN's

        See this IPython Notebook [1]_.

        References
        ----------
        .. [1] http://nbviewer.ipython.org/github/demotu/BMC/blob/master/notebooks/DetectPeaks.ipynb

        Examples
        --------
        """

        x = np.atleast_1d(x).astype('float64')
        if x.size < 3:
            return np.array([], dtype=int)
        if valley:
            x = -x
        # find indexes of all peaks
        dx = x[1:] - x[:-1]
        # handle NaN's
        indnan = np.where(np.isnan(x))[0]
        if indnan.size:
            x[indnan] = np.inf
            dx[np.where(np.isnan(dx))[0]] = np.inf
        ine, ire, ife = np.array([[], [], []], dtype=int)
        if not edge:
            ine = np.where((np.hstack((dx, 0)) < 0) & (np.hstack((0, dx)) > 0))[0]
        else:
            if edge.lower() in ['rising', 'both']:
                ire = np.where((np.hstack((dx, 0)) <= 0) & (np.hstack((0, dx)) > 0))[0]
            if edge.lower() in ['falling', 'both']:
                ife = np.where((np.hstack((dx, 0)) < 0) & (np.hstack((0, dx)) >= 0))[0]
        ind = np.unique(np.hstack((ine, ire, ife)))
        # handle NaN's
        if ind.size and indnan.size:
            # NaN's and values close to NaN's cannot be peaks
            ind = ind[np.in1d(ind, np.unique(np.hstack((indnan, indnan - 1, indnan + 1))), invert=True)]
        # first and last values of x cannot be peaks
        if ind.size and ind[0] == 0:
            ind = ind[1:]
        if ind.size and ind[-1] == x.size - 1:
            ind = ind[:-1]
        # remove peaks < minimum peak height
        if ind.size and mph is not None:
            ind = ind[x[ind] >= mph]
        # remove peaks - neighbors < threshold
        if ind.size and threshold > 0:
            dx = np.min(np.vstack([x[ind] - x[ind - 1], x[ind] - x[ind + 1]]), axis=0)
            ind = np.delete(ind, np.where(dx < threshold)[0])
        # detect small peaks closer than minimum peak distance
        if ind.size and mpd > 1:
            ind = ind[np.argsort(x[ind])][::-1]  # sort ind by peak height
            idel = np.zeros(ind.size, dtype=bool)
            for i in range(ind.size):
                if not idel[i]:
                    # keep peaks with the same height if kpsh is True
                    idel = idel | (ind >= ind[i] - mpd) & (ind <= ind[i] + mpd) \
                           & (x[ind[i]] > x[ind] if kpsh else True)
                    idel[i] = 0  # Keep current peak
            # remove the small peaks and sort back the indexes by their occurrence
            ind = np.sort(ind[~idel])

        return ind

    def findpeaks(data, spacing=1, limit=None):
        """Finds peaks in `data` which are of `spacing` width and >=`limit`.
        :param data: values
        :param spacing: minimum spacing to the next peak (should be 1 or more)
        :param limit: peaks should have value greater or equal
        :return:
        """
        len = data.size
        x = np.zeros(len + 2 * spacing)
        x[:spacing] = data[0] - 1.e-6
        x[-spacing:] = data[-1] - 1.e-6
        x[spacing:spacing + len] = data
        peak_candidate = np.zeros(len)
        peak_candidate[:] = True
        for s in range(spacing):
            start = spacing - s - 1
            h_b = x[start: start + len]  # before
            start = spacing
            h_c = x[start: start + len]  # central
            start = spacing + s + 1
            h_a = x[start: start + len]  # after
            peak_candidate = np.logical_and(peak_candidate, np.logical_and(h_c > h_b, h_c > h_a))

        ind = np.argwhere(peak_candidate)
        ind = ind.reshape(ind.size)
        if limit is not None:
            ind = ind[data[ind] > limit]
        return ind

    def tony_beltramelli_detect_peaks(signal, threshold=0.5):
        """ Performs peak detection on three steps: root mean square, peak to
        average ratios and first order logic.
        threshold used to discard peaks too small """
        # compute root mean square
        root_mean_square = sqrt(np.sum(np.square(signal) / len(signal)))
        # compute peak to average ratios
        ratios = np.array([pow(x / root_mean_square, 2) for x in signal])
        # apply first order logic
        peaks = (ratios > np.roll(ratios, 1)) & (ratios > np.roll(ratios, -1)) & (ratios > threshold)
        # optional: return peak indices
        peak_indexes = []
        for i in range(0, len(peaks)):
            if peaks[i]:
                peak_indexes.append(i)
        return peak_indexes

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = findpeaks()
    w.show()
    sys.exit(app.exec_())