import os
import shutil

dirSource = r'D:\Files\Documents\HKU Materials\HKU Research\Lin - Network MnA\2015.12.17 FDIC bank branch data\Financial Data'
dirTarget = r'D:\Files\Documents\HKU Materials\HKU Research\Lin - Network MnA\2015.12.17 FDIC bank branch data\Customer Base'

#fileList = ['USDtoFX_1971to2015.txt','US_DEF_CALL_1971_2015.txt','TRADINGCOST2015.txt','SSPAunv11FX_MeanRetTim_s.for','SSPAunv11FX_MeanRet_s.for','SSPAunv11FX_InfoRatioTim_s.for','SSPAunv11FX_InfoRatio_s.for',
#            'SR2_RESULT.TXT','SR1_RESULT.TXT','O2_RESULT.TXT','O1_RESULT.TXT','MA5_RESULT.TXT','MA4_RESULT.TXT','MA3_RESULT.TXT','MA2_RESULT.TXT','MA1_RESULT.TXT','INDEX21195.TXT','FX_daily_1971to2015.txt',
#            'F3_RESULT.TXT','F2_RESULT.TXT','F1_RESULT.TXT','executeAllCountriesFourMainCodes.sh','CB2_RESULT.TXT','CB1_RESULT.TXT','BootSeedB200BQ01.txt','BootSeedB100BQ01.txt','autoSimulatorReadLines.sh']

# fileList = ['SSPAunv11FX_MeanRetTim_s.for','SSPAunv11FX_MeanRet_s.for','SSPAunv11FX_InfoRatioTim_s.for','SSPAunv11FX_InfoRatio_s.for','INDEX21195.TXT',
#             'executeAllCountriesFourMainCodes.sh','autoSimulatorReadLines.sh','RunFSR.for','RunMA.for','StationaryBootstrapGenerator1.for']

# countryList = ['EU','JP','NZ','SWE','SWI','CHI','COL','ISR','KOR','PHI','RUS','TAI']

# fileList = ['DailyReturn_InfoRatio.TXT','DailyReturn_InfoRatioTim.TXT']

# for folder in os.listdir(dirTarget):
# #     if len(folder)<=4 and (folder in countryList):
#     if len(folder)<=4:
#         folderLocation = dirSource + os.sep + folder
#         for fileName in os.listdir(folderLocation):
#             try:
#                 if fileName in fileList:
#                     sourceFile = dirSource + os.sep + folder + os.sep + fileName
#                     targetFile = dirTarget + os.sep + folder + os.sep + fileName
#                     shutil.copyfile(sourceFile, targetFile)
#             except:
#                 print folder
#                 print fileName
#                 pass


for folder in os.listdir(dirSource):
    folderLocation = dirSource + os.sep + folder
    for fileName in os.listdir(folderLocation):
        try:
#             print fileName[-18:]
            if fileName[-18:] == 'Total Deposits.csv':
#                 print True
#                 if not os.path.exists(dirTarget + os.sep + folder):
#                     os.makedirs(dirTarget + os.sep + folder)
                sourceFile = dirSource + os.sep + folder + os.sep + fileName
                targetFile = dirTarget + os.sep + fileName
                shutil.copyfile(sourceFile, targetFile)
        except:
#             print folder
#             print fileName
            pass
