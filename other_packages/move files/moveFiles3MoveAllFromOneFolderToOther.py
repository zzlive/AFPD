import xlrd
import math
import os
import shutil

dirSource = r'D:\Files\Documents\HKU Materials\HKU Research\Po - ForEX\updateDataReplication'
dirTarget = r'D:\Files\Documents\HKU Materials\HKU Research\Po - ForEX\updateDataBreakeven'

fileList = ['Breakeven_InfoRatio.TXT','Breakeven_InfoRatioTim.TXT','Breakeven_MeanRet.TXT','Breakeven_MeanRetTim.TXT']

for folder in os.listdir(dirSource):
    if len(folder)<=4:
        folderLocation = dirSource + os.sep + folder
        for fileName in os.listdir(folderLocation):
            try:
                if fileName in fileList:
                    sourceFile = dirSource + os.sep + folder + os.sep + fileName
                    targetFile = dirTarget + os.sep + folder + os.sep + fileName
                    shutil.copyfile(sourceFile, targetFile)
            except:
                print folder
                print fileName
                pass

