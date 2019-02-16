import xlrd
import math
import os
import shutil

dirRemoveBase = r'D:\Files\Documents\HKU Materials\HKU Research\Po - ForEX'

folderList = ['updateDataReplicationTCasEU',
'updateDataReplicationTCasJP',
'updateDataReplicationTCasUK',
'updateDataReplicationTCasSWI',
'updateDataUSDasEU',
'updateDataUSDasEUTC00',
'updateDataUSDasJP',
'updateDataUSDasJPTC00',
'updateDataUSDasUK',
'updateDataUSDasUKTC00',
'updateDataUSDasSWI',
'updateDataUSDasSWITC00']

fileList = ['CB1_RESULT.TXT','CB2_RESULT.TXT','F1_RESULT.TXT','F2_RESULT.TXT','F3_RESULT.TXT','MA1_RESULT.TXT','MA2_RESULT.TXT','MA3_RESULT.TXT','MA4_RESULT.TXT','MA5_RESULT.TXT',
            'O1_RESULT.TXT','O2_RESULT.TXT','SR1_RESULT.TXT','SR2_RESULT.TXT']

for forderToDelete in folderList:
    dirRemove = dirRemoveBase + os.sep + forderToDelete
#     print dirRemove
    for folder in os.listdir(dirRemove):
        if len(folder)<4:
#         print folder
            folderLocation = dirRemove + os.sep + folder
            for fileName in os.listdir(folderLocation):
                try:
                    if fileName in fileList:
                        toDeleteFile = folderLocation + os.sep + fileName
                        os.remove(toDeleteFile)
                except:
                    print folder
                    print fileName
                    pass

