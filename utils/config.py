# coding:utf-8
# 这里本来是使用yaml的方式保存数据，无奈pyinstall打包不能打包yaml文件，整合到一个文件好了

# 本软件的默认工作目录
workdir = "data"
# 数据文件的拓展名
default_data_file_extension = ".txt"
# 绘图间隔
ticksspacing = 500
# 绘图限制，当绘图板上超过这个限制会提示用户清除图形
plotlimit = 5
# 网格透明度
grid_alpha = 0.5
# x坐标轴文字
x_axis_lable = "波长"
# 轴坐标文字
y_axis_lable = "反射率"
# 在线说明网址
help_documentation_url = "https://docs.qq.com/doc/DWkNmQ3VDZVJuVlVu"
# 示例数据
testdata = "Wavelength	XK1Y08-100000.asd\n" \
           "350	 0.068295808533771 \n" \
           "351	 6.88503984835842E-02 \n" \
           "353	 6.96586664904809E-02"


def get_default_workdir():
    return workdir


def get_default_data_file_extension():
    return default_data_file_extension


def get_ticks_spacing():
    return ticksspacing


def get_plot_limit():
    return int(plotlimit)


def get_grid_alpha():
    return grid_alpha


def get_x_axis_lable():
    return x_axis_lable


def get_y_axis_lable():
    return y_axis_lable


def get_help_documentation_url():
    return help_documentation_url


def get_testdata():
    return testdata


