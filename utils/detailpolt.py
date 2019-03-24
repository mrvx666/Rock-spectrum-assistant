import pyqtgraph as pg
from pandas import read_csv
import sys

from utils.config import get_ticks_spacing

ticksspacing = get_ticks_spacing()

fileinex = sys.argv[1]

data = read_csv(fileinex, dtype=float, sep='\t', index_col=0)

# 初始化窗口
app = pg.QtGui.QApplication([])
win = pg.GraphicsWindow(title='RSA详细绘图模式')
win.resize(730, 400)

xdict = dict(enumerate(data.index))
axis_x_data = [(i, list(data.index)[i]) for i in range(0, len(data.index), ticksspacing)]
stringaxis = pg.AxisItem(orientation='bottom')
stringaxis.setTicks([axis_x_data, xdict.items()])

plot = win.addPlot(axisItems={'bottom': stringaxis})
label = pg.TextItem()
plot.addItem(label)

# 绘图与设置坐标轴
plot.plot(x=list(xdict.keys()), y=data.iloc[:, 0].values, pen='b')
plot.setLabel(axis='left', text='wavevalues')
plot.setLabel(axis='bottom', text='wavelength')

# 十字光标
vLine = pg.InfiniteLine(angle=90, movable=False, )
hLine = pg.InfiniteLine(angle=0, movable=False, )
plot.addItem(vLine, ignoreBounds=True)
plot.addItem(hLine, ignoreBounds=True)
vb = plot.vb

def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if plot.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        #pos_y = int(mousePoint.y())
        if 0 < index < len(data.index):
            #print(xdict[index], data.iloc[index].values)
            label.setHtml(
                "<p style='color:white'>波长：{0}</p><p style='color:white'>数值：{1}</p>".format(
                    xdict[index], data.iloc[index].values))
            label.setPos(mousePoint.x(), mousePoint.y())
        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())

proxy = pg.SignalProxy(plot.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

app.exec_()