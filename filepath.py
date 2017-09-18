# -*- coding:utf8 -*-

import os
import shutil
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

resourePath = ""
targetPath =  ""


def copyFile(rootDir):
    count = 0
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for fileLastName in files:
            if (fileLastName.split(".")[-1] == "mp3"):
                filePath = os.path.join(root, fileLastName)
                shutil.copy(filePath, targetPath)
                print ("copy end===>:" + filePath)
                count = count + 1

    print ("处理文件：%d个" % (count))


def targetDir(targetPath):
    if(os.path.exists(targetPath) == False):
        os.makedirs(targetPath)

targetDir(targetPath)
copyFile(resourePath)

