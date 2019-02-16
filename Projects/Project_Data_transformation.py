import pandas as pd
import os
import numpy as np
import datetime
pd.options.display.expand_frame_repr=False

path = r'C:\便捷\工作\Course\MFIN7033 Advanced Financial Programming and Databases\Projects_Zhao Zhao\Data transformation'

def fun_1_to_25(df_deal_1,df_col):
    '''
    Convert 1 row data to 25 quarter data.
    :param df_deal_1: DataFrame, 1 row data.
    :param df_col: List, quarter data's columns
    :return: DataFrame, 25 rows quarter data
    '''
    df_quarter_25 = pd.concat([df_deal_1.iloc[:14,]] * 25,axis = 1).T #Generate first 14 columns
    df_quarter_25.insert(len(df_quarter_25.columns),df_col[14],[i for i in range(-12,13,1)]) #insert 15 column
    df_quarter_25.index = range(25) #change index
    df_quarter_25 = pd.concat([df_quarter_25,pd.DataFrame(np.array(list(([df_deal_1[(col + '_' + str(j - 12).replace('-', '_')).replace('_0', '')] for j in range(25)] for col in df_col[15:]))).T, columns=df_col[15:])],axis = 1)
    return df_quarter_25

def fun_main(df_deal,quarter_col):
    '''
    Convert all data
    :param df_deal: DataFrame, deal data
    :param quarter_col: List, quarter data's columns
    :return: DataFrame, output data
    '''
    results = []
    for i in range(len(df_deal.index)):
        results.append(fun_1_to_25(df_deal.iloc[i, :], quarter_col))
    result = pd.concat(results)
    return result

if __name__ == '__main__':
    # Import data
    starttime = datetime.datetime.now()
    df_deal = pd.read_csv(os.path.join(path,'deal_level_data.csv'),engine='python',index_col = None)
    # Get useful columns
    quarter_col = ['Deal_Number',	'Date_Announced',	'Year_Announced',	'Acquirer_Name_clean',	'Acquirer_Primary_SIC', 'Acquirer_State_abbr',	'Acquirer_CUSIP',	'Acquirer_Ticker', 	'Target_Name_clean',	'Target_Primary_SIC','Target_State_abbr',	'Target_CUSIP',	'Target_Ticker	','Attitde',	'quarter_to_the_event_date','quarter', 'Com_Net_Charge_Off',	'Com_Insider_Loan',	'Com_NIE',	'Com_NII',	'Com_NIM','Com_ROA',	'Com_Total_Assets',	'Com_AvgSalary',	'Com_EmployNum',	'Com_TtlSalary','Com_AvgSalary_log',	'Com_EmployNum_log',	'Com_TtlSalary_log',	'Tar_Net_Charge_Off',	'Tar_Insider_Loan','Tar_NIE',	'Tar_NII',	'Tar_NIM',	'Tar_ROA',	'Tar_Total_Assets',	'Tar_AvgSalary','Tar_EmployNum','Tar_TtlSalary',	'Tar_AvgSalary_log',	'Tar_EmployNum_log',	'Tar_TtlSalary_log']
    # Convert and export data
    df_quarter = fun_main(df_deal,quarter_col)
    df_quarter.to_csv(os.path.join(path,'transformation_output_data.csv'),index =False)
    endtime = datetime.datetime.now()
    print (endtime - starttime)
