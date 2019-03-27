# Rock spectrum assistant
hello，看到这个文档的朋友。
Rock spectrum assistant是一个基于Qt5架构和Python3语言开发的简单绘图小程序。本项目2018年11月立项，2018年12月正式开始开发。

使用说明：

1.程序默认读取同目录下的data文件夹作为工作目录，如果data文件夹不存在，您可以手动指定目录

2.在右侧文件操作区，单机鼠标右键弹出菜单，即可使用“绘图”、“添加文件”、“编辑文件”、“删除文件功能”

3.当您进行了一个绘图，可以在绘图区域用鼠标滚轮放大，或者按住鼠标左键拖动绘图区域

4.右下角“清除绘图”按钮用于清除绘画板上已经绘出的曲线

5.当您想使用十字线绘图模式时，请点击位于下侧的detailpolt，然后再选择一个文件点击polt，即可用新窗口绘制一个图形

6.本软件的设置位于until\config.py下，只有一些最简单的参数设置，不建议进行修改

Note：当你在pycharm中导入代码时，请在pycharm左侧目录树，右击ui和until两个文件夹，选择Make Directory As → Souces Root，否则在pycharm中run会报错


TO DO List：

~~“关于”界面~~

~~底部系统状态栏功能开发~~

~~绘图板可以指定不同画笔颜色~~

~~简单的系统选项及其存储~~

开发带有checkbox的model

参考资料：

1.《PyQt5快速开发与实战》与其配套代码

https://github.com/cxinping/PyQt5

2.Create file browser in python and Qt (PyQt5 or PySide2 QTreeView and QFileSystemModel)

https://www.youtube.com/watch?v=4PkPezdpO90

https://github.com/vfxpipeline/filebrowser

3.documentation for pyqtgraph

http://www.pyqtgraph.org/documentation/

4.PyQt5的PyQtGraph实践系列2：绘制股票十字光标K线图

https://zmister.com/archives/793.html

5.PyQt Examples（PyQt各种测试和例子） 页面切换/图片轮播动画

https://github.com/PyQt5/PyQt/tree/master/QPropertyAnimation

6.Notepad by python3.4+pyqt 作者github/Lowpower

https://github.com/Lowpower/notepad




