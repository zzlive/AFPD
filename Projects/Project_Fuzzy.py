import pandas as pd
import numpy as np
import os
from fuzzywuzzy import fuzz,process
pd.options.display.expand_frame_repr=False

# Import data
path = r'C:\便捷\工作\Course\MFIN7033 Advanced Financial Programming and Databases\2018 Fall Projects\Fuzzy and multiprocessing\data'
df_acquirers = pd.read_excel(os.path.join(path, 'acquirers.xlsx'), index_col=None)
df_bank_names = pd.read_csv(open(os.path.join(path, 'bank_names.csv'), encoding='utf-8'))

# Data processing, remove interference in acquirers and construct dataFrame to be updated
def fun_remove_interference():
    temp = df_acquirers.iloc[:, 2]
    re_items = ['BANCORP','BANCSHARES','BANK','BANKS','FINANCIAL','FINL','PARTNERS']
    uni_acquirers = []
    for i in range(len(temp)):
        item_list = temp[i].upper().split()
        for i,item in enumerate(item_list):
            if item not in re_items:
                if i == 0:
                    item_to_be_matched = item
                else:
                    item_to_be_matched = item_to_be_matched + " " + item
        uni_acquirers.append(item_to_be_matched)
    df_result = pd.DataFrame(df_acquirers.iloc[:, 2])
    for i in range(5): df_result.insert(i + 1, i, 0)
    return (df_result,uni_acquirers)

df_result, uni_acquirers = fun_remove_interference()

def fun_average_ratio(acquirer,name):
    '''
    calculate the average number of four type matching ratio.
    :param acquirer:str, element to be matched
    :param name:str, element to be matched
    :return:ratio
    '''
    return np.mean([fuzz.partial_ratio(acquirer, name),fuzz.ratio(acquirer, name),fuzz.token_sort_ratio(acquirer, name),fuzz.token_set_ratio(acquirer, name)])


def fun_match(n_start):
    '''
    The function is to fuzzy match the acquirers and the bank names
    :param n_start: Int, the start number of the matching
    :return: Dataframe, 12-lines results
    '''
    for i in range(n_start, min(n_start + 12, len(df_acquirers))):
        ratio_list = []
        for j in range(len(df_bank_names)):
            ratio_list.append(fun_average_ratio(uni_acquirers[i], df_bank_names.iloc[j, 1]))
        max_match_list = []
        for k in range(5):
            max_match_list.append(df_bank_names.iloc[ratio_list.index(max(ratio_list)), 1])
            ratio_list[ratio_list.index(max(ratio_list))] = 0
        df_result.iloc[i, 1:] = max_match_list
    return (df_result.iloc[n_start: min(n_start + 12, len(df_acquirers)),:])

def fun_match_2(n_start):
    '''
    The function is to fuzzy match the acquirers and the bank names
    :param n_start: Int, the start number of the matching
    :return: Dataframe, 12-lines results
    '''
    for i in range(n_start, min(n_start + 12, len(df_acquirers))):
        max_match_list = process.extract(uni_acquirers[i],df_bank_names.iloc[:, 1],limit=5)
        df_result.iloc[i, 1:] = [item[0] for item in max_match_list]
    return(df_result.iloc[n_start: min(n_start + 12, len(df_acquirers)),:])

