from fuzzywuzzy import process
import pandas as pd
import os
import multiprocessing
from timeit import default_timer as timer

path = r'C:\便捷\工作\Course\MFIN7033 Advanced Financial Programming and Databases\2018 Fall Projects\Fuzzy and multiprocessing\data'
ACQUIRER_SET = pd.read_excel(path+'\\'+'acquirers.xlsx')
BANK_SET = pd.read_csv(open(os.path.join(path, 'bank_names.csv'), encoding='utf-8'))
# To reduce noises
acquirer = list(map(lambda x: x.upper(), ACQUIRER_SET.loc[:, "Acquirer Name"]))
rep_str = ["BANKS", "BANK", "BANCORP", "BANC", "BANCSHARES", "FINANCIAL"]
for rep in rep_str:
    acquirer = list(map(lambda x: x.replace(rep, ''), acquirer))


# Parallel Function
def find_element(idx):
    extract = process.extract(acquirer[idx], BANK_SET.loc[:, "bank_names"], limit=3)
    print(idx)
    return extract, idx


if __name__ == '__main__':

    ts = timer()

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

    full_lst = pool.map(find_element, ACQUIRER_SET.index, chunksize=1)
    ACQUIRER_SET["1"] = ACQUIRER_SET["2"] = ACQUIRER_SET["3"] = None

    # Output
    for item in full_lst:
        idx = item[1]
        for var in range(3):
            ACQUIRER_SET.loc[idx, "%d" % (var + 1)] = item[0][var][0]
    ACQUIRER_SET.to_csv('output.csv', index=False)

    te = timer()
    print("%.2f seconds" % (te - ts))
