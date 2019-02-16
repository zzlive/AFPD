import pandas as pd
import os
import numpy as np
import datetime

pd.options.display.expand_frame_repr=False

path = r'C:\便捷\工作\Course\MFIN7033 Advanced Financial Programming and Databases\2018 Fall Projects\Datetime\data'

def fun_datetime():
    # Import data
    df_daily = pd.read_csv(os.path.join(path, 'ukpound_exchange.csv'), engine='python', index_col=None)
    # Convert str to datetime
    df_daily.iloc[:,1] = [datetime.datetime.strptime(df_daily.iloc[i,1],'%m/%d/%Y') for i in range(len(df_daily.index))]
    # Find the index of last day of each month
    list_m = [df_daily.iloc[i,1].month/100 + df_daily.iloc[i,1].year for i in range(len(df_daily.index))]
    index = np.cumsum(np.unique(list_m, return_counts=True)[1])
    # Export data
    df_month = df_daily.iloc[index-1,1:]
    df_month.to_csv(os.path.join(path, 'datetime_output_data.csv'),index=None)
    return df_month

if __name__ == '__main__':
    fun_datetime()
