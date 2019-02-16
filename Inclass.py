import pandas as pd
import numpy as np

df1 = pd.read_csv('pd_merge_1.csv')
df2 = pd.read_csv('pd_merge_2.csv')

print (len(df1))
print (len(df2))
print (df1.columns)
print (df2.columns)

df1.loc[:,'xrd'] = df1.loc[:,'xrd'].fillna(0)

df_merge = pd.merge(df1,df2,on=list(set(list(df1)) & set(list(df2))),how='left')

df_merge = df_merge.drop_duplicates(keep = 'first')

df_result = df_merge.dropna(subset = ['cusip','gvkey','fyear'], how = 'any')

df_result.to_csv('mergeResult.csv')