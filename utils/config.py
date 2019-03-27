# coding:utf-8
# 这里本来是使用yaml的方式保存数据，无奈pyinstall打包不能打包yaml文件，整合到一个文件好了

# 本软件的默认工作目录
workdir = "data"
# 数据文件的拓展名
data_filename_extension = ".txt"
# 绘图间隔
ticksspacing = 500
# 帮助手册图片数目
help_manual_page = 6
# 绘图限制，当绘图板上超过这个限制会提示用户清除图形
plotlimit = 5
# 网格透明度
grid_alpha = 0.7
# 示例数据
testdata = "Wavelength	XK1Y08-100000.asd\n" \
           "350	 0.068295808533771 \n" \
           "351	 6.88503984835842E-02 \n" \
           "353	 6.96586664904809E-02"


def get_default_workdir():
    return workdir


def get_default_data_filename_extension():
    return data_filename_extension


def get_ticks_spacing():
    return ticksspacing


def get_plot_limit():
    return int(plotlimit)


def get_help_manual_page():
    return int(help_manual_page)


def get_grid_alpha():
    return grid_alpha


def get_testdata():
    return testdata


