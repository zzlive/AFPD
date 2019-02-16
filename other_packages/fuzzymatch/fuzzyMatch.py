import csv, sys, time, os
from multiprocessing import Pool
from fuzzywuzzy import fuzz
import pandas as pd

base_path = r'D:\C Disk Transfer\Desktop\AFPD\other_packages\fuzzymatch'
MnAfirmNameCUSIPLists = pd.read_csv(base_path + os.sep + '20160313AcquirerList.csv')
# MnAfirmNameCUSIPLists.columns = ['bank','cusip']

#base_path = r'D:\C Disk Transfer\Desktop\AFPD\other_packages\fuzzymatch'
fileRawData = pd.read_csv(base_path + os.sep + 'concise_centrality_firm_connection_via_ceo_chairman_after_1968.csv')
# fileRawData = fileRawData['Id']

CUT = 70

saved_file_name = base_path + os.sep + 'test_save.csv'

def mainFunction(index):
    
    global fileRawData

#     listToWrite = []
    MnAfirmNameCUSIP = MnAfirmNameCUSIPLists['Acquirer Name'].ix[index]
#     try:
    for rawfileInfo in fileRawData['Id'].tolist():
        if rawfileInfo.strip().split(' ')[0] == MnAfirmNameCUSIP.strip().split(' ')[0]: #MnAfirmNameCUSIP is an element of MnAfirmNameCUSIPListFile['bank'].tolist()
            if ((fuzz.ratio(MnAfirmNameCUSIP.lower(), rawfileInfo.lower())>CUT) and 
                (fuzz.partial_ratio(MnAfirmNameCUSIP.lower(), rawfileInfo.lower())>CUT) and
                (fuzz.token_sort_ratio(MnAfirmNameCUSIP.lower(), rawfileInfo.lower())>CUT) and 
                (fuzz.token_set_ratio(MnAfirmNameCUSIP.lower(), rawfileInfo.lower())>CUT)):
#             if (fuzz.partial_ratio(MnAfirmNameCUSIP.lower(), rawfileInfo.lower())>CUT):
#                     listToWrite.append(MnAfirmNameCUSIP)

                MnAfirmNameCUSIP = MnAfirmNameCUSIP.replace(',',' ')
                MnAfirmNameCUSIP = MnAfirmNameCUSIP.replace('|',' ')
                rawfileInfo = rawfileInfo.replace(',',' ')
                rawfileInfo = rawfileInfo.replace('|',' ')
                
                csvfile = open(saved_file_name, 'ab+')
                linewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                linewriter.writerow([MnAfirmNameCUSIP, rawfileInfo])

            else:
                pass
#     except:
#         pass
        

if __name__ == '__main__':
    start_time = time.time()
     
    p = Pool(processes=7)
    p.map(mainFunction, range(len(MnAfirmNameCUSIPLists)))
    
    print("--- %s seconds ---" % (time.time() - start_time))



