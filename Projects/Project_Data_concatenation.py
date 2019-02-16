import pandas as pd
import os
pd.options.display.expand_frame_repr=False

path = r'C:\便捷\工作\Course\MFIN7033 Advanced Financial Programming and Databases\2018 Fall Projects\Data concatenation\data'

def fun_connection():
    df_2014 = pd.read_csv(os.path.join(path,'2014.csv'),engine='python',index_col = [0])
    df_2015 = pd.read_csv(os.path.join(path,'2015.csv'),engine='python',index_col = [0])
    df_output = pd.concat([df_2014,df_2015],axis = 0)
    df_output.to_csv(os.path.join(path,'concatenation_output_data.csv'))
    return df_output

if __name__ == '__main__':
    fun_connection()

    import numpy as np
    def fun(w):
        return (0.05*w+0.1)/(0.75*w**2+0.25)**0.5
    for i in range(100):
        print (i,fun(i/100))