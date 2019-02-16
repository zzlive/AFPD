import xlrd
import math
import os
import shutil

dirSource = r'D:\Files\Documents\HKU Materials\HKU Research\Po - ForEX\Files\FX TA 2012 March correct'
dirTarget = r'D:\Files\Documents\HKU Materials\HKU Research\Po - ForEX\all_po_meanret'

for folder in os.listdir(dirSource):
    if not folder[-4:].endswith('xlsx') and not folder[-4:].endswith('.xls'):
        try:
            if os.path.exists(dirSource + os.sep + folder + '\All seed1'):
                seedNumber = 1
            elif os.path.exists(dirSource + os.sep + folder + '\All seed2'):
                seedNumber = 2
            elif os.path.exists(dirSource + os.sep + folder + '\All seed3'):
                seedNumber = 3
            elif os.path.exists(dirSource + os.sep + folder + '\All seed4'):
                seedNumber = 4
            else:
                print 'cannot find the folder'
            
#             file1 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) +' tc2-5bps' + '\FX_daily_1971to2011.txt'
#             file2 = dirTarget + os.sep + folder + '\FX_daily_1971to2011.txt'
#             shutil.copyfile(file1, file2)
#             file3 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) +' tc2-5bps' + '\USDtoFX_1971to2011.txt'
#             file4 = dirTarget + os.sep + folder + '\USDtoFX_1971to2011.txt'
#             shutil.copyfile(file3, file4)
#             file5 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) +' tc2-5bps' + '\US_DEF_CALL_1971_2011.txt'
#             file6 = dirTarget + os.sep + folder + '\US_DEF_CALL_1971_2011.txt'
#             shutil.copyfile(file5, file6)
#             
#             file7 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) +' tc2-5bps' + '\SSPA_AveRet_SigRules_TC00.txt'
#             file8 = dirTarget + os.sep + folder + '\seed2_5' + '\SSPA_AveRet_SigRules_TC00.txt'
#             shutil.copyfile(file7, file8)
#             file9 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) +' tc2-5bps' + '\SSPA_AveRetTim_SigRules_TC00.txt'
#             file10 = dirTarget + os.sep + folder + '\seed2_5' + '\SSPA_AveRetTim_SigRules_TC00.txt'
#             shutil.copyfile(file9, file10)
#             file11 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) +' tc2-5bps' + '\SSPA_InfoRatio_SigRules_TC00.txt'
#             file12 = dirTarget + os.sep + folder + '\seed2_5' + '\SSPA_InfoRatio_SigRules_TC00.txt'
#             shutil.copyfile(file11, file12)
#             file13 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) +' tc2-5bps' + '\SSPA_InfoRatioTim_SigRules_TC00.txt'
#             file14 = dirTarget + os.sep + folder + '\seed2_5' + '\SSPA_InfoRatioTim_SigRules_TC00.txt'
#             shutil.copyfile(file13, file14)
                        
            file15 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) + '\SSPAunv11FX_MeanRet_s.for'
            file16 = dirTarget + '\SSPAunv11FX_MeanRet_s_' + folder + '.for'
            shutil.copyfile(file15, file16)
            file17 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) + '\SSPAunv11FX_InfoRatio_s.for'
            file18 = dirTarget + '\SSPAunv11FX_InfoRatio_s_' + folder + '.for'
            shutil.copyfile(file17, file18)
            file19 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) + '\SSPAunv11FX_MeanRetTim_s.for'
            file20 = dirTarget + '\SSPAunv11FX_MeanRetTim_s_' + folder + '.for'
            shutil.copyfile(file19, file20)
            file21 = dirSource + os.sep + folder + '\All seed' + str(seedNumber) + '\SSPAunv11FX_InfoRatioTim_s.for'
            file22 = dirTarget + '\SSPAunv11FX_InfoRatioTim_s_' + folder + '.for'
            shutil.copyfile(file21, file22)
        except:
            print folder
            pass

