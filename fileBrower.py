import os,re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import numpy as np

abspath = r"C:\Users\MrvX\Desktop\MSA\data"
path = "./data/"
testdataname = "Test.txt"
testdata = path + testdataname

def getallfile(path):
    allfile = []
    allfilelist = os.listdir(path)
    for file in allfilelist:
        print(file)
        filepath = os.path.join(path, file)
        # 判断是不是文件夹
        if os.path.isdir(filepath):
            print("filepath is dir")
            getallfile(filepath)
        allfile.append(filepath)
    return allfile

def xwalk(path):
    for maindir, subdir, file_name_list in os.walk(path):
        if len(subdir):
            print("subdir exist")
            print(subdir)
            for dir in subdir:
                print("xwalk(dir)")
                print(dir)
                xwalk(dir)
        else:
            print("subdir no exist")
            print(file_name_list)
            return file_name_list


def scan_files(directory, prefix=None, postfix=None):
    files_list = []

    for root, sub_dirs, files in os.walk(directory):
        for special_file in files:
            if postfix:
                if special_file.endswith(postfix):
                    files_list.append(os.path.join(root, special_file))
            elif prefix:
                if special_file.startswith(prefix):
                    files_list.append(os.path.join(root, special_file))
            else:
                files_list.append(os.path.join(root, special_file))

    return files_list

def list_all_files(rootdir):
    import os
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files

def lwalk(top, topdown=True, followlinks=False, max_level=None):
    if max_level is None:
        new_max_level = None
    else:
        if max_level == 0:
            return
        else:
            new_max_level = max_level - 1
    top = os.fspath(top)
    dirs, nondirs, walk_dirs = [], [], []
    with os.scandir(top) as it:
        for entry in it:
            if entry.is_dir():
                dirs.append(entry.name)
            else:
                nondirs.append(entry.name)
            if not topdown and entry.is_dir():
                if followlinks or not entry.is_symlink():
                    walk_dirs.append(entry.path)
        if topdown:
            yield top, dirs, nondirs
            for dirname in dirs:
                new_path = os.path.join(top, dirname)
                if followlinks or not os.path.islink(new_path):
                    yield from lwalk(new_path, topdown, followlinks, new_max_level)
        else:
            for new_path in walk_dirs:
                yield from lwalk(new_path, topdown, followlinks, new_max_level)
            yield top, dirs, nondirs

def openDataFile(filepath):
    return np.loadtxt(filepath,dtype=float,skiprows=1,usecols=1)


def getEachFile(path):
    for dirpath, dirnames, filenames in os.walk(path):
        return dirpath,dirnames,filenames


def printEachFile(path):
    dirpath,dirnames,filenames = getEachFile(path)
    print(type(dirpath))
    print(dirpath)
    print(type(dirnames))
    print(dirnames)
    print(type(filenames))
    print(filenames)


if __name__ == '__main__':
    data = openDataFile(testdata)
    for i in range(0,5,1):
        print(data[i])
    print(data)
    print(type(data[0]))
    printEachFile("./data/")


