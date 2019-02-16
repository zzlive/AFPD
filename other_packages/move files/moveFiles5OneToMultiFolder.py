import xlrd
import math
import os
import shutil

dirSource = r'D:\Files\Documents\HKU Materials\HKU Research\Po - ForEX\2015.9.28 Transaction cost process\updatedDevelopedCountrySSPA'
dirTarget = r'D:\Files\Documents\HKU Materials\HKU Research\Po - ForEX\updateDataOutOfSampleTest'

# for fileName in os.listdir(dirSource):
#     sourceFile = dirSource + os.sep + fileName
#     for folder in os.listdir(dirTarget):
#         try:
#             targetFile = dirTarget + os.sep + folder + os.sep + fileName
#             shutil.copyfile(sourceFile, targetFile)
#         except:
#             print folder
#             print fileName
#             pass


fileName = 'executeInfoRatioAndIRTim.sh'
sourceFile = fileName
for folder in os.listdir(dirTarget):
    if len(folder)<=3:
        try:
            targetFile = dirTarget + os.sep + folder + os.sep + fileName
            shutil.copyfile(sourceFile, targetFile)
        except:
            print folder
            pass