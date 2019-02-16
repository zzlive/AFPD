import os
import shutil
import csv

dirSource = r'D:\Files\Documents\HKU Materials\HKU Research\Po - ForEX\updateDataReplication'
dirTarget = r'D:\Files\Documents\HKU Materials\HKU Research\Po - ForEX\updateDataUSDasJP'

for folder in os.listdir(dirSource):
    if len(folder)<=4:
        fileName = dirSource + os.sep + folder + os.sep + 'TRADINGCOST2015.txt'
        targetFileName = dirTarget + os.sep + folder + os.sep + 'TRADINGCOST2015.txt'
#         try:
        newTransactionCostFile = []
        with open(fileName, 'r') as transactionCostFile:
            for line in transactionCostFile:
                newTransactionCostFile.append(line.strip().split('\t'))
        
        for line in newTransactionCostFile:
            line[3] = str(float(line[3])+0.0001)

#         if not os.path.exists(targetFileName):
#             os.makedirs(targetFileName)

        with open(targetFileName, 'w') as txtfile:
            linewriter = csv.writer(txtfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for line in newTransactionCostFile:
                linewriter.writerow([line[0],line[1],line[2],line[3]])
            
#         except:
#             print folder
#             pass